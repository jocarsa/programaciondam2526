#now python script, parse all the txt files 
#inside videotutoriales folder, create chunks with overlapping, 
#compute vectors with chroma, and save to chroma database

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parse all .txt files inside a folder (default: ./videotutoriales),
split into overlapping chunks, embed with SentenceTransformers,
and store everything into a persistent ChromaDB collection.

Install:
  pip install chromadb sentence-transformers numpy

Run:
  python ingest_txt_to_chroma.py \
    --input_dir "./videotutoriales" \
    --persist_dir "./chroma_data" \
    --collection "videotutoriales_es" \
    --chunk_chars 1200 \
    --overlap_chars 200 \
    --batch_size 128
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
from pathlib import Path
from typing import Iterator, List, Dict, Tuple

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer


# -----------------------------
# Chunking
# -----------------------------
def normalize_text(s: str) -> str:
    # Keep it simple: normalize whitespace, preserve punctuation.
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def chunk_text_chars(text: str, chunk_chars: int, overlap_chars: int) -> Iterator[Tuple[int, int, str]]:
    """
    Yield (start, end, chunk) with character windowing and overlap.
    """
    if chunk_chars <= 0:
        raise ValueError("chunk_chars must be > 0")
    if overlap_chars < 0:
        raise ValueError("overlap_chars must be >= 0")
    if overlap_chars >= chunk_chars:
        raise ValueError("overlap_chars must be < chunk_chars")

    n = len(text)
    start = 0
    while start < n:
        end = min(start + chunk_chars, n)
        chunk = text[start:end].strip()
        if chunk:
            yield start, end, chunk
        if end == n:
            break
        start = max(0, end - overlap_chars)


# -----------------------------
# IDs
# -----------------------------
def stable_chunk_id(rel_path: str, start: int, end: int, chunk: str) -> str:
    """
    Stable ID so re-ingestion updates the same chunk instead of duplicating.
    """
    h = hashlib.sha1()
    h.update(rel_path.encode("utf-8"))
    h.update(b"|")
    h.update(f"{start}:{end}".encode("utf-8"))
    h.update(b"|")
    # Include content hash too, so edits change ids (optional). If you prefer
    # IDs stable even when content changes, remove the chunk part.
    h.update(hashlib.sha1(chunk.encode("utf-8")).digest())
    return "chunk:" + h.hexdigest()


# -----------------------------
# File discovery
# -----------------------------
def iter_txt_files(root: Path) -> Iterator[Path]:
    for p in root.rglob("*.txt"):
        if p.is_file():
            yield p


# -----------------------------
# Main ingestion
# -----------------------------
def ingest(
    input_dir: Path,
    persist_dir: Path,
    collection_name: str,
    model_name: str,
    chunk_chars: int,
    overlap_chars: int,
    batch_size: int,
) -> None:
    model = SentenceTransformer(model_name)

    client = chromadb.PersistentClient(
        path=str(persist_dir),
        settings=Settings(anonymized_telemetry=False),
    )

    collection = client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"},
    )

    all_files = list(iter_txt_files(input_dir))
    if not all_files:
        print(f"No .txt files found in: {input_dir}")
        return

    print(f"Found {len(all_files)} .txt files in: {input_dir}")
    print(f"Persist dir: {persist_dir}")
    print(f"Collection: {collection_name}")
    print(f"Model: {model_name}")
    print(f"Chunk chars: {chunk_chars} | Overlap chars: {overlap_chars} | Batch: {batch_size}")
    print("-" * 80)

    batch_ids: List[str] = []
    batch_docs: List[str] = []
    batch_metas: List[Dict] = []

    total_chunks = 0
    total_files = 0

    for file_path in all_files:
        total_files += 1
        rel_path = str(file_path.relative_to(input_dir))
        try:
            raw = file_path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"[SKIP] Could not read {rel_path}: {e}")
            continue

        text = normalize_text(raw)
        if not text:
            print(f"[SKIP] Empty after normalization: {rel_path}")
            continue

        file_chunks = 0
        for start, end, chunk in chunk_text_chars(text, chunk_chars, overlap_chars):
            cid = stable_chunk_id(rel_path, start, end, chunk)

            meta = {
                "source_file": rel_path,
                "start_char": start,
                "end_char": end,
                "chunk_chars": len(chunk),
            }

            batch_ids.append(cid)
            batch_docs.append(chunk)
            batch_metas.append(meta)

            file_chunks += 1
            total_chunks += 1

            if len(batch_docs) >= batch_size:
                _flush_batch(collection, model, batch_ids, batch_docs, batch_metas)
                batch_ids.clear()
                batch_docs.clear()
                batch_metas.clear()

        print(f"[OK] {rel_path} -> {file_chunks} chunks")

    # Flush remaining
    if batch_docs:
        _flush_batch(collection, model, batch_ids, batch_docs, batch_metas)

    print("-" * 80)
    print(f"Done. Files processed: {total_files} | Total chunks stored: {total_chunks}")


def _flush_batch(collection, model, ids: List[str], docs: List[str], metas: List[Dict]) -> None:
    # Encode and upsert
    embeddings = model.encode(docs, normalize_embeddings=True).tolist()
    collection.upsert(
        ids=ids,
        documents=docs,
        metadatas=metas,
        embeddings=embeddings,
    )
    print(f"  -> Upserted batch: {len(docs)}")


def main():
    ap = argparse.ArgumentParser(description="Ingest .txt files into ChromaDB with overlapping chunks.")
    ap.add_argument("--input_dir", default="./videotutoriales", help="Folder containing .txt files (recursive).")
    ap.add_argument("--persist_dir", default="./chroma_data", help="ChromaDB persistent directory.")
    ap.add_argument("--collection", default="videotutoriales_es", help="Chroma collection name.")
    ap.add_argument(
        "--model",
        default="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        help="SentenceTransformers model name/path.",
    )
    ap.add_argument("--chunk_chars", type=int, default=1200, help="Chunk size in characters.")
    ap.add_argument("--overlap_chars", type=int, default=200, help="Overlap size in characters.")
    ap.add_argument("--batch_size", type=int, default=128, help="Upsert batch size.")
    args = ap.parse_args()

    input_dir = Path(args.input_dir).resolve()
    persist_dir = Path(args.persist_dir).resolve()

    if not input_dir.exists() or not input_dir.is_dir():
        raise SystemExit(f"input_dir does not exist or is not a directory: {input_dir}")

    persist_dir.mkdir(parents=True, exist_ok=True)

    ingest(
        input_dir=input_dir,
        persist_dir=persist_dir,
        collection_name=args.collection,
        model_name=args.model,
        chunk_chars=args.chunk_chars,
        overlap_chars=args.overlap_chars,
        batch_size=args.batch_size,
    )


if __name__ == "__main__":
    main()

#now please a search engine on python with input on console 
#- over the database created

# no CLI arguments, all hardcoded

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple console semantic search over an existing ChromaDB collection.
- No CLI arguments: everything is hardcoded below.
- Reads queries from input()
- Searches the ChromaDB collection created by your ingestion script
- Prints Top-K results with similarity (%) and source metadata

Requirements:
  pip install chromadb sentence-transformers numpy
"""

import os
from typing import Any, Dict, List

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer


# =========================
# HARDCODED CONFIG
# =========================
PERSIST_DIR = os.path.abspath("./chroma_data")     # same as ingestion
COLLECTION_NAME = "videotutoriales_es"             # same as ingestion
MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

TOP_K = 8                  # results per query
SHOW_CHARS = 320           # snippet length to print


def fmt_meta(meta: Dict[str, Any]) -> str:
    if not meta:
        return ""
    src = meta.get("source_file", "?")
    s = meta.get("start_char", "?")
    e = meta.get("end_char", "?")
    return f"{src} [{s}-{e}]"


def clamp01(x: float) -> float:
    if x < 0.0:
        return 0.0
    if x > 1.0:
        return 1.0
    return x


def main():
    # Load embedding model
    model = SentenceTransformer(MODEL_NAME)

    # Open Chroma persistent DB
    client = chromadb.PersistentClient(
        path=PERSIST_DIR,
        settings=Settings(anonymized_telemetry=False)
    )
    collection = client.get_collection(name=COLLECTION_NAME)

    print("Chroma semantic search (console)")
    print(f"Persist dir : {PERSIST_DIR}")
    print(f"Collection  : {COLLECTION_NAME}")
    print(f"Model       : {MODEL_NAME}")
    print(f"Top-K       : {TOP_K}")
    print("\nWrite a query and press ENTER (empty line = exit)\n")

    while True:
        query = input("search> ").strip()
        if not query:
            print("Bye.")
            break

        q_emb = model.encode(query, normalize_embeddings=True).tolist()

        # With cosine space: distance ~= 1 - cosine_similarity
        res = collection.query(
            query_embeddings=[q_emb],
            n_results=TOP_K,
            include=["documents", "metadatas", "distances"]
        )

        docs: List[str] = (res.get("documents") or [[]])[0]
        metas: List[Dict[str, Any]] = (res.get("metadatas") or [[]])[0]
        dists: List[float] = (res.get("distances") or [[]])[0]

        if not docs:
            print("No results.\n")
            continue

        print("\nResults:")
        for i, (doc, meta, dist) in enumerate(zip(docs, metas, dists), start=1):
            dist = float(dist)
            sim = clamp01(1.0 - dist)
            pct = sim * 100.0

            snippet = (doc or "").replace("\n", " ").strip()
            if len(snippet) > SHOW_CHARS:
                snippet = snippet[:SHOW_CHARS].rstrip() + "…"

            print(f"{i:02d}. {pct:6.2f}%  |  {fmt_meta(meta)}")
            print(f"    {snippet}\n")

        print("-" * 80)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import math
import chromadb
from chromadb.config import Settings

def cosine_similarity(a, b) -> float:
    # cos(a,b) = dot(a,b) / (||a|| * ||b||)
    dot = 0.0
    na = 0.0
    nb = 0.0
    for x, y in zip(a, b):
        dot += x * y
        na += x * x
        nb += y * y
    denom = math.sqrt(na) * math.sqrt(nb)
    return dot / denom if denom != 0.0 else 0.0

def main():
    persist_dir = os.path.abspath("./chroma_data")

    client = chromadb.PersistentClient(
        path=persist_dir,
        settings=Settings(anonymized_telemetry=False)
    )

    collection = client.get_collection(name="diccionario_es")

    words = ["perro", "gato", "mesa"]
    ids = [f"word:{w}" for w in words]

    res = collection.get(ids=ids, include=["documents", "embeddings"])

    # Map palabra -> embedding
    doc_to_emb = {doc: emb for doc, emb in zip(res["documents"], res["embeddings"])}

    pairs = [("perro", "gato"), ("perro", "mesa"), ("gato", "mesa")]

    print("Cosine similarity (pair by pair):")
    for a, b in pairs:
        sim = cosine_similarity(doc_to_emb[a], doc_to_emb[b])
        print(f"- {a} vs {b}: {sim:.6f}")

    # (Opcional) también mostrar "distancia coseno" = 1 - similitud
    print("\nCosine distance (1 - similarity):")
    for a, b in pairs:
        sim = cosine_similarity(doc_to_emb[a], doc_to_emb[b])
        dist = 1.0 - sim
        print(f"- {a} vs {b}: {dist:.6f}")

if __name__ == "__main__":
    main()

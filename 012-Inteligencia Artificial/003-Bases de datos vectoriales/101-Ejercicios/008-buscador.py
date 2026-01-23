#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import math
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

def cosine_similarity(a, b) -> float:
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
    collection_name = "sentencias_es"

    model = SentenceTransformer(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    client = chromadb.PersistentClient(
        path=persist_dir,
        settings=Settings(anonymized_telemetry=False)
    )
    collection = client.get_collection(name=collection_name)

    # ⚠️ NO usar "or []" con numpy arrays
    stored = collection.get(include=["documents", "embeddings", "metadatas"])

    ids = stored["ids"]
    docs = stored["documents"]
    embs = stored["embeddings"]
    metas = stored["metadatas"]

    if len(docs) == 0:
        print("No hay frases almacenadas en la colección.")
        return

    print(f"Cargadas {len(docs)} frases desde Chroma")
    print("Introduce una frase para comparar (ENTER para salir)\n")

    while True:
        query = input("Tu frase> ").strip()
        if not query:
            print("Saliendo.")
            break

        q_emb = model.encode(query, normalize_embeddings=True).tolist()

        resultados = []

        for doc_id, doc, emb in zip(ids, docs, embs):
            sim = cosine_similarity(q_emb, emb)
            porcentaje = max(0.0, min(sim, 1.0)) * 100.0
            resultados.append((porcentaje, doc_id, doc))

        resultados.sort(reverse=True, key=lambda x: x[0])

        print("\nSimilitud semántica:")
        for pct, doc_id, doc in resultados:
            print(f"- {pct:6.2f}%  ({doc_id})  {doc}")

        print()

if __name__ == "__main__":
    main()

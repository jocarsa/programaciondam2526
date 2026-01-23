#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

def main():
    # 1) Modelo de embeddings
    model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    # 2) Directorio persistente (queda en disco)
    persist_dir = os.path.abspath("./chroma_data")

    # 3) Cliente Chroma persistente
    client = chromadb.PersistentClient(
        path=persist_dir,
        settings=Settings(anonymized_telemetry=False)
    )

    # 4) Colección (similar a una "tabla" lógica)
    collection = client.get_or_create_collection(
        name="diccionario_es",
        metadata={"hnsw:space": "cosine"}  # opción típica para embeddings
    )

    # 5) Documentos a guardar
    words = ["perro", "gato", "mesa"]
    ids = [f"word:{w}" for w in words]
    metadatas = [{"tipo": "palabra", "idioma": "es"} for _ in words]

    # 6) Embeddings (lista de listas floats)
    embeddings = model.encode(words, normalize_embeddings=True).tolist()

    # 7) Insertar / upsert (si existe, se actualiza)
    collection.upsert(
        ids=ids,
        documents=words,        # guardamos el texto original como documento
        metadatas=metadatas,
        embeddings=embeddings
    )

    # 8) Comprobación rápida: consulta por similitud
    query = "animal doméstico"
    q_emb = model.encode(query, normalize_embeddings=True).tolist()

    results = collection.query(
        query_embeddings=[q_emb],
        n_results=3,
        include=["documents", "metadatas", "distances"]
    )

    print("Persist dir:", persist_dir)
    print("Inserted:", ids)
    print("\nQuery:", query)
    for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
        print(f"- {doc} | {meta} | distance={dist:.6f}")

if __name__ == "__main__":
    main()

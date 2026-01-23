#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

def main():
    # Embedding model (multilingual, fast, solid)
    model = SentenceTransformer(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    # Persistent storage directory
    persist_dir = os.path.abspath("./chroma_data")

    # Chroma persistent client
    client = chromadb.PersistentClient(
        path=persist_dir,
        settings=Settings(anonymized_telemetry=False)
    )

    # Create or load collection
    collection = client.get_or_create_collection(
        name="sentencias_es",
        metadata={"hnsw:space": "cosine"}
    )

    # Spanish sentences
    sentences = [
        "El perro duerme tranquilamente junto a la chimenea.",
        "El gato observa atentamente a los pájaros desde la ventana.",
        "La mesa de madera está cubierta de libros antiguos.",
        "La inteligencia artificial está transformando el desarrollo de software.",
        "Los estudiantes aprenden programación con ejercicios prácticos.",
        "Me gusta tomar café por la mañana mientras leo las noticias.",
        "El ordenador portátil se quedó sin batería durante la reunión.",
        "La profesora explicó el concepto con un ejemplo muy claro."
    ]

    # IDs and metadata
    ids = [f"sent:{i}" for i in range(len(sentences))]
    metadatas = [
        {"idioma": "es", "tipo": "oracion"} for _ in sentences
    ]

    # Generate embeddings
    embeddings = model.encode(
        sentences,
        normalize_embeddings=True
    ).tolist()

    # Insert / update
    collection.upsert(
        ids=ids,
        documents=sentences,
        metadatas=metadatas,
        embeddings=embeddings
    )

    print("Inserted sentences into ChromaDB:")
    for i, s in zip(ids, sentences):
        print(f"- {i}: {s}")

    print("\nPersisted at:", persist_dir)

if __name__ == "__main__":
    main()

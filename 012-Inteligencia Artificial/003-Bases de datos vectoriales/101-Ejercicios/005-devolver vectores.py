#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import chromadb
from chromadb.config import Settings

def main():
    # Directorio persistente (debe ser el mismo usado al insertar)
    persist_dir = os.path.abspath("./chroma_data")

    # Cliente Chroma persistente
    client = chromadb.PersistentClient(
        path=persist_dir,
        settings=Settings(anonymized_telemetry=False)
    )

    # Obtener la colección existente
    collection = client.get_collection(name="diccionario_es")

    # IDs de las palabras a recuperar
    ids = ["word:perro", "word:gato", "word:mesa"]

    # Recuperar datos
    result = collection.get(
        ids=ids,
        include=["documents", "embeddings", "metadatas"]
    )

    # Mostrar resultados
    for doc, emb, meta in zip(
        result["documents"],
        result["embeddings"],
        result["metadatas"]
    ):
        print("Palabra:", doc)
        print("Metadatos:", meta)
        print("Longitud del vector:", len(emb))
        print("Vector (primeros 10 valores):", emb)
        print("-" * 60)

if __name__ == "__main__":
    main()

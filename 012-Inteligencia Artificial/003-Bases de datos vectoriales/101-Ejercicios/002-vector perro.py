from sentence_transformers import SentenceTransformer
import numpy as np

# Load a small, fast multilingual embedding model
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# Word to embed
word = "perro"

# Generate embedding
vector = model.encode(word)

# Show results
print("Word:", word)
print("Vector length:", len(vector))
print("Vector (first 10 values):")
print(np.round(vector[:10], 6))

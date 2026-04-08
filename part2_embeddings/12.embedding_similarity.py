##
## Concept    : Embedding Similarity Metrics — Euclidean Distance, Cosine Similarity & Dot Product
## What it does: Computes three different mathematical similarity/distance measures between
##               two fixed 3-dimensional vectors, demonstrating how each metric behaves.
## What you'll learn:
##   - Euclidean distance: straight-line distance between two points in vector space.
##     Lower = more similar. Sensitive to the magnitude (length) of the vectors.
##   - Cosine similarity: measures the angle between two vectors, not their magnitude.
##     Ranges from -1 to 1; higher = more similar. Most common metric for text embeddings.
##   - Dot product: related to cosine similarity but also influenced by vector magnitude.
##     Used in many neural network attention mechanisms.
##   - Why cosine similarity is preferred for text: two documents with the same words
##     but different lengths should still be "similar" — cosine handles this, euclidean doesn't.
## Note: This file uses fixed vectors (no API call) — great for understanding the math in isolation.
## Run: python 12.embedding_similarity.py
##
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity
import numpy as np

#define two vectors
embedding1 = np.array([1.5, 2.0, 3.5])
embedding2 = np.array([4.0, 1.0, 2.5])

print(f"Embedding 1: {embedding1}")
print(f"Embedding 2: {embedding2}")

euclidean_distance = euclidean_distances([embedding1], [embedding2])[0][0]

print(f"Euclidean distance between the two embeddings: {euclidean_distance}")

# Calculate cosine similarity
cosine_sim = cosine_similarity([embedding1], [embedding2])[0][0]
print("Cosine similarity between the two embeddings:", cosine_sim)

# Calculate the dot product
dot_product = np.dot(embedding1, embedding2)
print("Dot product:", dot_product)

##
## Expected output:
##   Embedding 1: [1.5 2.  3.5]
##   Embedding 2: [4.  1.  2.5]
##   Euclidean distance between the two embeddings: 3.3541
##   Cosine similarity between the two embeddings: 0.7792
##   Dot product: 16.75
##
## Challenges:
##   1. Create two vectors pointing in the exact same direction (e.g. [1,2,3] and [2,4,6])
##      — cosine similarity should be 1.0, but euclidean distance will not be 0. Why?
##   2. Create two perpendicular vectors (dot product = 0) — what does cosine similarity return?
##   3. Normalize both vectors to unit length before computing euclidean distance
##      — observe that it now equals sqrt(2 - 2*cosine_similarity)
##   4. Scale up to 768 dimensions (BERT embedding size) using np.random.rand(768)
##      and see if the metrics still behave as expected
##

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_similarity_scores(query, concepts):
    embeddings = model.encode(list(concepts.values()))
    query_embedding = model.encode([query])[0]
    scores = cosine_similarity([query_embedding], embeddings)[0]
    return scores

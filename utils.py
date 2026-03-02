from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    return model.encode(texts)

def similarity_score(query_embedding, article_embeddings):
    scores = cosine_similarity([query_embedding], article_embeddings)
    return scores[0]
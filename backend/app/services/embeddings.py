from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer("all-MiniLM-L6-v2")


def embed_texts(texts):
    embeddings = MODEL.encode(texts, show_progress_bar=False)
    return [list(map(float, emb)) for emb in embeddings]


def embed_text(text):
    return embed_texts([text])[0]

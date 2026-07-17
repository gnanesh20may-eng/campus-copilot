from fastembed import TextEmbedding

MODEL = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")


def embed_texts(texts):
    embeddings = list(MODEL.embed(texts))
    return [list(map(float, emb)) for emb in embeddings]


def embed_text(text):
    return embed_texts([text])[0]

import uuid

from embeddings import EmbeddingModel
from vector_store import VectorStore


class MemoryAgent:

    def __init__(self):

        self.embedder = EmbeddingModel()
        self.vector_db = VectorStore()

    def remember(self, text):

        embedding = self.embedder.encode([text])

        self.vector_db.add(
            ids=[str(uuid.uuid4())],
            documents=[text],
            embeddings=embedding
        )

    def recall(self, query):

        query_embedding = self.embedder.encode([query])

        results = self.vector_db.search(query_embedding)

        return results["documents"][0]
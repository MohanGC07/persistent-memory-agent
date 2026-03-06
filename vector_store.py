import chromadb


class VectorStore:

    def __init__(self):

        # persistent database
        self.client = chromadb.PersistentClient(
            path="data/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="memory"
        )

    def add(self, ids, documents, embeddings):

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings
        )

    def search(self, query_embedding, k=3):

        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=k
        )

        return results
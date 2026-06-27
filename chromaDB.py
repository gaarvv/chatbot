import chromadb

class chromaDB:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.collection = self.client.get_or_create_collection(
                name="papers"
            )
    
    def add_documents(self, ids, documents, embeddings):
        """
        Store documents and their embeddings in ChromaDB.
        """

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist()
        )
    
    def add_documents(self, ids, documents, embeddings):
        """
        Store documents and their embeddings in ChromaDB.
        """

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist()
        )

    def search(self, query_embedding, n_results=5):
        """
        Search for the most similar documents.
        """

        return self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=n_results
        )
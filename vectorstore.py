import logging
from langchain.vectorstores import FAISS

class VectorStore:
    def __init__(self):
        pass
    
    def vectorstore(self, documents, embeddings):
        try:
            vectorstore = FAISS.from_documents(documents=documents,
                                            embedding=embeddings)
            return vectorstore  
        except Exception as e:
            logging.error(f"Error in creating vector {e}")
            raise e
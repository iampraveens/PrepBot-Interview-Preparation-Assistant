import logging
from langchain.embeddings import HuggingFaceEmbeddings

class Embeddings:
    def __init__(self, model_name, model_kwargs):
        self.model_name = model_name
        self.model_kwargs = model_kwargs
    
    def embed_documents(self):
        try:
            embeddings = HuggingFaceEmbeddings(model_name=self.model_name, 
                                            model_kwargs=self.model_kwargs)
            return embeddings
        except Exception as e:
            logging.error(f"Error in embedding text {e}")
            raise e
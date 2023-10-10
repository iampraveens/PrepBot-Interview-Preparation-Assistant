import logging
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DataIngest:
    def __init__(self, path, glob):
        self.path = path
        self.glob = glob
    
    def ingest_data(self):
        try:
            loader = DirectoryLoader(path=self.path, glob=self.glob, loader_cls=PyPDFLoader)
            data = loader.load()
            return data
        except Exception as e:
            logging.error(f"Error loading data {e}")
            raise e
        
    def split_text(self):
        try:
            splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            data = self.ingest_data()
            documents = splitter.split_documents(data)
            return documents
        except Exception as e:
            logging.error(f"Error splitting data")
            raise e
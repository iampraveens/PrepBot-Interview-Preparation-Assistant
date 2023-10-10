import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextSplitter:
    def __init__(self, chunk_size, chunk_overlap):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def split_text(self, data):
        splitter = RecursiveCharacterTextSplitter(self.chunk_size, self.chunk_overlap)
        documents = splitter.split_documents(data)
        return documents
import logging
from langchain.llms import CTransformers

class LLMModel:
    def __init__(self, model, config, streaming):
        self.model = model
        self.config = config
        self.streaming = streaming
    
    def llm_model(self):
        llm = CTransformers(model=self.model, 
                            config=self.config, 
                            streaming=self.streaming)
        return llm
import logging
from langchain.memory import ConversationBufferMemory

class Memory:
    def __init__(self, memory_key, return_messages):
        self.memory_key = memory_key
        self.return_messages = return_messages
    
    def memory(self):
        try:
            memory = ConversationBufferMemory(memory_key=self.memory_key, 
                                            return_messages=self.return_messages)
            return memory
        except Exception as e:
            logging.error(f"Error in memory {e}")
            raise e
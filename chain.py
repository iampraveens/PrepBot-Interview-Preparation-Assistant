from langchain.chains import ConversationalRetrievalChain

class Chain:
    def __init__(self, llm, retriever, memory):
        self.llm = llm
        self.retriever = retriever
        self.memory = memory

    def chain(self):
        chain = ConversationalRetrievalChain.from_llm(llm=self.llm, 
                                                      retriever=self.retriever.as_retriever(search_kwargs={"k": 2}),
                                                      memory=self.memory)
        return chain

import os
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document

class RAGPipeline:
    def __init__(self, openai_api_key: str):
        os.environ["OPENAI_API_KEY"] = openai_api_key
        os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.llm = ChatOpenAI(model_name="mistralai/mistral-7b-instruct", temperature=0.1, max_tokens=512)
        self.vector_store = None

    def index_chunks(self, chunks):
        documents = [Document(page_content=chunk) for chunk in chunks]
        self.vector_store = FAISS.from_documents(documents, self.embeddings)

    def ask(self, query: str) -> str:
        if self.vector_store is None:
            return "No document indexed yet."
        retriever = self.vector_store.as_retriever()
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=retriever,
            return_source_documents=False
        )
        return qa_chain.run(query)

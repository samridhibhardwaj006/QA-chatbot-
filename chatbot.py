from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

from retriever import Retriever


class Chatbot:

    @staticmethod
    def answer(pdf_path, question):

        retriever = Retriever.build(pdf_path)

        llm = Ollama(
            model="llama3"
        )

        qa = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff"
        )

        result = qa.invoke(question)

        return result["result"]

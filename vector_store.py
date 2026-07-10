from langchain_chroma import Chroma

from embeddings import EmbeddingModel


class VectorDatabase:

    @staticmethod
    def create(chunks):

        embeddings = EmbeddingModel.load()

        vectordb = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings
        )

        return vectordb

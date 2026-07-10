from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:

    @staticmethod
    def load():

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        return embeddings

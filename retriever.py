from loader import PDFLoader
from splitter import DocumentSplitter
from vector_store import VectorDatabase


class Retriever:

    @staticmethod
    def build(pdf_path):

        docs = PDFLoader.load_pdf(pdf_path)

        chunks = DocumentSplitter.split_documents(docs)

        vectordb = VectorDatabase.create(chunks)

        return vectordb.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )

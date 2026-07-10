from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:
    """
    Loads PDF documents using LangChain.
    """

    @staticmethod
    def load_pdf(pdf_path: str):
        loader = PyPDFLoader(pdf_path)
        return loader.load()

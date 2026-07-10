from langchain.text_splitter import RecursiveCharacterTextSplitter


class DocumentSplitter:

    @staticmethod
    def split_documents(documents):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        return splitter.split_documents(documents)

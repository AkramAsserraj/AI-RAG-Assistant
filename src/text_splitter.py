from langchain_text_splitters import RecursiveCharacterTextSplitter

def decouper_texte(texte):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(texte)

    return chunks


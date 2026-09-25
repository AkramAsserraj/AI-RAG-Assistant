from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def creer_modele_embedding():
    return model


def creer_base_vectorielle(chunks, nom_document):

    model = creer_modele_embedding()

    metadatas = [
        {"source": nom_document}
        for _ in chunks
    ]

    base = Chroma.from_texts(
        texts=chunks,
        embedding=model,
        metadatas=metadatas,
        persist_directory="database"
    )

    return base


def charger_base_vectorielle():

    model = creer_modele_embedding()

    base = Chroma(
        persist_directory="database",
        embedding_function=model
    )

    return base


def rechercher_documents(base, question, nom_document=None):

    if nom_document:

        resultats = base.similarity_search(
            question,
            k=3,
            filter={"source": nom_document}
        )

    else:

        resultats = base.similarity_search(
            question,
            k=3
        )

    return resultats


def creer_contexte(resultats):

    contexte = ""

    for document in resultats:
        contexte += document.page_content + "\n\n"

    return contexte

def supprimer_document_de_la_base(base, nom_document):

    base.delete(
        where={"source": nom_document}
    )

    print("Embeddings du document supprimés de ChromaDB.")
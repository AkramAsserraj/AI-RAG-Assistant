from pathlib import Path

from src.document_manager import (
    ajouter_document,
    voir_documents,
    supprimer_document
)

from src.pdf_reader import lire_pdf
from src.text_splitter import decouper_texte

from src.vector_store import (
    creer_base_vectorielle,
    charger_base_vectorielle,
    rechercher_documents,
    creer_contexte,
    supprimer_document_de_la_base
)

from src.llm_manager import generer_reponse


def afficher_menu():
    print("\n" + "=" * 40)
    print("        AI RAG Assistant")
    print("=" * 40)
    print("1. Ajouter un document PDF")
    print("2. Voir les documents chargés")
    print("3. Supprimer un document")
    print("4. Poser une question")
    print("5. Quitter")
    print("=" * 40)


def lancer_menu():

    base = charger_base_vectorielle()
    historique = []

    while True:

        afficher_menu()

        choix = input("Entrez votre choix : ")

        if choix == "1":

            chemin = ajouter_document()

            if chemin is not None:

                texte = lire_pdf(chemin)

                if texte is None:
                   continue

                chunks = decouper_texte(texte)

                base = creer_base_vectorielle(chunks, chemin.name)

                print("\nDocument ajouté et indexé avec succès !")


        elif choix == "2":

            voir_documents()


        elif choix == "3":

            documents = list(Path("data").glob("*.pdf"))

            if not documents:
               print("\nAucun document à supprimer.")
               continue

            print("\nDocuments disponibles :")

            for i, document in enumerate(documents, start=1):
               print(f"{i}. {document.name}")

            try:
               choix_document = int(input("\nNuméro du document : "))
            except ValueError:
               print("\nErreur : veuillez entrer un numéro.")
               continue

            if choix_document < 1 or choix_document > len(documents):
               print("\nChoix invalide.")
               continue

            document = documents[choix_document - 1]

            supprimer_document_de_la_base(
               base,
               document.name
            )

            document.unlink()

            print("Document supprimé avec succès.")


        elif choix == "4":

            if base is None:

                print("\nAucun document n'a été chargé.")

                continue

            documents = list(Path("data").glob("*.pdf"))

            if not documents:
                print("\nAucun document chargé.")
                continue

            print("\nDocuments disponibles :")

            for i, document in enumerate(documents, start=1):
                print(f"{i}. {document.name}")

            try:
                choix_document = int(input("\nChoisissez un document : "))
            except ValueError:
                print("\nErreur : veuillez entrer un numéro.")
                continue

            if choix_document < 1 or choix_document > len(documents):
                print("\nChoix invalide.")
                continue

            nom_document = documents[choix_document - 1].name

            question = input("\nVotre question : ").strip()

            if not question:
                print("\nErreur : veuillez entrer une question.")
                continue

            resultats = rechercher_documents(
                base,
                question,
                nom_document
            )

            contexte = creer_contexte(resultats)

            reponse = generer_reponse(question, contexte)
            texte_historique = ""

            for question_precedente, reponse_precedente in historique:
                texte_historique += f"""
            Question : {question_precedente}
            Réponse : {reponse_precedente}
            """

            reponse = generer_reponse(
                question,
                contexte
            )

            historique.append((question, reponse))

            print("\nRéponse :\n")

            print(reponse)


        elif choix == "5":

            print("\nMerci d'avoir utilisé AI RAG Assistant.")
            print("À bientôt !")

            break

        else:

            print("\nChoix invalide.")

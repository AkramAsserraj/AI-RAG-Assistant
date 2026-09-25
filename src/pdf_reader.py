import fitz


def lire_pdf(chemin_pdf):

    try:
        document = fitz.open(chemin_pdf)

        texte_complet = ""

        for page in document:
            texte_complet += page.get_text()

        document.close()

    except Exception as e:
        print(f"Erreur lors de la lecture du PDF : {e}")
        return None

    if not texte_complet.strip():
        print("Erreur : ce PDF ne contient aucun texte exploitable.")
        return None

    return texte_complet

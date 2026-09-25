from pathlib import Path
import shutil
import tkinter as tk
from tkinter import filedialog

def ajouter_document():

    root = tk.Tk()
    root.withdraw()

    chemin = filedialog.askopenfilename(
        title="Choisissez un document PDF",
        filetypes=[("Fichiers PDF", "*.pdf")]
    )

    if not chemin:
        print("Aucun document sélectionné.")
        return None

    fichier = Path(chemin)

    if not fichier.exists():
        print("Erreur : le fichier n'existe pas.")
        return None

    if fichier.suffix.lower() != ".pdf":
        print("Erreur : veuillez sélectionner un fichier PDF.")
        return None

    dossier_data = Path("data")
    dossier_data.mkdir(exist_ok=True)

    destination = dossier_data / fichier.name
    destination = Path("data") / fichier.name

    if destination.exists():
        print("Ce document est déjà présent.")
        return None

    shutil.copy2(fichier, destination)

    print("Document ajouté avec succès.")

    return destination

def voir_documents():

    dossier = Path("data")

    fichiers = list(dossier.glob("*.pdf"))

    if not fichiers:
        print("Aucun document chargé.")
        return

    print("\nDocuments disponibles :")

    for i, fichier in enumerate(fichiers, start=1):
        print(f"{i}. {fichier.name}")


def supprimer_document():

    dossier = Path("data")

    fichiers = list(dossier.glob("*.pdf"))

    if not fichiers:
        print("Aucun document à supprimer.")
        return

    for i, fichier in enumerate(fichiers, start=1):
        print(f"{i}. {fichier.name}")

    try:
        choix = int(input("Numéro du document : "))
    except ValueError:
        print("Erreur : veuillez entrer un numéro.")
        return

    if 1 <= choix <= len(fichiers):
 
        fichiers[choix - 1].unlink()

        print("Document supprimé.")

    else:
        print("Erreur : ce numéro de document n'existe pas.")
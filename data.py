import os
from unidecode import unidecode

# 1) Conversion ASCII → binaire (section 3.1 du cahier technique)

def ascii_vers_base2(c):
    """
    Nous convertissons un caractère ASCII en sa représentation binaire sur 8 bits.
    Exemple : 'a' → '01100001'
    """
    return format(ord(c), "08b")


def texte_vers_ascii_binaire(texte):
    """
    Nous convertissons toute une chaîne de caractères en binaire ASCII.
    Chaque caractère devient un bloc de 8 bits.
    """
    return "".join(ascii_vers_base2(c) for c in texte)


# 2) Nettoyage des caractères non-ASCII (section 3.3.1)

def nettoyer_texte(texte):
    """
    Nous utilisons unidecode pour remplacer les caractères non-ASCII
    par leur équivalent le plus proche.
    Exemple : 'é' → 'e'
    """
    return unidecode(texte)


# 3) Lecture des fichiers d'un dossier (section 3.3.2)

def charger_fichiers(dossier):
    """
    Nous parcourons un dossier et nous chargeons tous les fichiers .txt.
    La fonction renvoie une liste de tuples : (nom_fichier, contenu).
    """
    fichiers = []

    for f in os.listdir(dossier):
        if f.endswith(".txt"):
            chemin = os.path.join(dossier, f)

            with open(chemin, "r", encoding="utf-8") as fichier:
                contenu = fichier.read()
                fichiers.append((f, contenu))

    return fichiers

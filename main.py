import sys
import os
from unidecode import unidecode
from Huffman import Huffman
from Compression import ascii_vers_base2

def traiter_fichier(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        texte = unidecode(f.read())


    #   Ce bout de code fait appel à ma fonction ascii_vers_base2 qui affiche l'encodage ASCCI de chaque
    #   caractéristiques du ou des fichiers scannés par notre script

    ascii_bits = "".join(ascii_vers_base2(c) for c in texte)
    taille_initiale = len(ascii_bits)

    print("l'encodage du texte ASCII fonctionne")



    #    Ce bout de code crée un dico vide que nous allons remplir via la boucle for ci dessous
    #   la valeur représente le charactère et la clé le nombre de fois


    freqs = {}
    for c in texte:
        freqs[c] = freqs.get(c, 0) + 1

    # Construction de l'arbre
    h = Huffman()
    h.construire(freqs)

    # Génération des codes
    codes = h.generer_codes()

    # Encodage
    texte_code = h.encoder(texte)

    # Décodage (vérification)
    texte_decode = h.decoder(texte_code)

    # Résultats
    taille_avant = len(texte) * 8
    taille_apres = len(texte_code)
    taux = taille_apres / taille_avant * 100

    print(f"\nFichier : {chemin}")
    print(f"  Taille initiale   : {taille_avant} bits")
    print(f"  Taille compressée : {taille_apres} bits")
    print(f"  Taux de compression : {taux:.1f}%")
    print(f"  Décodage correct  : {texte == texte_decode}")



    # Je vais éviter de laisser ça décommenter parce que ça remplit mon terminal de 0 et de 1
    # en gros, ça affiche l'encodage ASCII de chaque caractère du texte lu par notre programme
    # et vu que nous travaillons sur un dossier contenant plusieurs fichiers texte, cela remplit
    # le CMD et on ne s'y retrouve plus

    # print(ascii_bits)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python3 main.py input/")
        sys.exit(1)

    dossier = sys.argv[1]
    for nom_fichier in os.listdir(dossier):
        if nom_fichier.endswith(".txt"):
            chemin = os.path.join(dossier, nom_fichier)
            traiter_fichier(chemin)
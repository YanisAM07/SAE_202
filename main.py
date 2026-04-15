import sys
import os
from unidecode import unidecode
from Huffman import Huffman

def traiter_fichier(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        texte = unidecode(f.read())

    # Fréquences
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python3 main.py TEST/")
        sys.exit(1)

    dossier = sys.argv[1]
    for nom_fichier in os.listdir(dossier):
        if nom_fichier.endswith(".txt"):
            chemin = os.path.join(dossier, nom_fichier)
            traiter_fichier(chemin)
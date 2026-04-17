# voici les imports autorisé
import sys
import os
from unidecode import unidecode


from Huffman import Huffman
from Compression import ascii_vers_base2, calculer_frequences

# ouvre le fichier en lecture
def traiter_fichier(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        texte = unidecode(f.read())


    #   Ce bout de code fait appel à ma fonction ascii_vers_base2 qui affiche l'encodage ASCCI de chaque
    #   caractère du ou des fichiers scannés par notre script
    ascii_bits = "".join(ascii_vers_base2(c) for c in texte)
    taille_initiale = len(ascii_bits)

    freqs = calculer_frequences(texte)

    # Construction de l'arbre
    h = Huffman()
    h.construire(freqs)

    # On parcourt l’arbre pour créer le code binaire de chaque caractère
    codes = h.generer_codes()

    # Afficher l'arbre
    h.afficher_arbre()

    # Permet de vérifier qu'il n'y a pas eu de perte
    texte_code = h.encoder(texte)  # prend le texte en lettres et le transforme en une suite de bits selon l’arbre Huffman
    texte_decode = h.decoder(texte_code)  # prend cette suite de bits et reconstruit le texte original


    # Permet de calculer le taux de compression
    taille_avant = len(texte) * 8 # 1 caractère = 8 bit dans la table ASCII c'est pour ça que l'on multiplie par 8
    taille_apres = len(texte_code)
    taux = taille_apres / taille_avant * 100

    print(f"\nFichier : {chemin}")
    print(f"  Taille initiale   : {taille_avant} bits")
    print(f"  Taille compressée : {taille_apres} bits")
    print(f"  Taux de compression : {taux:.1f}%")
    print("l'encodage du texte ASCII fonctionne")
    print(f"  Décodage correct  : {texte == texte_decode}")



    # Je vais éviter de laisser ça décommenter parce que ça remplit mon terminal de 0 et de 1
    # en gros, ça affiche l'encodage ASCII de chaque caractère du texte lu par notre programme
    # et vu que nous travaillons sur un dossier contenant plusieurs fichiers texte, cela remplit
    # le CMD et on ne s'y retrouve plus

    # print(ascii_bits)


# Ce bloc permet l'exécution de notre algorithme avec des vérifications
# Il vérifie qu'un dossier est bien passé en argument sinon il affiche une aide
# Il parcourt tous les fichiers du dossier et ne garde que ceux qui finissent par .txt
# Il construit ensuite le chemin complet de chaque fichier texte
# Et enfin il applique notre compression sur chaque fichier du dossier.

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python3 main.py TEST/")
        sys.exit(1)

    dossier = sys.argv[1] # en gros, ça contient ce que nous écrivons après python3 main.py pour exécuter le code
    for nom_fichier in os.listdir(dossier):
        if nom_fichier.endswith(".txt"):
            chemin = os.path.join(dossier, nom_fichier)
            traiter_fichier(chemin)
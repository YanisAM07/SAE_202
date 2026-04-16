from Huffman import Huffman

# Cette fonction renvoie le code binaire de l'encodage ASCCI d'un caractère
def ascii_vers_base2(c):
    return format(ord(c), '08b')


def compresser_fichier(source, dest_code, dest_table):

    # Lire le fichier source
    with open(source, "r", encoding="utf-8") as f:
        texte = f.read()

    # Calcul des fréquences
    freqs = {}
    for c in texte:
        freqs[c] = freqs.get(c, 0) + 1

    # Construire l'arbre de Huffman
    h = Huffman()
    h.construire(freqs)

    # Générer les codes
    codes = h.generer_codes()

    # Encoder le texte
    texte_code = h.encoder(texte)

    # Sauvegarder le texte compressé
    with open(dest_code, "w", encoding="utf-8") as f:
        f.write(texte_code)

    # Sauvegarder la table des codes
    with open(dest_table, "w", encoding="utf-8") as f:
        for caractere, code in codes.items():
            f.write(f"{repr(caractere)}:{code}\n")

    # Calcul des stats de compression
    taille_avant = len(texte) * 8          # chaque caractère = 8 bits (ASCII)
    taille_apres = len(texte_code)         # longueur de la chaîne binaire
    taux = taille_apres / taille_avant * 100 if taille_avant > 0 else 0



    print("Compression terminée")
    print(f"→ Fichier source       : {source}")
    print(f"→ Fichier compressé    : {dest_code}")
    print(f"→ Table des codes      : {dest_table}")
    print(f"→ Taille initiale      : {taille_avant} bits")
    print(f"→ Taille compressée    : {taille_apres} bits")
    print(f"→ Taux de compression  : {taux:.1f}%")

if __name__ == "__main__":
    compresser_fichier(
        "Documents/Urus.txt",
        "Urus_compresse.bin",
        "Urus_codes.txt"
    )
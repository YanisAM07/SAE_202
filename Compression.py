from Huffman import Huffman


#   Ce bout de code crée un dico vide que nous allons remplir via la boucle for ci dessous
#   la valeur représente le charactère et la clé le nombre de fois
def calculer_frequences(texte):
    freqs = {}
    for c in texte:
        freqs[c] = freqs.get(c, 0) + 1
    return freqs


# Cette fonction renvoie le code binaire de l'encodage ASCCI d'un caractère
def ascii_vers_base2(c):
    return format(ord(c), '08b') # ord transforme sont caractere en code ASCII (08b = 8bits)


def compresser_fichier(source, dest_code, dest_table):

    # Lire le fichier source
    with open(source, "r", encoding="utf-8") as f:
        texte = f.read()

    # Calculer les fréquences des caractères
    freqs = calculer_frequences(texte)

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



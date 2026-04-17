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




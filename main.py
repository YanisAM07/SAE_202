from Huffman import Huffman

def test():

    with open("TEST/testmaisahhrrr/testmaisaaaahhhrrrr/Urus.txt", "r", encoding="utf-8") as f:
        texte = f.read()

    # Étape 1 : fréquences
    freqs = {}
    for c in texte:
        freqs[c] = freqs.get(c, 0) + 1

    # Étape 2 : construire l'arbre
    h = Huffman()
    h.construire(freqs)

    # Étape 3 : générer les codes
    codes = h.generer_codes()
    print("Codes de Huffman :")
    for c, code in codes.items():
        print(f"  {repr(c)} : {code}")

    # Étape 4 : encoder
    texte_code = h.encoder(texte)
    print(f"\nTexte encodé  : {texte_code}")

    # Étape 5 : décoder (vérification)
    texte_decode = h.decoder(texte_code)
    print(f"Texte décodé  : {texte_decode}")
    print(f"Correct        : {texte == texte_decode}")

    # Taux de compression
    taille_avant = len(texte) * 8
    taille_apres = len(texte_code)
    print(f"\nTaille avant   : {taille_avant} bits")
    print(f"Taille après   : {taille_apres} bits")
    print(f"Compression    : {taille_apres / taille_avant * 100:.1f}%")

if __name__ == '__main__':
    test()
from arbre_binaire import NoeudBinaire
from Huffman import Huffman

#Premier test on créer un arbre binaire
print("Création arbre bianire")
racine = NoeudBinaire("A")
gauche = NoeudBinaire("B")
droite = NoeudBinaire("C")

racine.set_gauche(gauche)
racine.set_droit(droite)
gauche.set_gauche(NoeudBinaire("D"))
gauche.set_droit(NoeudBinaire("E"))

print(racine)


#on test ici les 4 méthodes de parcours demandées
print("Différents parcours")
# On utilise l'arbre créé au Test 1
print(f"1. Préfixe: {racine.parcours_prefixe()}")
print(f"2. Infixe: {racine.parcours_infixe()}")
print(f"3. Suffixe: {racine.parcours_suffixe()}")
print(f"4. Largeur: {racine.parcours_largeur()}")


#On crée l'abre de Huffman

from Huffman import Huffman

print("Huffman")

#On crée le message pour l'abre (lecture de fichier pas encore faite)
message = "test pour arbre Huffman"

# On calcule les fréquences des caractères
freqs = {}
for caractere in message:
    freqs[caractere] = freqs.get(caractere, 0) + 1

# On construit larbre
huff = Huffman()
huff.construire(freqs)

#On affiche l'abre
print(huff.racine)

# Sert à générer les codes
codes = huff.generer_codes()


# Test encodage et decodage
encoded = huff.encoder(message)
decoded = huff.decoder(encoded)

print(f"\nMessage original : '{message}'")
print(f"Message encodé (binaire) : {encoded}")
print(f"Message décodé : '{decoded}'")


from arbre_binaire import NoeudBinaire

a = NoeudBinaire("A")
b = NoeudBinaire("B")
c = NoeudBinaire("C")

a.set_gauche(b)
a.set_droit(c)

print(a)



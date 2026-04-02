from Noeud_Binaire import NoeudBinaire

class NoeudHuffman(NoeudBinaire):
    """
    Nœud de Huffman : valeur = tuple (s, es)
      - s  : chaine de caractères du nœud (ex: "ab")
      - es : effectif total (fréquence cumulée)
    """

    def __init__(self, valeur, gauche=None, droit=None):
        super().__init__(valeur, gauche, droit)

    @property
    def s(self):
        """Retourne la partie symbole du tuple."""
        return self.valeur[0]

    @property
    def es(self):
        """Retourne l'effectif du tuple."""
        return self.valeur[1]

    def est_feuille(self):
        """Feuille = pas d'enfants (valeur est toujours un tuple donc jamais None)."""
        return self.gauche is None and self.droit is None
# NoeudHuffman va hériter de toutes ses méthodes (parcours, hauteur, etc.)
# et on va juste adapter ce qui est spécifique à Huffman.
from Noeud_Binaire import NoeudBinaire

class NoeudHuffman(NoeudBinaire):
    """
    Nœud de Huffman : valeur = tuple (s, es)
      - s  : chaine de caractères du nœud (ex: "ab")
      - es : effectif total (fréquence cumulée)
    """

    def __init__(self, valeur, gauche=None, droit=None):
        super().__init__(valeur, gauche, droit)

    # @property permet d'accéder à noeud.s comme si c'était un attribut direct
    # au lieu de devoir écrire noeud.valeur[0] partout dans le code.
    # noeud.s retourne donc le symbole (le ou les caractères) stocké dans le tuple.
    # Exemple : si valeur = ("a", 5), alors noeud.s retourne "a"
    @property
    def s(self):
        """Retourne la partie symbole du tuple."""
        return self.valeur[0]

    # Même principe que s mais pour la fréquence.
    # noeud.es retourne l'effectif (la fréquence) stocké dans le tuple.
    # Exemple : si valeur = ("a", 5), alors noeud.es retourne 5
    @property
    def es(self):
        """Retourne l'effectif du tuple."""
        return self.valeur[1]

    # On redéfinit est_feuille() par rapport à celle de NoeudBinaire.
    # en gros NoeudBinaire et est_feuille vérifie que valeur is not None ET que les enfants sont None.
    # (cela nous sert de condition d'arret lors du processus de creation de l'arbre)
    # Ici ce n'est pas possible : valeur est TOUJOURS un tuple, donc jamais None,
    # On se base donc uniquement sur l'absence d'enfants pour déterminer si c'est une feuille :
    #   - si gauche et droit sont None alors c'est une feuille (un caractère unique)
    #   - sinon  c'est un oeud interne (résultat d'une fusion de deux sous-arbres)
    def est_feuille(self):
        """Feuille = pas d'enfants (valeur est toujours un tuple donc jamais None)."""
        return self.gauche is None and self.droit is None
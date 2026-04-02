from noeud_Huffman import NoeudHuffman

class Huffman:
    def __init__(self):
        self.racine = None
        self.codes = {}

    def construire(self, freqs):
        """
        Construit l'arbre de Huffman à partir d'un dictionnaire {caractere: frequence}.
        Chaque feuille stocke (caractere, frequence) comme tuple (s, es).
        """
        # Créer une feuille NoeudHuffman par caractère
        liste = []
        for caractere, f in freqs.items():
            noeud = NoeudHuffman(valeur=(caractere, f))
            liste.append([f, noeud])

        # Fusionner les deux nœuds de plus faible fréquence jusqu'à n'en avoir qu'un
        while len(liste) > 1:
            liste.sort(key=lambda x: x[0])

            freq1, n1 = liste.pop(0)
            freq2, n2 = liste.pop(0)

            # Le nouveau nœud interne concatène les symboles et additionne les effectifs
            s_combine = n1.s + n2.s
            es_combine = freq1 + freq2
            nouveau = NoeudHuffman(
                valeur=(s_combine, es_combine),
                gauche=n1,
                droit=n2
            )
            liste.append([es_combine, nouveau])

        self.racine = liste[0][1]

    def generer_codes(self):
        """
        Parcourt l'arbre et génère le dictionnaire {caractere: code_binaire}.
        Gauche = '0', Droite = '1'.
        """
        self.codes = {}

        def parcours(noeud, code):
            if noeud is None:
                return
            if noeud.est_feuille():
                self.codes[noeud.s] = code  # noeud.s = le caractère
                return
            parcours(noeud.get_gauche(), code + "0")
            parcours(noeud.get_droit(),  code + "1")

        parcours(self.racine, "")
        return self.codes

    def encoder(self, texte):
        """Encode le texte avec les codes de Huffman générés."""
        res = ""
        for c in texte:
            res += self.codes[c]
        return res

    def decoder(self, binaire):
        """Décode une chaîne binaire en remontant l'arbre."""
        res = ""
        noeud = self.racine
        for bit in binaire:
            noeud = noeud.get_gauche() if bit == "0" else noeud.get_droit()
            if noeud.est_feuille():
                res += noeud.s  # noeud.s = le caractère stocké dans le tuple
                noeud = self.racine
        return res
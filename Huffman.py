from noeud_Huffman import NoeudHuffman

class Huffman:
    def __init__(self):
        self.racine = None
        self.codes = {}

    def construire(self, freqs):
        """
        Construit l'arbre de Huffman à partir d'un dictionnaire {caractere: frequence}.
        Cette fonction transforme les fréquences en un arbre binaire optimal pour la compression.

        Fonctionnement :
        - On crée d'abord une feuille pour chaque caractère avec sa fréquence.
        - On fusionne ensuite les deux noeuds les moins fréquents pour créer un noeud interne.
        - Ce nouveau noeud contient la somme des fréquences et devient le parent des deux noeuds fusionnés.
        - On répète cette opération jusqu'à ce qu'il ne reste plus qu'un seul noeud : la racine de l'arbre.

        L'idée est que les caractères fréquents se retrouvent proches de la racine (codes courts),
        et les caractères rares plus loin (codes longs), ce qui permet une compression + efficace.
        """

        # Créer une feuille NoeudHuffman par caractère
        liste = []
        for caractere, f in freqs.items():
            noeud = NoeudHuffman(valeur=(caractere, f))
            liste.append([f, noeud])

        # Fusionner les deux noeuds de plus faible fréquence jusqu'à n'en avoir qu'un
        while len(liste) > 1:
            liste.sort(key=lambda x: x[0])

            freq1, n1 = liste.pop(0)
            freq2, n2 = liste.pop(0)

            # Le nouveau noeud interne concatène les symboles et additionne les effectifs
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

        # chaîne vide qui contiendra le txt encodé en binaire (Chaque caractère du texte sera remplacé par son code Huffman)
        res = ""

        # Parcourt chaque caractère du texte original
        # Pour chaque caractère, on récupère son code binaire dans le dictionnaire self.codes
        # et on l'ajoute à la chaîne résultat
        for c in texte:
            res += self.codes[c]

        # Renvoie la chaîne complète de bits représentant le texte compressé
        return res

    def decoder(self, binaire):
        """Décode une chaîne binaire en remontant l'arbre"""

        # Initialise une chaîne vide pour reconstruire le texte original
        res = ""

        # On commence le décodage depuis la racine de l'arbre Huffman
        noeud = self.racine

        # Parcourt chaque bit de la chaîne binaire
        # Chaque bit indique dans quelle direction descendre dans l'arbre : 0 = branche gauche et 1 = branche droite
        for bit in binaire:
            noeud = noeud.get_gauche() if bit == "0" else noeud.get_droit()

            # Si on arrive sur une feuille, cela signifie qu'on a retrouvé un caractère complet
            # On l'ajoute au texte décodé.
            if noeud.est_feuille():
                res += noeud.s  # noeud.s = le caractère stocké dans la feuille

                # On revient à la racine pour décoder le prochain caractère.
                noeud = self.racine

        return res

    def afficher_arbre(self, noeud=None, prefixe="", est_racine=True, direction="", code_courant="" ):
        """
        Affiche l'arbre de Huffman avec les branches gauche donc 0 et droite donc 1 ainsi que le code
         binaire sur chaque feuille.
         on aura donc le caractère suivie de la fréquence et de son code binaire
        Appel : h.afficher_arbre()
        """


        # Détermine d’où on commence l’affichage de l’arbre et évite de descendre dans des branches qui n’existent pas.
        # Si noeud est None et qu’on est à la racine alors on démarre depuis la racine.
        # Si noeud est None et qu’on n’est pas à la racine alors on arrête la récursion pour cette branche.
        if noeud is None:
            if est_racine:
                noeud = self.racine
            else:
                return

        # Ajoute le bit correspondant au chemin parcouru dans l'arbre.
        # Si on arrive depuis la branche gauche, on ajoute un 0 au code.
        # Si on arrive depuis la branche droite, on ajoute un 1 au code.
        if direction == "gauche":
            code_courant += "0"
        elif direction == "droit":
            code_courant += "1"

        # Détermine ce qu’on doit afficher pour ce noeud.
        # Si c’est une feuille  on affiche le caractère sa fréquence et son code binaire complet.
        # Sinon  on affiche simplement la fréquence du noeud.
        if noeud.est_feuille():
            label = f"['{noeud.s}' : {noeud.es}]  →  {code_courant}"
        else:
            label = f"({noeud.es})"

        # Affiche visuellement la ligne correspondant au nœud.
        # Si on est à la racine : on l’indique clairement.
        # Sinon : on affiche une flèche 0──> ou 1──> selon la direction empruntée,
        #         avec le préfixe qui permet de dessiner correctement la structure de l’arbre.
        if est_racine:
            print(f"RACINE {label}")
        else:
            fleche = "0──>" if direction == "gauche" else "1──>"
            print(f"{prefixe}{fleche} {label}")

        # Descend récursivement dans l’arbre si le nœud n’est pas une feuille.
        # On prépare un nouveau préfixe pour garder l’alignement visuel de l’arbre.
        # Puis on explore d’abord la branche gauche si elle existe, puis la droite.
        # À chaque appel récursif, le code binaire continue de se construire.
        if not noeud.est_feuille():
            nouveau_prefixe = prefixe + ("    " if direction == "droit" else "|   ")
            if noeud.get_gauche():
                self.afficher_arbre(noeud.get_gauche(), nouveau_prefixe, False, "gauche", code_courant)
            if noeud.get_droit():
                self.afficher_arbre(noeud.get_droit(), nouveau_prefixe, False, "droit", code_courant)
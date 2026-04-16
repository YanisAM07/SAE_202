# NoeudBinaire est la brique de base de tout notre projet.
# C'est une classe générique qui modélise un nœud d'arbre binaire classique.
# Elle ne sait rien de Huffman, elle peut servir pour n'importe quel arbre binaire.
# NoeudHuffman en héritera et l'adaptera à nos besoins.
class NoeudBinaire:

    # Chaque nœud possède trois attributs :
    #   - valeur : la donnée stockée dans ce nœud (None = nœud vide)
    #   - gauche : le fils gauche, lui-même un NoeudBinaire (ou None si absent)
    #   - droit  : le fils droit,  lui-même un NoeudBinaire (ou None si absent)
    # Les valeurs par défaut à None permettent de créer un nœud vide simplement
    # avec NoeudBinaire() sans arguments.
    def __init__(self, valeur=None, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit  = droit


    # ─── Getters : lire les données du nœud ───────────────────────────────────

    # Retourne la valeur stockée dans ce nœud.
    def get_valeur(self):
        return self.valeur

    # Retourne le fils gauche de ce nœud (peut être None).
    def get_gauche(self):
        return self.gauche

    # Retourne le fils droit de ce nœud (peut être None).
    def get_droit(self):
        return self.droit


    # ─── Setters : modifier les données du nœud ───────────────────────────────

    # Modifie la valeur stockée dans ce nœud.
    def set_valeur(self, v):
        self.valeur = v

    # Attache un nouveau fils gauche à ce nœud.
    def set_gauche(self, g):
        self.gauche = g

    # Attache un nouveau fils droit à ce nœud.
    def set_droit(self, d):
        self.droit = d


    # ─── État du nœud ─────────────────────────────────────────────────────────

    # Un nœud est considéré vide si les trois attributs sont à None.
    # Cela correspond à un arbre complètement inexistant.
    def est_vide(self):
        return self.valeur is None and self.gauche is None and self.droit is None

    # Un nœud est une feuille s'il a une valeur mais aucun enfant.
    # Dans un arbre de Huffman, les feuilles représentent les caractères individuels.
    def est_feuille(self):
        return self.valeur is not None and self.gauche is None and self.droit is None

    # Retourne True si ce nœud possède un fils gauche.
    # Utilisé dans les parcours pour savoir si on peut descendre à gauche.
    def a_gauche(self):
        return self.gauche is not None

    # Retourne True si ce nœud possède un fils droit.
    def a_droit(self):
        return self.droit is not None

    # Calcule la hauteur de l'arbre enraciné à ce nœud.
    # La hauteur = nombre de niveaux - 1 (une feuille seule a une hauteur de 0).
    # On descend récursivement des deux côtés et on garde le chemin le plus long,
    # auquel on ajoute 1 pour compter le nœud actuel.
    def hauteur(self):
        # Condition d'arrêt : un nœud vide ou une feuille n'a pas de profondeur à ajouter.
        if self.est_vide() or self.est_feuille():
            return 0

        h_gauche = self.gauche.hauteur() if self.a_gauche() else 0
        h_droit  = self.droit.hauteur()  if self.a_droit()  else 0

        # On prend le chemin le plus long et on ajoute 1 pour le nœud courant.
        return 1 + max(h_gauche, h_droit)


    # ─── Parcours de l'arbre ──────────────────────────────────────────────────

    # Parcours PRÉFIXE : on lit le nœud courant AVANT ses enfants.
    # Ordre : racine → gauche → droite
    # Exemple sur [A, B, C] : A, B, C
    def parcours_prefixe(self):
        if self.est_vide():
            return []

        # On commence par ajouter la valeur du nœud courant
        res = [self.valeur]
        # Puis on descend à gauche
        if self.a_gauche():
            res += self.gauche.parcours_prefixe()
        # Puis à droite
        if self.a_droit():
            res += self.droit.parcours_prefixe()
        return res

    # Parcours SUFFIXE : on lit le nœud courant APRÈS ses enfants.
    # Ordre : gauche → droite → racine
    # Utile pour supprimer un arbre ou calculer la taille.
    def parcours_suffixe(self):
        if self.est_vide():
            return []

        res = []
        # On descend d'abord entièrement à gauche
        if self.a_gauche():
            res += self.gauche.parcours_suffixe()
        # Puis à droite
        if self.a_droit():
            res += self.droit.parcours_suffixe()
        # Et on ajoute la racine en dernier
        res.append(self.valeur)
        return res

    # Parcours INFIXE : on lit le nœud courant ENTRE ses deux enfants.
    # Ordre : gauche puis racine puis droite
    # Sur un arbre binaire de recherche, cela donne les valeurs triées dans l'ordre croissant.
    def parcours_infixe(self):
        if self.est_vide():
            return []

        res = []
        if self.a_gauche(): res += self.gauche.parcours_infixe()
        res.append(self.valeur)
        if self.a_droit():  res += self.droit.parcours_infixe()
        return res

    # Parcours en LARGEUR (BFS  Breadth First Search) : on lit niveau par niveau,
    # de gauche à droite, en commençant par la racine.
    # On utilise une file (liste Python) : on enfile les enfants au fur et à mesure
    # qu'on défile les parents. Principe FIFO (premier entré, premier sorti).
    def parcours_largeur(self):
        if self.est_vide():
            return []

        # On initialise la file avec le nœud racine
        file = [self]
        res  = []


        #Le script regarde si le noeud node a quelque chose dans son à gauche ou à droit.
        #Si oui, ces boîtes sont envoyées dans file.
        #Ensuite, node met seulement ce qu’il y a écrit sur la boîte dans res.
        #node sert un peu de filtre : il évite de mettre du vide dans la file.
        while file:
            node = file.pop(0) # pop(0) pour prendre le premier element d'une liste donc de la file
            res.append(node.valeur)

            if node.a_gauche():
                file.append(node.gauche)
            if node.a_droit():
                file.append(node.droit)

        return res
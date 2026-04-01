class NoeudBinaire:
    def __init__(self, valeur=None, gauche=None, droit=None):
        # On crée un nœud avec une valeur et potentiellement deux enfants
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

    # pour lire et modifier les données

    #ici on récupére la valeur
    def get_valeur(self):
        return self.valeur  
    def get_gauche(self):
        return self.gauche
    def get_droit(self):
        return self.droit
    
    #ici on lui attribu une valeur
    def set_valeur(self, v):
        self.valeur = v 
    def set_gauche(self, g):
        self.gauche = g
    def set_droit(self, d): 
        self.droit = d

    # Pour savoir ou on en est dans l'arbre
    def est_vide(self):
        # L'arbre est vide si tout est à None
        return self.valeur is None and self.gauche is None and self.droite is None

    def est_feuille(self):
        # C'est une feuille s'il n'y a pas d'enfants à gauche et à droite
        return self.valeur is not None and self.gauche is None and self.droit is None
    
    def a_gauche(self): 
        return self.gauche is not None #retourne TRUE ou FALSE, si False alors l,'affichage de l'arbre s'arretera
    def a_droit(self): 
        return self.droit is not None

    def hauteur(self):
        # On calcule la profondeur de l'arbre en allant jusqu'au bout
        if self.est_vide() or self.est_feuille():
            return 0 #condition d'arret 
        
        h_gauche = self.gauche.hauteur() if self.a_gauche() else 0
        h_droit = self.droit.hauteur() if self.a_droit() else 0
        # On prend le chemin le plus long et on ajoute 1 (le nœud actuel)
        return 1 + max(h_gauche,h_droit)    
    

    #On implémente 
    #on commence par préfixe, le but est de faire sur les branches de gauche puis de droite
    def parcours_prefixe(self):
        if self.est_vide(): #condition d'arrêt
            return []

        res = [self.valeur] #on commence la liste par la valeur dunoeud
        if self.a_gauche(): 
            res += self.gauche.parcours_prefixe()
        if self.a_droit():
            res += self.droit.parcours_prefixe()
        return res

    #parcour suffixe, ici on commence par les enfants gauche puis ceux de droite et on fini par la racine pricipale
    def parcours_suffixe(self):
        if self.est_vide(): 
            return []
        res = []

        if self.a_gauche(): 
            res += self.gauche.parcours_suffixe()
        if self.a_droit(): 
            res += self.droit.parcours_suffixe()
        res.append(self.valeur)
        return res
    

   #Parcour infixe, le but est de faire le sous arbre gauche puis la racine et le sous arbre droit
    def parcours_infixe(self):
        if self.est_vide(): 
            return []#condition d'arret
        
        res = []
        if self.a_gauche(): res += self.gauche.parcours_infixe()
        res.append(self.valeur)
        if self.a_droit(): res += self.droit.parcours_infixe()
        return res
    

    #parcour largeur, le but est de commencer par la racine puis de descendre étage par étage en commencant par la gauche
    def parcours_largeur(self):
        if self.est_vide():
            return []
        
        file = [self] # On utilise une liste comme une file d'attente, principe FILE
        res = []

        while file:
            node = file.pop(0)
            res.append(node.valeur)
            if node.a_gauche():
                file.append(node.gauche)
            if node.a_droit(): 
                file.append(node.droit)
        return res

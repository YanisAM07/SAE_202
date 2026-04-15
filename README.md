README SAE 2.02 Exploration algorithmique d'un problème 

Ce projet implémente l'algorithme de compréssion de Huffman en Python 
L'objectif est de compresser des fichiers texte en attribuant un encdage binaire aux caractères: plus un caractère est réccurent plus son code est court.

Ce programme permet de :
-Lire des fichiers .txt depuis un répertoir et de le normaliser (via 'unicode')
-Construire un arbre de Huffman pour chaque fichier 
-Compresser le texte et calculer le gain d'espace par rapport à l'encodage classique 
-vérifier l'intégrité des donnée par décompression

Structure du projet:
Ce projet possède 5 fichiers:
-main.py qui permet de lancer le programme et traiter les fichiers voulus 
-Noeud_binaire.py est la classe gérant les arbres bianires, elle inclut les méthodes de calcul de hauteur, l'affichage des arbres binaires classiques et les quatres types de parcours:
    -Parcours préfixe
    -Parcours suffixe 
    -Parcours infixe
    -Parcours en largeur
-Noeud_Huffman.py classe héritant de noeud_binaire.py qui manipulent les valeurs sous forme de tuples.
-Compression.py Programme qui permet de compresser un fichier


Pour utiliser ce projet il est nécéssaire d'installer au péalable le module 'unicode' pour la gestion des caractère spéciaux, la formule pour cela est:

    pip install unicode

Une fois le projet finalisé et téléchargé, pour utiliser ce projet il faut suivre ces étapes:
-Faire Windows+r et taper cmd puis validez.
-Une fois dans le terminal on se place dans l'arborescence du projet 
-Puis on tape la commande suivante (mettre
le nom du fichier voulu):
    'python main.py 'Nom-fichier'/'

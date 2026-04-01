import sys
import os
import unidecode

class Huffman:
    def __init__(huff, char = None, freq = 0, gauche = None, droite = None,max = None, path = None, test = None):
        huff.char = char
        huff.freq = freq # ou compteur
        huff.gauche = gauche
        huff.droite = droite
        huff.max = max
        huff.path = path
        huff.test = test

    def __str__(huff):
        return f"Huffman(char={huff.char}, freq={huff.freq}, gauche={huff.gauche}, droite={huff.droite})"


    #def repertoire (huff, path) :
    #    with open (path)

    #def compteur (huff):
    #   for i in range (max):

    #def feuilles(huff):
    #    if huff.gauche == None & huff.droite == None:
    #        print("Nous sommes sur une feuille")











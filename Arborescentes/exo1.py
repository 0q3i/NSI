from noeud import *


def affiche(a,n=0):
    e = str(a.valeur)
    for elm in a.fils:
        e+="\n"+" "*(n) + affiche(elm, n+1) 
    return e

#jeu de test
a = a = Noeud("A", [
    Noeud("B", [
        Noeud("D", [])
    ]),
    Noeud("C", [
        Noeud("E", []),
        Noeud("F", [
            Noeud("H", [])
        ]),
        Noeud("G", [])
    ])
])

print(affiche(a))
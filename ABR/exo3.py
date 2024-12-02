from noeud import *

#1
#tout a gauche est ou ce trouve le plus petit element d'un arbre abr

#2
def minimum(a):
    if a.gauche is None:
        return a.valeur
    else:
        return minimum(a.gauche)

#jeu de test
a = Noeud(Noeud(Noeud(None,0,None),1,None),2,None)

assert minimum(a) == 0

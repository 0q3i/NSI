from noeud import *

def str_arbre(a):
    if a is None:
        return ""
    else:
        g=str_arbre(a.gauche)
        d=str_arbre(a.droit)
        return "("+str(g)+str(a.valeur)+str(d)+")"
    
#jeu de test
a = Noeud(Noeud(None,"B",Noeud(None,"C",None)),"A",Noeud(None,"D",None))

#arbre exo5
b = Noeud(None,1,Noeud(Noeud(None,2,None),3,None))


assert str_arbre(a) == "((B(C))A(D))"
assert str_arbre(b) == "(1((2)3))"
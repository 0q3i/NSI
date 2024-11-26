from noeud import *

def parfait(h):
    if h==1:
        return Noeud(None,None,None)
    else:
        return Noeud(parfait(h-1),None,parfait(h-1))
    
#jeu de test

assert parfait(2) == Noeud(Noeud(None,None,None),None,Noeud(None,None,None))
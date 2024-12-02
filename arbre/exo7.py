from noeud import *
from math import *

def parfait(h,n=1):
    if h==1:
        return Noeud(None,n,None)
    else:
        return Noeud(parfait(h-1,n+1),n,parfait(h-1,n+1))
    
#jeu de test

assert parfait(2) == Noeud(Noeud(None,2,None),1,Noeud(None,2,None))
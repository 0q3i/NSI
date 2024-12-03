from cellul import *

def concatener_inverser(l1,l2):
     if l1 is None:
          return l2
     else:
          return concatener_inverser(l1.suivante,Cellule(l1.valeur,l2))
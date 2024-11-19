from exo7 import *

def tri_par_incertion(lst):
    inserer(lst.valeur,lst.suivante)
    if lst is None:
        return None
    else:
        inserer(lst.valeur,lst.suivante)
        return tri_par_incertion(lst.suivante)


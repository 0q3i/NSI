from cellul import *
def inserer(x,lst):
    if lst is None:
        return Cellule(x,lst)
    elif x > lst.valeur:
        return inserer(x,lst.suivante)
    elif x < lst.valeur:
        return Cellule(x,lst)
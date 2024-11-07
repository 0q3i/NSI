from random import randint 

class Cellule:
    def __init__(self,v,s):
        self.valeur = v
        self.suivante = s


def nieme_elm(n,lst):
    while n >0:
        n-=1
        lst = lst.suivante
        if lst is None:
            return None
    return lst
from noeud import *
from exo3 import *
from random import *

def appartient(x, a):
    if a is None:
        return False
    elif x < a.valeur:
        return appartient(x, a.gauche)
    elif x > a.valeur:
        return appartient(x, a.droit)
    else:
        return True
    
#exo5
def remplir(a , t):
    if a is None:
        return 
    else:
        remplir(a.gauche,t)
        t.append(a.valeur)
        remplir(a.droit,t)

def ajoute(x, a):
    #exo4
    if a is None:
        return Noeud(None,x,None)
    elif x < a.valeur:
        return Noeud(ajoute(x, a.gauche),a.valeur, a.droit)
    elif x > a.valeur:
        return Noeud(a.gauche,a.valeur,ajoute(x, a.droit)) 
    else:
        return a

def suprime_minimum(a):
    assert a is not None
    if a.gauche is None:
        return a.droit
    else:
        return Noeud(suprime_minimum(a.gauche), a.valeur, a.droit)

#exo3 - 3

def supp(a, x):
    if a is None:
        return None
    elif x > a.valeur:
        return Noeud(a.gauche, a.valeur ,supp(a.droit, x))
    elif x < a.valeur:
        return Noeud(supp(a.gauche, x),a.valeur, a.droit)
    elif a.droit is None:
        return a.gauche
    else:
        return Noeud(a.gauche,minimum(a.droit),suprime_minimum(a.droit))



#exo6

#1
def trier(t):
    abr = ABR()
    melange(t)#modification pour le 3
    for elm in t:
        abr.ajoute(elm)
    return abr.lister()
#complexite lineaire

#2
def melange(t):
    for i in range(len(t)):
        i_random = randint(0,i)
        t[i],t[i_random] = t[i_random], t[i]
#compexite linaire    



class ABR:
    def __init__(self):
        self.racine = None

    def __contains__(self, x):
        return appartient(x, self.racine)
    
    def ajoute(self, x):
        self.racine = ajoute(x, self.racine)

    def supp(self, x):
        return supp(self.racine, x)
    
    def lister(self):
        t = []
        remplir(self.racine, t)
        return t 
    
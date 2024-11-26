class Noeud:

    def __init__(self,g,v,d):
        self.gauche = g
        self.valeur = v
        self.droit = d
        
    def parcour_infixe(self):
        if self is None:
            return ""
        else:
            g = self.gauche.parcour_infixe()
            d = self.droit.parcour_infixe()
            return g+str(self.valeur)+d
        
    #exo6 
        
    def __eq__(self, a2):
        if self is None and a2 is None:
            return True
        else:
            return (
            (self.valeur == a2.valeur) and
            (self.gauche == a2.gauche if self.gauche or a2.gauche else self.gauche == a2.gauche) and
            (self.droit == a2.droit if self.droit or a2.droit else self.droit == a2.droit)
        )
        
#jeu de test 

a1 = Noeud(None,"rien tkt",Noeud(None,"rien tkt",None))
a2 = Noeud(None,"rien tkt",Noeud(None,"rien tkt",None))

assert a1 == a1 
assert a1 == a2 

a2 = Noeud(Noeud(None,"rien tkt",None),"rien tkt",Noeud(None,"rien tkt",None))

assert a1 == a2 
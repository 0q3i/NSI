from pile import *

class Pilebornee:
    def __init__(self,capacite):
        self.tab = [None for i in range(capacite)] 
        self.nb_elm = 0

    def est_vide(self):
        return self.nb_elm == 0
    
    def est_pleine(self):
        return self.nb_elm == len(self.tab)
    
    def empiler(self,e):
        if not self.est_pleine():
            self.nb_elm+=1
            for i in range(self.nb_elm):
                stocker = self.tab[i]
                self.tab[i+1] = stocker
            self.tab[0]=e
        else:
            raise IndexError
    
    def depiler(self):
        elm = self.tab[0]
        for i in range(self.nb_elm):
            stocker = self.tab[i+1]
            self.tab[i] =self.tab[i+1]
        return elm 
    
# Jeu de test

pb = Pilebornee(5)

assert pb.est_vide() == True
for i in range(4):
    pb.empiler(i)
assert pb.est_pleine() == False










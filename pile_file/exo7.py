class Filemax:
    
    def __init__(self,c):
        self.tab = [None for _ in range(c)]
        self.nb_elm = 0 
        self.indicePrem = 0
        
    def est_vide(self):
        if self.nb_elm == 0:
            return True
        return False 
    
    def est_peleine(self):
        if self.nb_elm == len(self.tab):
            return True
        return False
    
    def ajouter(self, e):
        if self.est_peleine():
            raise IndexError
        elif self.est_vide():
            self.tab[self.indicePrem]=e

        else:
            for i in range(self.nb_elm):
                if not i == self.nb_elm:
                    stoker = self.tab[i+1]
                    self.tab[i] = stoker
        self.indicePrem+=1   
            
    def retirer(self):
        if self.est_vide():
            raise IndexError
        elm = self.tab[self.indicePrem]
        for i in range(self.nb_elm):
            if not i == self.nb_elm:
                stoker = self.tab[i]
                self.tab[i+1] = stoker
        return elm
    
    
#jeu de test 
fm = Filemax(5)
assert fm.est_vide() == True
for i in range(5):
    fm.ajoute(i)
assert fm.est_peleine == True
fm.retirer
assert fm.est_peleine == False


    
    
    
        
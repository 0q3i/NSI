class Cellul:

    def __init__(self,v,id):
        self.valeur = v
        self.suivante = id

class Pile:

    def __init__(self):
        self._contenu = None
    def est_vide(self):
        return self._contenu is None
    def empiler(self, e):
        self._contenu = Cellul(e, self._contenu)
    def depiler(self):
        if self.est_vide():
            raise IndexError
        v = self._contenu.valeur
        self._contenu = self._contenu.suivante
        return v 
    
    
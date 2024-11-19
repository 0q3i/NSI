import pile as p

class Historique:
    
    def __init__(self):
        self.adresse_courante = None
        self._adresse_precendentes = p.creer_pile()
class Chrono:
    """une classe pour representer un temps mesure en heure
    , minute et secondes"""
    heure_max = 24

    def __init__(self,h,m,s):
        self._temps = 3600*h + 60*m + s

    def avancer(self, s):
        self._temps += s

    def _convertion(self):
        s = self._temps
        return (s//3600,(s//60)%60, s%60)

    def __str__(self):
        h, m, s = self._convertion()
        return (str(h) + "h " + str(m) + "m" + str(s) + "s")
    
    def clone(self,h, m, s):
        u = Chrono(h, m, s)
        return u
    
    def __eq__(self, u):
        if self.h == u and self.m == u and self.s == u:
            return True
        return False

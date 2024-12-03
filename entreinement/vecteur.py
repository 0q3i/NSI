from math import *

class Vecteur:
    
    def __init__(self,x,y):
        self._x=x
        self._y=y
        
    def norme(self):
        return sqrt(self._x**2+self._y**2)
    
    
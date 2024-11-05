class Intervalle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def est_vide(self):
        return self.b < self.a
    def __len__(self):
        if not self.est_vide():
            return self.b-self.a
        else:
            return 0 
    def __contians__(self,x):
        return x >= self.a and x <= self.b
    def __eq__(self,I2):
        return I2.est_vide() and self.est_vide() or I2.a == self.a and I2.b==self.b
    def __le__(self,I2):
        return self.a >= I2.a and self.b <= I2.b or I2.est_vide() and self.est_vide()
    def intercetion(self,I2):
        if self.b >= I2.a:
            return Intervalle(I2.a,self.b)
        elif self.a >= I2.a:
            return Intervalle(I2.a, self.a)
        elif self==I2:
            return Intervalle(self.a,self.b)
        elif I2.est_vide() and self.est_vide():
            return Intervalle(0,-1)
        else:
            return False
    def union(self, I2):
        if not I2.est_vide() and self.est_vide():
            return Intervalle(min(self.a,I2.a),max(self.b,I2.b))
        return Intervalle(1,0)


  
def pgcd(a, b):
    if b ==  0:
        return a
    else:
        return pgcd(b,a %b)


class Fraction:

    def __init__(self, num, denom):
        self.num = num 
        self.denom = denom 
        self.format = num / denom
        n = self.denom 
        if n <= 0:
            raise ValueError

        
    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        else:
            num = str(self.num)
            denom = str(self.denom)
            return num + "/"+ denom 
        
    def __eq__(self, fac2):
        if fac2.num*self.denom == self.num*fac2.denom:
            return True
        else:
            return False 
        
    def __lt__(self, fac2):
        if fac2.num*self.denom > self.num*fac2.denom:
            return True
        else:
            return False
        
    def __add__(self, fac2):
        return Fraction(self.num * fac2.denom + self.denom * self.num , self.denom * fac2.denom)
    
    def __mul__(self,fac2):
        return Fraction(self.num*fac2.num, self.denom*fac2.denom)
    
    def irreductible(self):
        if self.num < self.denom:
            return Fraction(self.num // pgcd(self.denom , self.num), self.denom //pgcd(self.denom,self.num))
        else:
            return Fraction(self.num // pgcd(self.num, self.denom), self.denom // pgcd(self.num, self.denom))

#jeu de test
f1 = Fraction(1,3)
f2 = Fraction(1,9)
f3 = Fraction(9,27)

assert f1.__str__() == "1/3"
assert f1.__eq__(f2) == False
assert f1.__lt__(f2) == False
assert f1.__add__(f2) == Fraction(12, 27)
assert f1.__mul__(f2) == Fraction(1,27)
assert f3.irreductible() == Fraction(1,3)
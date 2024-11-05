class DbTab:
    def __init__(self, g, d):
        g = g[::-1]
        self.d = d
        self.g = g
        self.lenG = len(g)
        self.lenD = len(d)

    def imin(self):
        return -len(self.lenG)
    
    def imax(self):
        return len(self.lenD)
    
    def append(self,elm):
        self.d.append(elm)

    
    def prepend(self, elm):
        self.g.reverse()
        self.g.append(elm)
        self.g.reverse()

    def __getitem__(self,i):
        if i < 0:
            self.g[abs(i)-1][::-1]
        else:
            self.d[i]

    def __setitem__(self, elm , i):
        if i < 0:
            self.g[abs(i)-1] = elm
        else:
            self.d[i] = elm 

    def __str__(self):
        tab = self.g + self.d
        return str(tab)
        

d = [0,1,2]
g = [-1,-2]

a = DbTab(g,d)

print(str(a))





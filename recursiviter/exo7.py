import mudulate as mt

def tranche(tab,i,j):
    """Renvois un nouveau tableau avec les element de i inclu a j exclu,
    si j<= i alors ca revois un tbleau vide"""
    if j <= i:
        return []
    else:
        return [tab[k] for k in range(i,j)]
    
# méthode 1
def concatenation(t1,t2):
    return mt.union(t1,t2)
# méthode 2
def concatenation(t1,t2):
    t3 = t1
    for elm in range(t2):
        t3.append(elm)
    return t3
def cree():
    return [0]*6

def contient(s,x):
    iEntier = x//64
    bit = x % 64 
    return (s[iEntier] & (1<<bit) !=0)

def ajoute(s,x):
    iEntier = x // 64
    bit = x //  64
    s[iEntier] = s[iEntier] | 1<<bit

def enumere(s):
    lst_s = []
    for elm in s:
        if bin(elm) in s:
            lst_s.append(elm)
    return lst_s


def union(E,F):
    """Renvois l'union entre E et F"""
    A = E
    for elm in F:
        if elm not in A:
            A.append(elm)
    return A


def intersection(E,F):
    """Renvois l'intersecion de E et F"""
    A = []
    for elmE in E:
        if elmE in F and elmE not in A:
            A.append(elmE)
    return A



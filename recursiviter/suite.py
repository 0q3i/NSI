def suite(n,a,b):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return 3*suite(n-1,a,b) + 2*suite(n-2,a,b)+5
    

def boucle(i,k):
    x = k-i
    print(x)
    if k-i <= 0: 
        return "ouhhlalal coco"
    else:
        return boucle(i+1,k)
    
def pgcd(a, b):
    if b ==  0:
        return a
    else:
        return pgcd(b,a %b)
    

def nbchiffres(n):
    i = 1
    if n <10:
        return i
    return nbchiffres(n/10)
    

def coef(n,p):
    if n == 0 or p == 0:
        return 1
    else: 
        return coef(n-1,p-1)+coef(n-1,p)
    

print(coef(4,2))

    
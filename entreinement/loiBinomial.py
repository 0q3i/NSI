def factorielle(n):
    if n == 0:
        return 1 
    else:
        return factorielle(n-1)*n

def coef(k,n):
    num = factorielle(n)
    denom = factorielle(k)*factorielle(n-k)
    return (num//denom)

def Binomial_inferieur(k,n,p):
    if k == 0:
        return coef(0,n)*(1-p)**n
    else:
        return Binomial_inferieur(k-1,n,p) + coef(k,n)*p**k*(1-p)**(n-k)
    
def Binomial_superieure(k,n,p):
    if k == n:
        return coef(k,n)*p**k*(1-p)**(n-k)
    else:
        return Binomial_superieure(k+1,n,p) + coef(k,n)*p**k*(1-p)**(n-k)
    
def Binomial_intervale(k,b,n,p):
    if k == b:
        return coef(k,n)*p**k*(1-p)**(n-k)
    else: 
        return Binomial_intervale(k+1,b,n,p) + coef(k,n)*p**k*(1-p)**(n-k)
    
    
#jeu de test 

assert factorielle(5) == 120 
assert coef(2,4) == 6
assert Binomial_inferieur(2,3,0.75) >= 0.57
assert Binomial_superieure(2,3,0.75) >= 0.84
assert Binomial_intervale(1,3,3,0.75) >=0,98

def remplir(a , t):
    if a is None:
        return 
    else:
        g = remplir(a.gauche,t)
        d = remplir(a.droit,t)
# pass fini
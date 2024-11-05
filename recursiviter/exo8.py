def cree():
    """cree un dictionnaire vide"""
    return {}

def key(d,k):
    """regarde si la cle k est dans le dictionnaire d"""
    if d[k] in d:
        return True
    return False
    
def lit(d,k):
    """Renvois la valeur de k dans d ssi k est dans d"""
    if not key(d,k):
        return False 
    else: 
        return d[k]
    
def ecrit(d,k,v):
    d[k] = v


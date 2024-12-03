
class Cellule:
    def __init__(self,v,s):
        self.valeur = v
        self.suivante = s



def occurence_recursive(x,lst):
    if lst is None:
        return 0
    elif lst.valeur == x:
        return 1 + occurence_recursive(x, lst.suivante)
    else:
        return occurence_recursive(x, lst.suivante)
    
def occuence_while(x,lst):
    n=0 
    while lst is not None:
        if lst.valeur == x:
            n +=1
            lst.suivante
        else:
            lst.suivante
    return n 


def premiere_occrence_x_recursive(x,lst):
    if lst is None:
        return None
    elif lst.valeur == x:
        return 0
    else:
        trouve =premiere_occrence_x_recursive(x,lst.suivante)
        if trouve is not None:
            return 1+ trouve
        else:
            return None
        


def premaire_occurence_x_while(x,lst):
    n=0
    while lst is not None:
        if lst.valeur == x:
            return n 
        else:
            lst.suivante
            n+=1

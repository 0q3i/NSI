def identique(l1,l2):
    if l1.valeur != l2.valeur:
        return False
    elif l1 is None and l2 is None:
        return True
    else:
        return identique(l1,l2)
from pile import *

def chaine_bien_parenthesee(str):
    p_parenthese = Pile()
    p_crocher = Pile()
    for elm in str:
        if elm == "(":
            p_parenthese.empiler(elm)
        elif elm == ")":
            p_parenthese.depiler()
        elif elm == "[":
            p_crocher.empiler(elm)
        elif elm =="]":
            p_crocher.depiler()
    if p_parenthese.est_vide() == p_crocher.est_vide():
        return True
    return False


assert chaine_bien_parenthesee("()")== True
assert chaine_bien_parenthesee("[([])]")== True
assert chaine_bien_parenthesee("(")== False
#Exo1
def trouve(tab, p):
    for elm in tab:
        if p(elm):
            return elm
    return None

#Exo2
def applique1(fonc , tab):
    nov_tab= []
    for elm in tab:
        nov_tab.append(fonc(elm))
    return nov_tab

def applique2(fonc, tab):
    return [fonc(elm) for elm in tab]

#JEU DE TEST
#test exo1
tab = [1,3,5,2]
def p(x):
    return x%2 == 0
assert trouve(tab,p) == 2
#test exo2
tab = [1,2,3,4,5]
def f(x):
    return x**2
assert applique1(f,tab) == [1,4,9,16,25]
assert applique2(f,tab) == applique1(f,tab)



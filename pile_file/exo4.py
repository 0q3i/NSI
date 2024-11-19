from pile import *

def parenthese(strr, f):
    p = Pile()
    n = 0
    run = True
    for i in range(f):
        p.empiler(strr[i])
    while run:
        parenthese_ouvrante = p.depiler()
        if p.est_vide():
            run = False
        if parenthese_ouvrante == "(":
            return n 
        n+=1
    raise SyntaxError

assert parenthese("(())",3) == 1

assert parenthese("(2))",3) == 0
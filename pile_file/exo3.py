from pile import *

def polonais(strC):
    p = Pile()
    for elm in strC:
        if elm != " ":
            if elm not in ["*","+"]:
                a = int(elm)
                p.empiler(a)
            else:
                if elm == "*":
                    x = p.depiler()
                    y = p.depiler()
                    z = x*y
                    p.empiler(z)
                else:
                    x = p.depiler()
                    y = p.depiler()
                    z = x+y
                    p.empiler(z)                  
    return p.depiler()


assert polonais("1 2 3 + * ") == 5
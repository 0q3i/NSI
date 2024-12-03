def point(x,y):
    return (x,y)

def deplacer_triangle(t,dx,dy):
    copie = list(t)
    for  i in range(len(t)):
        copie.append((copie[i][0]+dx,copie[i][1]+dy))
    return tuple(copie)

a = point(0,1)
b = point(1,1)
c = point(2,1)
d = point(3,1)

t1 = (a,b,c)
t2 = (b,c,d)

t3 = deplacer_triangle(t1,-1,-1)
t4 = deplacer_triangle(t2,2,3)







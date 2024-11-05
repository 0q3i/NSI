
def f(elm):
    pass

def calcule(op,f,t):
    val = t[0]
    for i in range(len(t)):
        val = op(val, f(t[i]))
    return val


def fibonacci(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1 
    else:
        return fibonacci(n-1) + fibonacci(n-2) 
    
#jeu de test

assert fibonacci(2) == 1 
assert fibonacci(5) == 5
assert fibonacci(8) == 21

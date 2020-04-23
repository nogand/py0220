"""
   Módulo Fibonacci
   2020-04-22
   Greencore - PY0220
   Módulo de ejemplo con la serie de Fibonacci implementada de múltiples maneras.
"""

def fibo(n):
    # Recibe un número n, entero mayor a cero, y devuelve el elemento n-ésimo de la serie de Fibonacci
    if n <= 2:
        return 1
    else :
        return fibo(n-1)+fibo(n-2)

"""
   fibo(1) -> 1
   fibo(2) -> 1
   fibo(3) -> fibo(2)+fibo(1) -> 1+1 -> 2
   fibo(4) -> fibo(3)+fibo(2) -> (fibo(2)+fibo(1))+1 -> (1+1)+1 -> 3
   fibo(5) -> fibo(4)+fibo(3) -> (fibo(3)+fibo(2))+(fibo(2)+fibo(1)) -> ((fibo(2)+fibo(1))+1)... -> 5
"""

def fiblist(n):
    # Recibe un número n, entero mayor a cero, y devuelve una lista de los elementos de la serie de Fibonacci hasta ese número.
    if n == 1 :
        return [ 1 ]
    else :
        return fiblist(n-1)+[ fibo(n) ]

"""
   fiblist(1) -> [ 1 ]
   fiblist(2) -> fiblist(1)+[ fibo(2) ] -> [ 1 ] + [ 1 ] -> [1, 1]
   fiblist(3) -> fiblist(2)+[ fibo(3) ] -> [1, 1] + [ 2 ] -> [1, 1, 2] 
   fiblist(4) -> fiblist(3)+[ fibo(4) ] -> [1, 1, 2] + [ 3 ] -> [1, 1, 2, 3]
"""

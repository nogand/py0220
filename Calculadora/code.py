#!/usr/bin/python3
from calculadora import *

operaciones={"+":suma, "-":resta, "*":multiplicacion, "/": division}

def esnumero(candidato):
    valido=True
    for caracter in candidato :
        if caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9" or caracter == "0" :
            continue
        else :
            valido=False
            break
    return valido
    
print("Bienvenido a la calculadora")
operacion = ""
while len(operacion) != 1 or operacion not in '+-*/' :
    operacion=input("Indique la operación (+, -, *, /): ")

oper1=input("Indique el primer número: ")
oper2=input("Indique el segundo número: ")
if oper1.isnumeric() and oper2.isnumeric() :
    oper1 = int(oper1)
    oper2 = int(oper2)
    print(operaciones[operacion](oper1, oper2))
else :
    print("Error! Ambos números deben tener formato numérico.")

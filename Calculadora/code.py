from calculadora import *

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
operacion=input("Indique la operación (+, -, *, /): ")
oper1=input("Indique el primer número: ")
oper2=input("Indique el segundo número: ")
if esnumero(oper1) and esnumero(oper2) :
    oper1 = int(oper1)
    oper2 = int(oper2)
    if operacion == "+" :
        print(suma(oper1,oper2))
    elif operacion == "-" :
        print(resta(oper1, oper2))
    elif operacion == "*" :
        print(multiplicacion(oper1, oper2))
    elif operacion == "/" :
        print(division(oper1, oper2))
    else :
        print("Error! Eso no es una operación válida!")
else :
    print("Error! Ambos números deben tener formato numérico.")

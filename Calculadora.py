#Funcion Suma
def suma(a,b):
    return a+b

#Función resta
def resta(a, b):
    return a - b

def multiplicacion(a,b):   #Devuelve la multiplicacion de dos enteros
    return a*b
    
def division(a: float,b: float) -> float:
	if b == 0:
		raise ZeroDivisionError("division by zero")
	return a / b


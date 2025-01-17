#clases def


def saludar():
    print("¡Hola, mundo!")


saludar()


def saludar2(nombre):
    print("¡Hola,", nombre, "!")


saludar2("Juan")


def sumar_restar(a, b):
    suma = a + b
    resta = a - b
    return suma, resta


resultadosuma, resultadoresta = sumar_restar(3, 5)
print(resultadosuma , resultadoresta)

def saludar3(nombre, saludo="Hola"):
    print(saludo + ",", nombre, "!")


saludar3("Pedro")  

saludar3("Ana", "Buen día")  



def sumar(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado


print(sumar(1, 5, 3))  
print(sumar(4, 5))  



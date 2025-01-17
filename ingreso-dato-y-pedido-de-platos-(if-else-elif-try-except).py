#ingreso dato y pedido de platos (if-else-elif-try-except)
edad = int(input('Ingrese la edad: '))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
plato = input("Ingrese el nombre del plato que desea pedir: ")
if plato == 'hamburguesa':
    precio = 10
    print("El precio de ", plato, 'es ',precio)
elif plato == 'pizza':
    precio = 12
    print("El precio de ", plato, 'es ',precio)
elif plato == 'ensalada':
    precio = 8
    print("El precio de ", plato, 'es ',precio)
elif plato == 'papas fritas':
    precio = 5
    print("El precio de ", plato, 'es ',precio)
else:
    print("Lo siento, ese plato no está en el menú")
try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 / num2
     
        print(f"El resultado de la división es {resultado}")
except ValueError:
        print("Error: Debe ingresar un número válido. Por favor intente nuevamente.")        
        
except ZeroDivisionError:      
        print("Error: No se puede dividir por cero. Por favor ingrese otro número.")

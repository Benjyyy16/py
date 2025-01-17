#menu usando funcionespython 



def sum(a, b):
    c=a+b 
    return (c)

def resta(a,b):
    return (a-b)

def multi(a, b):
    return (a*b)


def fibonacci_iter(n):
    a=1
    b=1
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            print(total)

def numeros_primos(n):
    for i in range(2, n+1):
        primo = True
        for j in range(2, i):
            if i == j:
                break
            elif i % j == 0:
                primo = False
            else:
                continue
        if primo == True:
            print(' ', i, end='')

opc = 0 

while(opc!=-1):
    print("Menú: \n")
    print("Ingrese opción: \n")
    print("1 - Suma \n")
    print("2 - Resta \n")
    print("3 - Multi \n")
    print("4 - Fibonacci \n")
    print("5 - Numeros primos \n")
    print("6 - Finalizar \n")
    
    opc = int(input('Ingresa la opción:'))
    
    if(opc==1):

        a = int(input('Ingrese el primer numero'))
        b = int(input('Ingrese el segundo numero'))
        print("La respuesta es", sum(a,b))

    elif(opc==2):

        a = int(input('Ingrese el primer numero'))
        b = int(input('Ingrese el segundo numero'))
        print("La respuesta es", resta(a,b))

    elif(opc==3):

        a = int(input('Ingrese el primer numero'))
        b = int(input('Ingrese el segundo numero'))
        print("La respuesta es", multi(a,b))

    elif(opc==4):
        n = int(input('Ingrese el numero'))
        fibonacci_iter(n)
    
    elif(opc==5):
        n = int(input('¿Hasta qué número quieres la lista?: '))
        numeros_primos(n)

    elif(opc==6):

        print("Desea realizar una nueva operación?")
        a = input('si o no: ')

        if(a=="si"):
            opc=0
        else:
            opc=-1
            print("Programa finalizado")

    else:
        print("Opcion invalida")
        
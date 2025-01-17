
#funciones variables y definiciones
"""
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5"""

flag=True

while flag:
    fila = input("Ingrese el número de filas: ")
    try:
        filan=int(fila)
        break 
    except:
        print("Ingrese solo valores numéricos")
for i in range(1, filan+1): 
    for j in range(1, i+1 ): 
        print(j, end=' ')  
    print("")     


while True:

    try:
        inicio=int(input("Ingrese el valor inicial del rango deseado: "))
        final=int(input("Ingrese el valor final del rango deseado: "))
        if final>inicio:
            break
        else:
            print("El valor inicial no debe ser mayor o igual que el final")
    except:
        print("Datos Incorrectos vuelva a ingresarlos")    
 
for num in range(inicio, final+1,1):
    if num>1:

        for i in range(2,num):
        
            if num % i == 0:
                break
        else:
            print(num, end=' ')
    else:
        continue

"""
while True:
    try:
        n=int(input("Ingrese el valor de n: "))
        break   
    except:
        print("Ingrese un valor correcto")
num1 = 0
num2 = 1

for i in range(0,n):
    # imprimir el siguiente número de la serie
    print(num1, end="  ")
    # Sumar los dos números anteriores
    res = num1 + num2

    # Actualizar valores
    num1 = num2
    num2 = res"""

flag = True
while flag:
    print("Seleccione el número de ejemplo" )
    print("1._Imprimir Patrón")
    print("2._Números Primos")
    print("3._Serie Fibonacci")
    print("4._Salir")
    opt=input("Ingrese la Opción: ")
    if opt=="1":
        program=1
        
    elif opt=="2":
        program=2
        
    elif opt=="3":
        program=3
    elif opt=="4":
        program=4
        
    else:
        print("Dato incorrecto")
        

    if program==1:
        print("Imprimir patrón seleccionado")
        flag=True

        while flag:
            fila = input("Ingrese el número de filas: ")
            try:
                filan=int(fila)
                break 
            except:
                print("Ingrese solo valores numéricos")
        for i in range(1, filan+1): 
            for j in range(1, i+1 ):
                print(j, end=' ')   
            print("")
        
        
        while True:
            finish=input("Desea probar nuevos programas(Y/N): ")
            if finish=="Y":
                flag=True
                break
            elif finish=="N":
                flag=False
                print("Gracias!!!")
                break
            else:
                print("Ingrese un dato válido")

    elif program==2:
        print("Números primos seleccionados")
        while True:
  
            try:
                inicio=int(input("Ingrese el valor inicial del rango deseado: "))
                final=int(input("Ingrese el valor final del rango deseado: "))
                if final>inicio:
                    break
                else:
                    print("El valor inicial no debe ser mayor o igual que el final")
            except:
                print("Datos Incorrectos vuelva a ingresarlos")    

        for num in range(inicio, final+1,1):
            if num>1:

                for i in range(2,num):
        
                    if num % i == 0:
                        break
                else:
                    print(num, end=' ')
            else:
                continue
        print("")
        while True:
            finish=input("Desea probar nuevos programas(Y/N): ")
            if finish=="Y":
                flag=True
                break
            elif finish=="N":
                flag=False
                print("Gracias!!!")
                break
            else:
                print("Ingrese un dato válido")
    elif program==3:
        print("Serie Fibonacci seleccionada")
        while True:
            try:
                n=int(input("Ingrese el valor de n: "))
                break   
            except:
                print("Ingrese un valor correcto")
        num1 = 0
        num2 = 1

        for i in range(0,n):

            print(num1, end="  ")

            res = num1 + num2


            num1 = num2
            num2 = res
        print("")
        while True:
            finish=input("Desea probar nuevos programas(Y/N): ")
            if finish=="Y":
                flag=True
                break
            elif finish=="N":
                flag=False
                print("Gracias!!!")
                break
            else:
                print("Ingrese un dato válido")
    elif program==4:
        print("Gracias!!!")
        flag=False

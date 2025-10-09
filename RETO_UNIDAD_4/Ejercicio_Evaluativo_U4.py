from implementacion import *

while True:
    opc = int(input("Calcular CG\t\t(1). \nElementos del programa\t\t(2). \nSalir\t\t(3)\n\nIngresar opción: "))
    match opc:
        case 1:
            print("Abriendo calculadora ...")
            OP2()
        case 2:
            print("Elementos del programa")
            OP3()    
        case 3:
            print("Saliendo...")
            break
        case _:
            print("Error\n\nSeleccione una opción válida (1 ó 2)")
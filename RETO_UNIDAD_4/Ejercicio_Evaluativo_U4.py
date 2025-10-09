from implementacion import *

opc = int(input("¿Desea calcular el CG de su avión?. Sí (1). No (2): "))
while True:
    match opc:
        case 1:
            print("Abriendo calculadora ...")
            OP2()
        case 2:
            print("Saliendo...")
            break
        case _:
            print("Error\n\nSeleccione una opción válida (1 ó 2)")
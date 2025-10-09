# Opcion 2

info_aeronave = {
    "MDL": "",
    "MTCL": "",
    "NSRE": ""
    }

datum = []


def CALC_CG (MT, PMT):
    CG = MT / PMT
    return CG

def OP2 ():
    info_aeronave["MDL"] = input("Ingrese el modelo de la aeronave: ")
    info_aeronave["MTCL"] = input("Ingrese la matrícula de la aeronave: ")
    info_aeronave["NSRE"] = input("Ingrese el número de serie de la aeronave: ")

    BDMN = float(input("Ingrese la distancia desde el DATUM hasta el punto de apoyo del tren de nariz (ft): "))
    datum.append(BDMN)
    BDMP = float(input("Ingrese la distancia desde el DATUM hasta el punto de apoyo del tren principal: "))
    datum.append(BDMP)
    RPCG = float(input("Ingrese el Rango Permitido del Centro de Gravedad (en distancia desde el datum): "))
    datum.append(RPCG)
    RPCGmin = datum[2] - 1
    datum.append(RPCGmin)
    RPCGmax = datum[2] + 1
    datum.append(RPCGmax)

    while True:
        PMTN = float(input("Ingrese el peso registrado en el Tren de nariz (lb): "))
        PMTPI = float(input("Ingrese el peso registrado en el Tren principal (izquierda)): "))
        PMTPD = float(input("Ingrese el peso registrado en el Tren principal (derecha): "))
        PMTP = PMTPI + PMTPD    
        PMT = PMTP + PMTN
        MPN = PMTN * BDMN
        MPP = PMTP * BDMP
        MT = MPN + MPP
        CG = CALC_CG (MT, PMT)
        if datum[3] < CG < datum[4]:
            break
        elif CG < datum[3]: 
            print ("Añada más peso atras o reduzca adelante e introduzca los nuevos datos")
        elif CG > datum[4]:
            print ("Añada más peso adelante o reduzca atras e introduzca los nuevos datos")
    print (f"El avión {info_aeronave["MDL"]} con matrícula {info_aeronave["MTCL"]} y numero de serie {info_aeronave["NSRE"]}, cuenta con un CG a {CG:0.2f}ft del Datum, Dato valido para permitir su salida.")

def OP3():
    print("Diccionarios:")
    for k, v in info_aeronave.items():
        print(f"{k} --> {v}")
    print("Lista: ""datum []""")
    for i in range(len(datum)):
        print (datum[i])
# Diccionario vacío
aeronave = {}

# Diccionario con elementos
aeronave = {
    "modelo": "Boeing 787-9",
    "envergadura": 60.17,  # metros
    "longitud": 62.81,     # metros
    "mtow": 254000,        # kg
    "velocidad_max": 954   # km/h
}

aeronave["altura"] = 16.9

for k, v in aeronave.items():
    print(f"{k} --> {v}")

"""
print (f"Modelo: {aeronave["modelo"]}, mide: {aeronave["longitud"]}")

# Diccionario con diferentes tipos de datos como valores
vuelo = {
    "numero": "AA123",
    "origen": "KLAX",
    "destino": "KJFK",
    "distancia": 3983,
    "a_tiempo": True,
    "tripulacion": ["Capitán Smith", "F/O Johnson", "F/E Williams"]
}
print (f"Origen: \n {vuelo["numero"]},\nDestino: \n {vuelo["destino"]},\nTripulacion: ")

for n in vuelo["tripulacion"]:
    print (f" {n}")
# Creación con dict()
motor = dict(fabricante="GE", modelo="GE9X", empuje=470, bypass_ratio=10)

# Acceso a valores
print(aeronave["modelo"])  # "Boeing 787-9"

# Modificación de valores
aeronave["mtow"] = 260000

# Añadir nuevo par clave-valor
aeronave["alcance"] = 14140  # km

# Eliminar par clave-valor
del aeronave["velocidad_max"]

# Comprobar existencia de clave
if "alcance" in aeronave:
    print(f"El alcance es {aeronave['alcance']} km")

# Método get() (devuelve None o un valor por defecto si la clave no existe)
velocidad = aeronave.get("velocidad_max", "No disponible")
"""
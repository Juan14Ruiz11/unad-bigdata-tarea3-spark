
import csv
import glob
import matplotlib.pyplot as plt
from datetime import datetime

# Buscar el archivo CSV generado por Spark
archivos = glob.glob("resultado_trm/part-*.csv")

if not archivos:
    print("No se encontro el archivo CSV de resultados.")
    raise SystemExit(1)

fechas = []
valores = []

with open(archivos[0], "r", newline="") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        if fila["fecha_inicial"] and fila["trm"]:
            fecha = datetime.strptime(
                fila["fecha_inicial"], "%Y-%m-%d"
            )
            fechas.append(fecha)
            valores.append(float(fila["trm"]))

# Ordenar por fecha
datos = sorted(zip(fechas, valores))
fechas = [dato[0] for dato in datos]
valores = [dato[1] for dato in datos]

# Crear grafica
plt.figure(figsize=(10, 5))
plt.plot(fechas, valores, marker="o")
plt.title("Evolucion de la TRM")
plt.xlabel("Fecha")
plt.ylabel("Valor de la TRM (COP)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("grafica_trm.png")
plt.show()

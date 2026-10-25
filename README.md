Tarea 3: Procesamiento de datos con Apache Spark

1. Descripción del proyecto

Este proyecto desarrolla un procesamiento por lotes (Batch) utilizando Apache Spark y Python mediante PySpark. Se trabaja con un conjunto de datos de la Tasa Representativa del Mercado (TRM) expresada en pesos colombianos (COP).

El propósito es cargar los datos, realizar su limpieza y transformación, obtener estadísticas descriptivas y visualizar la evolución de la TRM.

2. Tecnologías utilizadas

Apache Spark 3.5.1.

Python y PySpark.

Hadoop y HDFS.

Matplotlib para la visualización de los resultados.

3. Procesamiento realizado

El programa tarea3.py desarrolla las siguientes actividades:

Carga el conjunto de datos desde HDFS.

Asigna nombres a las columnas.

Elimina registros con valores nulos y registros duplicados.

Convierte la TRM a un tipo numérico y transforma las fechas.

Realiza un análisis exploratorio de los datos mediante estadísticas descriptivas.

Calcula la cantidad de registros, el promedio, el valor mínimo y el valor máximo de la TRM.

Utiliza un RDD para calcular la cantidad de registros y el promedio.

Guarda los resultados procesados en formato CSV.

El archivo grafica_trm.py permite generar una gráfica de líneas para visualizar la evolución de la TRM por fecha.

4. Archivos del proyecto

tarea3.py: código del procesamiento por lotes con PySpark.

grafica_trm.py: código para generar la gráfica de la TRM.

README.md: descripción del proyecto e instrucciones de ejecución.

5. Requisitos previos

Para ejecutar el proyecto se requiere tener instalado y configurado:

Python.

Apache Spark y PySpark.

Hadoop con HDFS en funcionamiento.

Matplotlib, para generar la gráfica.

También se necesita disponer del conjunto de datos de la TRM en HDFS, en la ruta utilizada por el programa.

6. Instrucciones de ejecución

Paso 1. Iniciar los servicios de Hadoop

Iniciar los servicios de HDFS según la configuración de la máquina virtual.

Paso 2. Verificar los datos

Comprobar que el archivo de datos esté disponible en la ruta:

/Tarea3/rows.csv

Paso 3. Ejecutar el procesamiento Batch

Desde la terminal de Linux, ejecutar:

spark-submit tarea3.py

El comando debe ejecutarse desde la carpeta donde se encuentra el script. Si el archivo está en otra ubicación, se debe indicar su ruta.

Paso 4. Consultar los resultados

El programa muestra en la terminal los datos originales, los datos limpios y las estadísticas calculadas. También guarda los resultados procesados en la carpeta resultado_trm.

Paso 5. Generar la gráfica

Una vez finalizado el procesamiento, ejecutar:

python3 grafica_trm.py

El programa genera el archivo grafica_trm.png con la evolución de la TRM.

7. Resultados esperados

Se espera obtener un conjunto de datos limpio, estadísticas descriptivas de la TRM, cálculos mediante DataFrames y RDDs, un archivo CSV con los resultados procesados y una gráfica de líneas.

8. Fuente de datos

Conjunto de datos de la Tasa Representativa del Mercado (TRM), utilizado en el procesamiento de la actividad académica.

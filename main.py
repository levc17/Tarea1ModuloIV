from pyspark.sql import SparkSession
from pyspark.sql.types import (IntegerType,StringType, StructField,StructType,FloatType,DateType)
import sys
from functions import join_dfs,aggregate,top_n

#inputs
input_1 = sys.argv[1] #ciclista
input_2 = sys.argv[2] #ruta
input_3 = sys.argv[3] #actividad

#spark session

spark = SparkSession.builder \
    .master("local") \
    .appName("tarea1")  \
    .getOrCreate()

#Schema creation

ciclistas_schema= StructType([
    StructField('Cedula',IntegerType()),
    StructField('Nombre',StringType()),
    StructField('Provincia',StringType())])


ruta_schema= StructType([
    StructField('Codigo Ruta',IntegerType()),
    StructField('Nombre Ruta',StringType()),
    StructField('Kilometros',IntegerType())])

actividad_schema= StructType([
    StructField('Codigo Ruta',IntegerType()),
    StructField('Cedula',IntegerType()),
    StructField('Fecha',DateType())])

#DataFrame Creation


df_ciclista= spark.read.csv(input_1,schema=ciclistas_schema,header=False)
df_ruta=spark.read.csv(input_2,schema=ruta_schema,header=False)
df_actividad=spark.read.csv(input_3,schema=actividad_schema,header=False)

df_ciclista.show()

df_ruta.show()

df_actividad.show()

import pandas as pd
import pymysql
import datetime

from arcgis.features import SpatialDataFrame

from arcgis.gis import GIS
from IPython.display import display

from getpass import getpass

#Imprime finalización de ejecución
print("Started")

#Conexión con la base de datos MySQL.
connection = pymysql.connect(
host='localhost',
port=3306,
user='root',
password='',
db='recorre'
)


#Conexión con ArcGIS online
gis = GIS()
#Id de la capa de ArcGIS online donde se están 
#almacenando los datos enviados del survey123
item = gis.content.get("39f00564a0aa439a85174913be7e792f")

#Obtener datos de la capa de ArcGIS online
sdf = pd.DataFrame.spatial.from_layer(item.layers[0])


#Guarda los registros por columna en un arreglo de
#esa capa
capEfectiva = sdf['capEfectiva'].fillna(-1)
arregloCapEfectiva = capEfectiva.values


#Guarda los registros por columna en un arreglo de
#esa capa
creationDate = pd.to_datetime(sdf['CreationDate'])
arregloCreationDate = creationDate.values


#Cursor para la conexión con la base de dato MySQL
cursor1 = connection.cursor()
sql1 = 'DELETE from graficar'
cursor1.execute(sql1)
connection.commit()


#Ciclo que permite recorrer los arreglos e insertar
#los datos respectivos de cada posición de este
#en la base de datos MySQL
for i, j in zip(arregloCapEfectiva, arregloCreationDate):

    if i != -1:
        cursor = connection.cursor()
        sql = 'INSERT INTO graficar(capacidadCarga, CreationDate) values(%s, %s)'
        val = (float(i), str(j))
        cursor.execute(sql, val)
        connection.commit()


#Obtener datos de la capa de ArcGIS online
sdf2 = pd.DataFrame.spatial.from_layer(item.layers[2])

#Prom_VisSend, Prom_Ancho, Area_Sendero, Cap_Fisica, CreationDate

prom_VisSend = sdf2['Prom_VisSend'].fillna(-1)
arregloProm = prom_VisSend.values



prom_ancho = sdf2['Prom_Ancho'].fillna(-1)
arregloPromAncho = prom_ancho.values


area_sendero = sdf2['Area_Sendero'].fillna(-1)
arregloAreaSendero = area_sendero.values


cap_fisica = sdf2['Cap_Fisica'].fillna(-1)
arregloCapFisica = cap_fisica.values


creationDate = pd.to_datetime(sdf2['CreationDate'])
arregloCreationDate = creationDate.values


#Cursor para la conexión con la base de dato MySQL
cursor2 = connection.cursor()
sql2 = 'DELETE from tabla2'
cursor2.execute(sql2)
connection.commit()


#Ciclo que permite recorrer los arreglos e insertar
#los datos respectivos de cada posición de este
#en la base de datos MySQL
for i, j, p, b, n in zip(arregloProm, arregloPromAncho, arregloAreaSendero, arregloCapFisica, arregloCreationDate):

    if i != -1 or j != -1 or p != -1 or b != -1:
        cursor = connection.cursor()
        sql = 'INSERT INTO tabla2(prom_VisSend, prom_ancho, area_sendero, cap_fisica, creationDate) values(%s, %s, %s, %s, %s)'
        val = (float(i), float(j), float(p), float(b), str(n))
        cursor.execute(sql, val)
        connection.commit()



sdf3 = pd.DataFrame.spatial.from_layer(item.layers[3])

#area_Erod, CreationDate
areaErod = sdf3['area_Erod'].fillna(-1)
arregloAreaErod = areaErod.values


creationDate3 = pd.to_datetime(sdf3['CreationDate'])
arregloCreationDate3 = creationDate3.values


#Cursor para la conexión con la base de dato MySQL
cursor3 = connection.cursor()
sql3 = 'DELETE from tabla3'
cursor3.execute(sql3)
connection.commit()

#Ciclo que permite recorrer los arreglos e insertar
#los datos respectivos de cada posición de este
#en la base de datos MySQL
for i, j in zip(arregloAreaErod, arregloCreationDate3):
    if i != -1:
        cursor = connection.cursor()
        sql = 'INSERT INTO tabla3(areaErod, creationDate) values(%s, %s)'
        val = (float(i), str(j))
        cursor.execute(sql, val)
        connection.commit()


#Obtener datos de la capa 4 de ArcGIS online
sdf4 = pd.DataFrame.spatial.from_layer(item.layers[4])


#verificar_pend_A, long_Acces, CreationDate
verPendA = sdf4['verificar_pend_A'].fillna(-1)
arregloVerPendA = verPendA.values


longAcc = sdf4['long_Acces'].fillna(-1)
arregloVerPendA = longAcc.values


creationDate4 = pd.to_datetime(sdf4['CreationDate'])
arregloCreationDate4 = creationDate4.values


#Cursor para la conexión con la base de dato MySQL
cursor4 = connection.cursor()
sql4 = 'DELETE from tabla4'
cursor4.execute(sql4)
connection.commit()


#Ciclo que permite recorrer los arreglos e insertar
#los datos respectivos de cada posición de este
#en la base de datos MySQL
for i, j, p in zip(arregloVerPendA, arregloVerPendA, arregloCreationDate4):

   if i != -1 or j != -1:
       cursor = connection.cursor()
       sql = 'INSERT INTO tabla4(verificar_pend_A, long_Acces, CreationDate) values(%s, %s, %s)'
       val = (float(i), float(j), str(p))
       cursor.execute(sql, val)
       connection.commit()


#Obtener datos de la capa 6 de ArcGIS online
sdf6 = pd.DataFrame.spatial.from_layer(item.layers[6])


#dias_especiales, CreationDate

dias_especiales = sdf6['dias_especiales'].fillna(-1)
arregloDiasEspeciales = dias_especiales.values


creationDate6 = pd.to_datetime(sdf6['CreationDate'])
arregloCreationDate6 = creationDate6.values


#Cursor para la conexión con la base de dato MySQL
cursor6 = connection.cursor()
sql6 = 'DELETE from tabla6'
cursor6.execute(sql6)
connection.commit()

#Ciclo que permite recorrer los arreglos e insertar
#los datos respectivos de cada posición de este
#en la base de datos MySQL
for i, p in zip(arregloDiasEspeciales, arregloCreationDate6):
    if i != -1:
        cursor = connection.cursor()
        sql = 'INSERT INTO tabla6(dias_especiales, creationDate) values(%s, %s)'
        val = (float(i),  str(p))
        cursor.execute(sql, val)
        connection.commit()



#Obtener los datos de la capa 7 dese ArcGIS Online
sdf7 = pd.DataFrame.spatial.from_layer(item.layers[7])


#sum_flora, CreationDate
sumFlora = sdf7['sum_flora'].fillna(-1)
arregloSumFlora = sumFlora.values


creationDate7 = pd.to_datetime(sdf7['CreationDate'])
arregloCreationDate7 = creationDate7.values

#Cursor para la conexión con la base de dato MySQL
cursor7 = connection.cursor()
sql7 = 'DELETE from tabla7'
cursor7.execute(sql7)
connection.commit()

#Ciclo que permite recorrer los arreglos e insertar
#los datos respectivos de cada posición de este
#en la base de datos MySQL
for i, p in zip(arregloSumFlora, arregloCreationDate7):
    if i != -1:
        cursor = connection.cursor()
        sql = 'INSERT INTO tabla7(sum_flora, creationDate) values(%s, %s)'
        val = (float(i),  str(p))
        cursor.execute(sql, val)
        connection.commit()

#Método que permite modificar la hora de cada
#registro, esto se hace para poder utilizar
#la hora actual Colombiana.
def modificarFecha():
    cursorModificar = connection.cursor()
    sql1 = 'UPDATE graficar set CreationDate = DATE_SUB(CreationDate, INTERVAL 7 HOUR);'
    sql2 = 'UPDATE tabla2 set creationDate = DATE_SUB(creationDate, INTERVAL 7 HOUR);'
    sql3 = 'UPDATE tabla3 set creationDate = DATE_SUB(creationDate, INTERVAL 7 HOUR);'
    sql4 = 'UPDATE tabla4 set creationDate = DATE_SUB(creationDate, INTERVAL 7 HOUR);'
    sql6 = 'UPDATE tabla6 set creationDate = DATE_SUB(creationDate, INTERVAL 7 HOUR);'
    sql7 = 'UPDATE tabla7 set creationDate = DATE_SUB(creationDate, INTERVAL 7 HOUR);'

    cursorModificar.execute(sql1)
    cursorModificar.execute(sql2)
    cursorModificar.execute(sql3)
    cursorModificar.execute(sql4)
    cursorModificar.execute(sql6)
    cursorModificar.execute(sql7)

    connection.commit()


#Llama al método modificarFecha(), para ejecución
modificarFecha()

#Imprime finalización de ejecución
print("Completed")
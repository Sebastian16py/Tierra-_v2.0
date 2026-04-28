# Importar las librerias de sqlite y pandas para manejo de datos
import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

# Conectar con la base de datos
conn = sqlite3.connect('sistemas_planetarios.db')

# Columnas a extraer de la tabla  limpia
QUERY = 'SELECT AVG(pl_rade) AS Radio_promedio, discoverymethod AS Metodo FROM planetas GROUP BY discoverymethod'
df = pd.read_sql_query(QUERY, conn)

# Se muestran por consola el promedio de radio para cada grupo de exoplaneta
print(df)

# Segunda Consulta: filtro de habitabilidad
QUERY_2 = 'SELECT pl_eqt AS Temperatura_equilibrio, pl_rade AS Radio_promedio, st_teff  FROM planetas WHERE pl_eqt BETWEEN 200 AND 320 AND pl_rade<2.5'
df_2 = pd.read_sql_query(QUERY_2, conn)
print('Filtro de habitabilidad realizado')

# DaAtos generales
QUERY_3 = 'SELECT st_teff, pl_eqt FROM planetas'
df_3 = pd.read_sql_query(QUERY_3,conn)
conn.close()
print('Exoplanetas que poseen todos los datos')
print(len(df_3))

print(df_2.describe())
print(df_2[['Temperatura_equilibrio','Radio_promedio']].head())

# Grafica 
plt.style.use('dark_background')
plt.scatter(df_3['st_teff'], df_3['pl_eqt'], c='gray', label = 'Exoplanetas detectados en La Silla')
plt.scatter(df_2['st_teff'], df_2['Temperatura_equilibrio'], c='darkblue', label='Potencialmente habitables')

plt.grid(alpha=0.3)
plt.xlabel('Temporatura de la Estrella')
plt.ylabel('Temperatura del exoplaneta')
plt.legend()
plt.show(block=False) 
plt.savefig('filtro_habitabilidad.png')
print('Imagen generada exitosamente')



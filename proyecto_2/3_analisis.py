# Importar las librerias de sqlite y pandas para manejo de datos
import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Conectar con la base de datos
conn = sqlite3.connect('sistemas_planetarios.db')

# Columnas a extraer de la tabla  limpia
QUERY = 'SELECT AVG(pl_rade) AS Radio_promedio, discoverymethod AS Metodo FROM planetas GROUP BY discoverymethod'
df = pd.read_sql_query(QUERY, conn)


# Se muestran por consolas el promedio de radio para cada grupo de exoplaneta
print(df)

# Segunda Consulta: filtro de habitabilidad
QUERY_2 = 'SELECT pl_eqt AS Temperatura_equilibrio, pl_rade AS Radio_promedio FROM planetas WHERE 200<pl_eqt<320 AND pl_rade<2.5'
df_2 = pd.read_sql_query(QUERY_2, conn)
print('Filtro de habitabilidad realizado')
conn.close()
 

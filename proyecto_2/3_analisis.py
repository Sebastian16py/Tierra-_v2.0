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

conn.close()

print(df)

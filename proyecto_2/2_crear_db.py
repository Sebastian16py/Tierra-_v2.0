import pandas as pd
import sqlite3

# Leer los datos
df = pd.read_csv('exoplanetas_bruto.csv')

# Limpiar los datos
df = df.dropna(subset=['pl_rade','pl_eqt'])

# Conectar con una base de datos local
conn = sqlite3.connect('sistemas_planetarios.db')

df.to_sql('planetas', conn, if_exists='replace', index=False)
conn.close()
print('Exoplanetas filtrados a sistemas_planetarios.db')

\# Redactamos el Query
ADQL="SELECT pl_name,discoverymethod,disc_facility,pl_rade,pl_eqt,st_teff from ps WHERE disc_facility='La Silla Observatory'"

# Reemplazamos los espacios '+' usando 'sed' para que la URL no se rompa
URL_ADQL=$(echo $ADQL | sed 's/ /+/g')

# Definimos el endpoint
TAP_URL="https://exoplanetarchive.ipac.caltech.edu/TAP/sync?format=csv&query="

wget -O exoplanetas_bruto.csv "$TAP_URL$URL_ADQL"
echo 'Datos descargados en exoplanetas_bruto.csv'

echo 'Creando Database...'
python3 2_crear_db.py

echo 'Realizando el analisis para los exoplanetas...'

#python3 3_analisis.py

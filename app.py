## importación de librerías y funciones
import sys
import os
## Añade la ruta de búsqueda para importación de paquetes (funciones personalizadas)
sys.path.append(os.path.join('..', 'src'))

import streamlit as st
import pandas as pd
import plotly as px

st.header('Los carritos')
st.write('Esta aplicación aún no es funcional. En construcción.')

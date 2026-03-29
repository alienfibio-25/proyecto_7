import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import scipy.stats as stats

# Load the cleaned data
@st.cache_data
def load_data():
    df = pd.read_csv('notebooks/vehicles_us_clean.csv')
    return df

df = load_data()

st.title('Análisis de Vehículos Usados')

# Sidebar for filters
st.sidebar.header('Filtros')

# Checkbox for manufacturers with more than 1000 ads
manufacturers_counts = df['make'].value_counts()
manufacturers_over_1000 = manufacturers_counts[manufacturers_counts > 1000].index.tolist()
show_only_large_manufacturers = st.sidebar.checkbox('Mostrar solo fabricantes con más de 1000 anuncios', value=False)

if show_only_large_manufacturers:
    df_filtered = df[df['make'].isin(manufacturers_over_1000)]
else:
    df_filtered = df

# Dataviewer
st.header('Vista de Datos')
columns_to_show = ['price', 'model_year', 'make', 'model', 'condition', 'cylinders', 'fuel', 'odometer', 'transmission', 'type', 'paint_color', 'is_4wd']
st.dataframe(df_filtered[columns_to_show])

# Gráfico de barras "Tipos de vehículo por fabricante"
st.header('Tipos de Vehículo por Fabricante')
type_counts = df_filtered.groupby(['make', 'type']).size().reset_index(name='count')
fig_bar = px.bar(type_counts, x='make', y='count', color='type', title='Tipos de Vehículo por Fabricante')
st.plotly_chart(fig_bar)

# Histograma de frecuencias "Año vs condición"
st.header('Histograma de Año vs Condición')
fig_hist = px.histogram(df_filtered, x='model_year', color='condition', title='Distribución de Años por Condición')
st.plotly_chart(fig_hist)

# Comparación de distribución de precios entre fabricantes
st.header('Comparación de Distribución de Precios entre Fabricantes')
makes = sorted(df_filtered['make'].unique())
make1 = st.selectbox('Seleccionar primer fabricante', makes, key='make1')
make2 = st.selectbox('Seleccionar segundo fabricante', makes, key='make2')
normalized = st.checkbox('Mostrar gráfica normalizada', value=True)

if make1 and make2:
    df_comp = df_filtered[df_filtered['make'].isin([make1, make2])].dropna(subset=['price'])
    if normalized:
        fig_comp = px.histogram(df_comp, x='price', color='make', histnorm='percent', title=f'Distribución Normalizada de Precios: {make1} vs {make2}')
    else:
        fig_comp = px.histogram(df_comp, x='price', color='make', title=f'Distribución de Precios: {make1} vs {make2}')
    st.plotly_chart(fig_comp)
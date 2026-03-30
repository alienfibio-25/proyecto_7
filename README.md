# Análisis de Vehículos Usados

Una aplicación web interactiva construida con Streamlit para el análisis exploratorio de datos de vehículos usados. Esta app permite visualizar y comparar datos de anuncios de venta de autos, facilitando insights sobre precios, condiciones, fabricantes y más.

## Características

### Vista de Datos
- **Dataviewer Interactivo**: Muestra una tabla con los datos principales de los vehículos, incluyendo precio, año del modelo, fabricante, modelo, condición, cilindros, combustible, odómetro, transmisión, tipo, color de pintura y si es 4WD.
- **Filtros**: Opción para mostrar solo fabricantes con más de 1000 anuncios.

### Gráficos Interactivos
- **Tipos de Vehículo por Fabricante**: Gráfico de barras que muestra la distribución de tipos de vehículos (SUV, pickup, sedan, etc.) por fabricante. La leyenda permite ocultar/mostrar tipos específicos.
- **Histograma de Año vs Condición**: Histograma que distribuye los años de los modelos por condición del vehículo (nuevo, excelente, bueno, etc.).
- **Comparación de Precios entre Fabricantes**: Permite seleccionar dos fabricantes y comparar sus distribuciones de precios. Incluye opción para vista normalizada (porcentajes).

## Instalación

1. Clona o descarga este repositorio.
2. Instala las dependencias. Tienes dos opciones:

### Opción 1: Usando Conda (recomendado)
```bash
conda env create -f environment.yml
conda activate vehiculos_env
```

### Opción 2: Usando pip
Asegúrate de tener Python 3.7+ instalado, luego:
```bash
pip install -r requirements.txt
```

## Uso

1. Ejecuta el notebook `notebooks/EDA.ipynb` para procesar y limpiar los datos (esto genera `vehicles_us_clean.csv`).
2. Ejecuta la aplicación:

```bash
streamlit run app.py
```

3. Abre tu navegador en la URL proporcionada por Streamlit (generalmente `http://localhost:8501`).

## Datos

La aplicación utiliza un dataset de anuncios de venta de vehículos usados. Los datos incluyen información como precio, año del modelo, fabricante, condición, etc.

- **Fuente de datos**: `vehicles_us.csv` (archivo original)
- **Datos procesados**: `notebooks/vehicles_us_clean.csv` (generado por el notebook de limpieza)

## Requisitos

- Python 3.7+
- Streamlit
- Pandas
- Plotly
- Scipy

## Estructura del Proyecto

```
proyecto_7/
├── app.py                 # Aplicación principal de Streamlit
├── environment.yml        # Especificaciones del entorno Conda
├── notebooks/
│   └── EDA.ipynb         # Notebook de análisis exploratorio y limpieza de datos
├── src/
│   └── funciones_personales.py  # Funciones auxiliares
├── requirements.txt       # Dependencias de Python
├── vehicles_us.csv        # Dataset original
└── README.md             # Este archivo
```

## Desarrollo

Este proyecto forma parte del bootcamp de análisis de datos, demostrando habilidades en:
- Limpieza y transformación de datos con Pandas
- Visualización interactiva con Plotly
- Desarrollo de aplicaciones web con Streamlit
- Análisis exploratorio de datos

## Contribución

Si deseas contribuir, por favor:
1. Haz un fork del repositorio
2. Crea una rama para tu feature
3. Envía un pull request

## Licencia

Este proyecto es para fines educativos.

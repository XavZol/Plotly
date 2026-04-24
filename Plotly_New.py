import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import dash 
from dash import dcc, html
import streamlit as st
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    "Fruta": ["Manzanas", "Naranjas", "Bananas", "Manzanas", "Naranjas", "Bananas"],
    "Cantidad": [4, 1, 2, 2, 4, 5],
    "Ciudad": ["BG", "BG", "BG", "BCN", "BCN", "BCN"]
})

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Definir el layout de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Dashboard Interactivo Avanzado'),
    
    dcc.Dropdown(
        id='desplegable',
        options=[
            {'label': 'Bogotá', 'value': 'BG'},
            {'label': 'Barcelona', 'value': 'BCN'}
        ],
        value='BG'
    ),
    
    dcc.Graph(id='grafico')
])

# Callback para actualizar el gráfico basado en la selección del dropdown
@app.callback(
    Output('grafico', 'figure'),
    [Input('desplegable', 'value')]
)
def actualizar_grafico(ciudad_seleccionada):
    df_filtrado = df[df['Ciudad'] == ciudad_seleccionada]
    fig = px.bar(df_filtrado, x='Fruta', y='Cantidad', color='Fruta')
    return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)


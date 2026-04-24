import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import dash 
from dash import dcc, html
import streamlit as st
import numpy as np

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hola Dash'),
    html.Div(children='Este es un subtítulo'),
    dcc.Graph(id='grafico-ejemplo',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Bogotá'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Buenos Aires',}
                    ],
                    'layout': {'title': 'Visualización con Dash'}
                })
])

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    dcc.Input(id='caja-texto', type='text', value=''),
    html.Button('Enviar', id='boton'),
    html.Div(id='salida-boton', children='')
])

@app.callback(
    dash.Output('salida-boton', 'children'),
    [dash.Input('boton', 'n_clicks')],
    [dash.State('caja-texto', 'value')])
def actualizar_salida(n_clicks, valor):
    if n_clicks == None:
        return 'Introduzca un valor y presione el boton'
    else:
        return f'El valor ingresado es {valor}, el botón fue presionado {n_clicks} veces'

if __name__ == '__main__':
    app.run(debug=True)

# dcc.Graph(figure=fig)
# st.plotly_chart()

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
from dash import dcc
import streamlit as st
import numpy as np

fig = go.Figure(data=[go.Scatter3d(x=[1, 2, 3, 4, 5],
                                    y=[10, 11, 12, 13, 14],
                                    z=[5, 6, 7, 8, 9],
                                    mode='markers',
                                    marker=dict(size=10,
                                                color=[10, 20, 30, 40, 50],
                                                colorscale='viridis',
                                                opacity=0.8))])

fig.update_layout(title='Gráfico en 3D',
                    scene=dict(xaxis_title='Eje X',
                                yaxis_title='Eje Y',
                                zaxis_title='Eje Z'))

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='viridis')])

fig2 = go.Figure(data=[go.Scatter3d(x=[1, 2, 3, 4, 5],
                                    y=[10, 11, 12, 13, 14],
                                    z=[5, 6, 7, 8, 9],
                                    mode='lines',
                                    line=dict(color="blue",
                                                width=2))])

fig2.update_layout(title='Gráfico de líneas en 3D',
                    scene=dict(xaxis_title='Eje X',
                                yaxis_title='Eje Y',
                                zaxis_title='Eje Z'))

fig.write_image("grafico.png")
dcc.Graph(figure=fig)
st.plotly_chart(fig)
st.plotly_chart(fig2)

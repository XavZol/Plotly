import plotly.graph_objects as go
import plotly.figure_factory as ff
from dash import dcc
import streamlit as st


fig = go.Figure()

fig.add_trace(go.Bar(x=[1, 2, 3, 4, 5],
                    y=[17, 10, 14, 15, 18],
                    name='barras'))

fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5],
                        y=[16, 12, 11, 18, 19],
                        mode='lines',
                        name='linea'))

layout = go.Layout(title='Gráfico Personalizado',
                xaxis_title='Eje X',
                yaxis_title='Eje Y')

fig.update_layout(layout)

fig.update_traces(
    selector=dict(name='linea'),
    line=dict(color='firebrick', width=4))

fig.update_traces(
    selector=dict(name='barras'),
    marker=dict(color='lightgreen'))

fig.update_layout(bargap=0.4)

fig.update_layout(
    title=dict(
        text='Este es mi gráfico<br><sup>Subtítulo del Gráfico</sup>',
        font=dict(size=24, color='purple', family='Times New Roman'),
        x=0.5,
        xanchor='center'))

# Títulos de Ejes
fig.update_layout(
    xaxis_title=dict(font=dict(size=18, color='blue', family='Courier New')),
    yaxis_title=dict(font=dict(size=18, color='green', family='Courier New')))

fig.update_layout(
    plot_bgcolor='rgba(123, 65, 78, 0.5)', 
    paper_bgcolor='lightblue')

fig.add_annotation(
    x=2,
    y=12,
    text="Punto Clave",
    showarrow=True,
    arrowhead=5,
    ax=20,
    ay=-30)

fig.add_annotation(
    x=3,
    y=14,
    text="Otro Punto Clave",
    showarrow=True,
    arrowhead=2,
    ax=-50,
    ay=-50,
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#ffffff"),
    align="center",
    arrowcolor="#45e6aa",
    arrowsize=1,
    arrowwidth=2,
    bordercolor="#45e6aa",
    borderwidth=2,
    borderpad=4,
    bgcolor="#666aef",
    opacity=0.5)

fig.update_traces(
    selector=dict(name='linea'),
    text=['A', 'B', 'C', 'D', 'E'],
    hoverinfo='text')

fig.update_traces(
    selector=dict(name='linea'),
    text=['A', 'B', 'C', 'D', 'E'],
    hovertemplate='X: %{x}<br>Y: %{y}<br>Texto: %{text}<extra>Info</extra>')

fig.write_image("grafico.png")
dcc.Graph(figure=fig)
st.plotly_chart(fig)
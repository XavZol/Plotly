import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
from dash import dcc
import streamlit as st

fig = make_subplots(rows=2, cols=2)

plot1 = go.Scatter(x=[1, 2, 3],
                y=[4, 5, 6],
                mode='lines+markers',
                name='Plot 1')
fig.add_trace(plot1, row=1, col=1)

plot2 = go.Bar(x=['A', 'B', 'C'],
            y=[7, 8, 9],
            name='Plot 2')
fig.add_trace(plot2, row=1, col=2)

plot3 = go.Scatter(x=[1, 2, 3],
                y=[2, 3, 4],
                mode='markers',
                name='Plot 3')
fig.add_trace(plot3, row=2, col=1)

plot4 = go.Bar(x=['X', 'Y', 'Z'],
            y=[1, 3, 2],
            name='Plot 4')
fig.add_trace(plot4, row=2, col=2)

fig.update_layout(title="Subplots Básicos",
                    showlegend=False)

fig2 = make_subplots(rows=2, cols=2, shared_xaxes=True, shared_yaxes=True)
fig2.add_trace(plot1, row=1, col=1)
fig2.add_trace(plot2, row=1, col=2)
fig2.add_trace(plot3, row=2, col=1)
fig2.add_trace(plot4, row=2, col=2)
fig2.update_layout(title="Subplots con ejes compartidos",
                    showlegend=False)

df = px.data.iris()
df2 = px.scatter(df,
            x='sepal_width',
            y='sepal_length',
            color='species',
            facet_col='species',
            title='Gráfico Facetado por Especie')

fig.write_image("grafico.png")
dcc.Graph(figure=fig)
st.plotly_chart(fig)
st.plotly_chart(fig2)
st.plotly_chart(df2)
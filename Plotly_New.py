import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
from dash import dcc
import streamlit as st

fig = go.Figure(go.Scattergeo(lon=[-3.7, -99.1, -77.0],
                                lat=[40.4, 19.4, -12.0],
                                text=["Madrid", "México DF", "Lima"],
                                mode='markers'))
fig.update_layout(title='Mapa Básico de Puntos',
                    geo_scope='world') # south america

fig2 = go.Figure(go.Scattergeo(lon=[-3.7, -99.1, -77.0],
                                lat=[40.4, 19.4, -12.0],
                                text=["Madrid", "México DF", "Lima"],
                                mode='markers',
                                marker=dict(size=[16, 44, 48],
                                            color=[10, 20, 30],
                                            colorscale='Viridis',
                                            showscale=True)))

df = px.data.gapminder()
df.head()

fig3 = px.choropleth(df, 
                        locations='iso_alpha',
                        color='lifeExp',
                        hover_name='country',
                        color_continuous_scale=px.colors.sequential.Plasma,
                        animation_frame='year')

fig.write_image("grafico.png")
dcc.Graph(figure=fig)
st.plotly_chart(fig)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
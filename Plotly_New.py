import pandas as pd
import plotly.graph_objects as go 
import plotly.express as px
import dash
from dash import dcc, html
import streamlit as st

ruta = r"C:\Users\javie\OneDrive\Desktop\Excel_DB\earthquake+data.csv"
df = pd.read_csv(ruta)

df['Date & Time'] = pd.to_datetime(df['Date & Time'])

fig1 = px.choropleth(df,
                    locations="Country",
                    locationmode='country names',
                    color="Magnitude",
                    hover_name="Country",
                    projection="natural earth")
fig1.update_layout(title="Mapa Global de Terremotos según Magnitud")

# Gráfico de barras
magnitudes = df['Magnitude'].value_counts().sort_index()
fig2 = go.Figure(go.Bar(x=magnitudes.index,
                        y=magnitudes.values,
                        marker=dict(
                            color=magnitudes.values,
                            colorscale='viridis',
                            showscale=True,
                            colorbar=dict(title="Número de Terremotos")),
                        text=magnitudes.values,
                        textposition='outside'))
fig2.update_layout(title="Número de Terremotos por Magnitud",
    xaxis=dict(title="Magnitud"),
    yaxis=dict(title="Número de Terremotos"))

# Gráfico de Líneas 
df.sort_values('Date & Time', inplace=True)

fig3 = go.Figure(
    go.Scatter(
        x=df['Date & Time'],
        y=df['Magnitude'],
        mode='lines',
        line=dict(color='royalblue', width=2),
        text=df['Magnitude'],
        textposition='top center'
    )
)

fig3.update_layout(
    title="Tendencia de Magnitud de Terremotos a lo Largo del Tiempo",
    xaxis_title="Fecha",
    yaxis_title="Magnitud"
)

# Gráfico de dispersión
fig4 = go.Figure(
    go.Scatter(
        x=df['Depth'],
        y=df['Magnitude'],
        mode='markers',
        marker=dict(
            size=10,
            color=df['Magnitude'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Magnitud")
        ),
        text=df['Magnitude'],
        hoverinfo='text+x+y'
    )
)

fig4.update_layout(
    title="Relación entre Magnitud y Profundidad de Terremotos",
    xaxis_title="Profundidad",
    yaxis_title="Magnitud"
)

# Gráfico 3D
fig5 = go.Figure(
    go.Scatter3d(
        x=df['Date & Time'],
        y=df['Depth'],
        z=df['Magnitude'],
        mode='markers',
        marker=dict(
            size=5,
            color=df['Magnitude'],
            colorscale='Viridis',
            opacity=0.8
        )
    )
)

fig5.update_layout(
    title="Relación 3D entre Magnitud, Profundidad y Tiempo",
    scene=dict(
        xaxis_title="Fecha",
        yaxis_title="Profundidad",
        zaxis_title="Magnitud"
    )
)

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Creación del layout general
app.layout = html.Div([
    html.H1("Dashboard de Terremotos"),

    dcc.Graph(
        id='mapa-coropleto',
        figure=fig1
    ),

    dcc.Graph(
        id='grafico-barras',
        figure=fig2
    ),

    dcc.Graph(
        id='grafico-lineas',
        figure=fig3
    ),

    dcc.Graph(
        id='grafico-dispersion',
        figure=fig4
    ),

    dcc.Graph(
        id='grafico-3d',
        figure=fig5
    )
])

if __name__ == '__main__':
    app.run(debug=True)


st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
st.plotly_chart(fig4)
st.plotly_chart(fig5)
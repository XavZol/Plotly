import pandas as pd
import numpy as np
import plotly.express as px # Usamos Express en lugar de Cufflinks
import streamlit as st

np.random.seed(42)
df = pd.DataFrame(np.random.randn(100, 2), columns=['A', 'B'])

# Plotly Express es el estándar actual
fig = px.line(df, 
            y=['A', 'B'], 
            markers=True, # Esto activa los 'markers' que pedías
            title='Gráfico Interactivo con Plotly Express')

st.plotly_chart(fig)


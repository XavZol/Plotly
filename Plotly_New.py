import plotly.graph_objects as go

fig = go.Figure()

mi_trazado = go.Scatter(x=[1, 2, 3, 4, 5],
                        y=[10, 11, 12, 13, 14],
                        mode='markers')

fig.add_trace(mi_trazado)


mi_trazado = go.Scatter(x=[1, 2, 3, 4, 5],
                        y=[10, 11, 12, 13, 14],
                        mode='markers',
                        marker=dict(size=12,
                                    color='rgba(255, 0, 0, 0.8)'),
                                    line=dict(width=2,
                                                color='DarkSlateGrey'))
fig.update_traces(mi_trazado)

mi_layout = go.Layout(title='Ejemplo de gráfico con Plotly',
                        xaxis=dict(title='Eje de las X'),
                        yaxis=dict(title='Eje de las Y'))

fig.update_layout(mi_layout)


trazado_barras = go.Bar(x=[1, 2, 3, 4, 5],
                            y=[5, 10, 12, 7])
fig.add_trace(trazado_barras)

# Guardar el gráfico como archivo HTML
fig.write_html("grafico.html")
print("Gráfico guardado como 'grafico.html'. Ábrelo en tu navegador.")


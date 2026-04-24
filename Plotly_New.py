import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5],
                        y=[10, 15, 12, 17, 14],
                        mode='lines',
                        name='Linea'))

fig2 = go.Figure()
fig2.add_trace(go.Bar(x=[1, 2, 3, 4, 5],
                        y=[5, 6, 7, 8, 9],
                        marker=dict(color='rgba(0, 128, 255, .6)',
                                    line=dict(color='rgb(0, 0, 0)',
                                                width=1.5))))
fig2.update_layout(title='Gráfico de Barras',
                    xaxis_title='Eje X',
                    yaxis_title='Eje Y')

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=[1, 2, 3, 4, 5],
                        y=[10, 15, 12, 17, 14],
                        mode='lines',
                        fill='tozeroy',
                        name='area'))
fig3.update_layout(title='Gráfico de Area',
                    xaxis_title='Eje X',
                    yaxis_title='Eje Y')

fig4 = go.Figure()
fig4.add_trace(go.Pie(labels=['A', 'B', 'C', 'D'],
                        values=[4500, 2500, 1050, 750]))
fig4.update_layout(title='Gráfico de Circular')

data = go.Histogram(x=[1, 2, 2, 3, 3, 3, 4])

fig5 = go.Figure(data=data)
fig5.update_layout(title='Histograma')

fig5.write_html("grafico.html")
print("Gráfico guardado como 'grafico.html'. Ábrelo en tu navegador.")

import plotly.graph_objects as go
import plotly.figure_factory as ff

z = [[1, 20, 30],
        [20, 1, 60],
        [30, 60, 1]]

fig = go.Figure(data=go.Heatmap(z=z))

fig.update_layout(title='Mapa de Calor')

fig2 = go.Figure(data=go.Box(y=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
fig2.update_layout(title='Gráfico de Caja')

fig3 = go.Figure(data=go.Scatter(x=[1, 2, 3, 4, 5],
                                    y=[10, 15, 13, 17, 14],
                                    mode='lines+markers'))
fig3.update_layout(title='Gráfico de Dispersión con Líneas')

y0 = [2, 3, 4, 5, 6, 7 , 8, 9]
y1 = [3, 4, 5, 6, 7 , 8, 9, 10]

fig4 = go.Figure()
fig4.add_trace(go.Violin(y=y0,
                            name='y0',
                            box_visible=True,
                            meanline_visible=True))
fig4.add_trace(go.Violin(y=y1,
                            name='y1',
                            box_visible=True,
                            meanline_visible=True))
fig4.update_layout(title='Gráfico de Violín')

df = [dict(Task='Tarea A', Start='2024-01-01', Finish='2024-01-05'),
        dict(Task='Tarea B', Start='2024-01-06', Finish='2024-01-10')]
fig5 = ff.create_gantt(df)
fig5.update_layout(title='Gráfico de Gantt')

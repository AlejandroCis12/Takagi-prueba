import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc  # Importa Dash Bootstrap Components
from dash import Dash, html, Output, Input, State, no_update
import funcion_modificada 
from funcion_modificada import j_newton, T
import plotly.graph_objects as go

### Componentes de Dash Bootstrap
solicitar_a = html.Div(
    [
        html.P("Tome un numero para a entre 0 a 1", style={'color': 'white'}),
        dbc.Input(type="number", min=0, max=1, step="any",
                  value="0.38", id="a-input"),
    ],
)

solicitar_x0 = html.Div(
    [
        html.P("Tome un numero para x_0 entre 0 y 0.5", style={'color': 'white'}),
        dbc.Input(type="number", min=0, max=0.5, step="any",
                  value="0.2", id="x0-input"),
    ],
)

interaciones = html.Div(
    [
        html.P("Coloque el numero de iteraciones", style={'color': 'white'}),
        dbc.Input(type="number", min=0, max=2025, step="any",
                  value="500", id="iteraciones-input"),
    ],
)



insertar = dbc.Row([
    dbc.Col(
        children=solicitar_a,
        width=4, 
        xs=12, sm=12, md=4, lg=4, xl=4, xxl=4,
        style={'backgroundColor': '#000', 'padding': '0', 'margin': '0'}
    ),
    dbc.Col(
        children=solicitar_x0,
        width=4, 
        xs=12, sm=12, md=4, lg=4, xl=4, xxl=4,
        style={'backgroundColor': 'rgb(157, 36, 73)', 'padding': '0', 'margin': '0'}
    ),
        dbc.Col(
        children=interaciones,
        width=4, 
        xs=12, sm=12, md=4, lg=4, xl=4, xxl=4,
        style={'backgroundColor': '#000', 'padding': '0', 'margin': '0'}
    ),
],
    style={"height": "24vh", 'width': '100vw', 'padding': '0', 'margin': '0'}
)

grafica =  dbc.Row([
    dbc.Col(
        children= dcc.Graph(figure= go.Figure(), id="grafica", config={'scrollZoom': True}, style={'height': '76vh', 'width': '100vw', 'padding': '0', 'margin': '0'}),
        width=12, 
        #xxl=3, xl=3, lg=3, md=3, sm=3, xs=3,
        style={'backgroundColor': 'rgb(135, 206, 235)', 'padding': '0', 'margin': '0'}
    ),
],
    style={"height": "76vh", 'width': '100vw', 'padding': '0', 'margin': '0'}
)


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    insertar,
    grafica
],
    style={'height': '100vh', 'width': '100vw', 'padding': '0', 'margin': '0'}
)




#### Callbacks

@app.callback(
    [Output("grafica", "figure")],
    [Input("a-input", "value"),
     Input("x0-input", "value"),
     Input("iteraciones-input", "value")],
    #prevent_initial_call=True  # evita que el callback se dispare al cargar
)
def calcular_j_newton(a,x0, iteraciones):
    figura = funcion_modificada.j_newton(
        fun=funcion_modificada.T,
        a=float(a),
        x0=float(x0),
        tol=1e-5,
        nmax=float(iteraciones)
    )
    return  [figura]




if __name__ == '__main__':
    app.run(debug=True)

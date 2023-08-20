from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import service

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#F5F5F5",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Cuisine", className="display-4"),
        html.Hr(),
        html.P(
            "Choose your cuisine country", className="lead"
        ),
        html.Div([
            dcc.Dropdown(['Nigerian', 'Indian', 'Italian', 'Mexican','American'], placeholder="Pick a cuisine", id='demo-dropdown'),
        ]),
    ],
    style=SIDEBAR_STYLE,
)


content = html.Div(
    [
        html.H1("Resturant Name Generator"),
        html.Div([
            html.H3(id='dd-resturant-name'),
            html.Div(
                className="trend",
                children=[
                    html.P('Menu Items'),
                    html.Ul(id='dd-menu-items'),
                ]
            )]),
        ],id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@callback(
    Output('dd-resturant-name', 'children'),
    Output('dd-menu-items', 'children'),
    Input('demo-dropdown', 'value')
)


def output_update(value):
    if value:
        response = service.generate_res_name_item(cuisine=value)
        name = response['resturant_name'].strip().lstrip('resturant.')
        items = response['menu_items'].strip().split(',') 
    else:
        name = "Choose a cuisine to get a name"
        items = ["Choose a cuisine to get menu items"]
    return name, [html.Li(item) for item in items]

if __name__ == '__main__':
    app.run(debug=True)
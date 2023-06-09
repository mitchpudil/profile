import dash
from dash import html
import dash_bootstrap_components as dbc


LAYOUT = html.Div(
    [
        html.Div(
            [
                html.Img(
                    src='assets/ocean.jpg',
                    style={'width': '100%'}
                ),
                html.Div([
                    html.H4("I am"),
                    html.H1(html.B('Mitchell Pudil')),
                    html.P('Comtemplative coder and data scientist. Inspired by tough problems.'),
                    dbc.Button(
                        "MY PROJECTS",
                        className="gradient-button",
                        color="primary",
                        style={"font-size": "18px", "padding": "12px 20px"},
                        href='/portfolio'
                        )
                    ],
                    style={
                        'position': 'absolute',
                        'top': '25%',
                        'left': '50%',
                        'transform': 'translate(-50%, -50%)',
                        'font-size': '20px',
                        'color': 'white',
                        'text-shadow': '2px 2px 4px #000000',
                        'text-align': 'center'
                    }
                )
            ],
            style={'position': 'relative'}
        )
    ]
)

def add_callbacks(app: dash.Dash):
    pass

import warnings

# Ignore warnings from Dash about dcc and html
warnings.simplefilter("ignore", UserWarning)

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

import tabs

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.FLATLY, "./assets/css/stylesheet.css",
                                      "./assets/css/timeline.css"],
                title="Mitch Pudil",
                update_title="Loading...")

server = app.server

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "min(18rem, 30%)",
    "padding": "4rem 1rem 2rem 3rem",  # Adjust the padding-left value
    "background-color": "#f2f5f7",
}


NAV_BUTTON_STYLE = {
    "max-width": "100%",
    "color": "#86c2db"
}

CONTENT_STYLE = {
    "margin-left": "min(18rem, 30%)",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background": "linear-gradient(to right, #383838 0%, #e9e9f2 50px)",
    "min-height": "100vh",
    "position": "relative"
}


FOOTER_STYLE = {
    "margin-left": "min(18rem, 30%)",
    "margin-right": "2rem",
    "padding-left": "1rem"
}

sidebar = html.Div(
    [
        html.A(html.H2("M. Pudil"),
               href="/",
               style={"text-decoration": "inherit", "color": "inherit"}),
        html.Hr(),
        dbc.Nav(
            [
                # Add links to any new pages here
                dbc.NavLink("HOME",
                            href="/",
                            active="exact",
                            style=NAV_BUTTON_STYLE),
                dbc.NavLink("ABOUT ME",
                            href="/about-me",
                            active="exact",
                            style=NAV_BUTTON_STYLE),
                dbc.NavLink("PORTFOLIO",
                            href="/portfolio",
                            active="exact",
                            style=NAV_BUTTON_STYLE),
                dbc.NavLink("PERCEPTION",
                            href="/portfolio/perception",
                            active="exact",
                            style={**NAV_BUTTON_STYLE, "paddingLeft": "4rem"}),
                dbc.NavLink("APHASIA",
                            href="/portfolio/aphasia",
                            active="exact",
                            style={**NAV_BUTTON_STYLE, "paddingLeft": "4rem"}),
                dbc.NavLink("PROJECT 3",
                            href="/portfolio/project3",
                            active="exact",
                            style={**NAV_BUTTON_STYLE, "paddingLeft": "4rem"}),
                dbc.NavLink("PROJECT 4",
                            href="/portfolio/project4",
                            active="exact",
                            style={**NAV_BUTTON_STYLE, "paddingLeft": "4rem"}),
                dbc.NavLink("PROJECT 5",
                            href="/portfolio/project5",
                            active="exact",
                            style={**NAV_BUTTON_STYLE, "paddingLeft": "4rem"}),
                dbc.NavLink("SCOUT",
                            href="/scout",
                            active="exact",
                            style=NAV_BUTTON_STYLE),
                dbc.NavLink("RESUME",
                            href="/resume",
                            active="exact",
                            style=NAV_BUTTON_STYLE),
            ],
            vertical=True,
            pills=True
        ),
    ],
    style=SIDEBAR_STYLE
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render_page(path):
    if path == "/":
        return tabs.homepage.LAYOUT
    elif path == "/resume":
        return tabs.resume.LAYOUT
    elif path == "/about-me":
        return tabs.about.LAYOUT
    elif path == "/portfolio":
        return tabs.portfolio.LAYOUT
    elif path == "/portfolio/perception":
        return tabs.perception.LAYOUT
    elif path == "/portfolio/aphasia":
        return tabs.aphasia.LAYOUT
    elif path == "/scout":
        return tabs.scout.LAYOUT
    else:
        return tabs.not_found.LAYOUT

# Add callbacks for each custom page here
tabs.homepage.add_callbacks(app)
tabs.aphasia.add_callbacks(app)
tabs.perception.add_callbacks(app)


if __name__ == "__main__":
    app.run_server(debug=True, port=5000)

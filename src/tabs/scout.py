import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

# Define the list of images
image_paths = [{"key": i, "src": f"assets/scout_pics/scout{i}.png"} for i in range(5)]
# Initialize the index of the displayed image
current_image_index = 0

# Function to create the layout based on the current image index
LAYOUT = html.Div(
        style={
            'display': 'flex',
            'flex-direction': 'row',
            'align-items': 'center',
            'height': '100vh',
        },
        children=[
            html.Div(
                style={'flex': '1', 'padding': '20px',},
                children=[
                    html.Div([
                        html.H1(html.B("Scout")),
                        html.P("The best dog on Earth since 2020.", style={'color': 'dark gray'})],
                        style={
                        'position': 'absolute',
                        'top': '50%',
                        'left': '35%',
                        'transform': 'translate(-50%, -50%)',
                        'font-size': '20px',
                        'text-align': 'center'
                        }
                    )
                ],
            ),
            html.Div(
                style={'flex': '1', 'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'},
                children=[
                    dbc.Carousel(
                        items=image_paths,
                        controls=False,
                        indicators=False,
                        interval=2000,
                        ride="carousel"
                    )
                ],
            ),
        ],
    )

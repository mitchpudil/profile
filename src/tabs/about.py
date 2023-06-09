import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import dcc

bio = dcc.Markdown("""Hi! I'm Mitchell, a data scientist located in Salt Lake City with an unwavering passion for turning raw data into meaningful insights.

I currently serve as a lead data scientist and data science manager at a software consulting firm for Meta where I lead a team in
crafting innovative solutions that drive real-world impact.

Beyond the world of data, I'm an avid bowler, having competed in national tournaments, and a skilled billiards player.
Comedy shows tickle my funny bone, and I find solace in the great outdoors, accompanied by my exuberant Golden Retriever.

Let's add a dash of fun to the data-driven universe together!""")

social_links = html.Footer([
                    html.A(
                        html.Img(id="github",
                                 src="assets/github-mark.png",
                                 style={'color': 'inheret', 'max-height': '50px'}),
                                 href="https://github.com/mitchpudil",
                                 target="_blank",
                                 rel="noopener noreferrer",
                    ),
                    dbc.Tooltip("Open my GitHub page in new tab",
                                target="github",
                                placement="top",
                                delay={"show": 0, "hide": 0}),
                    html.A(
                        html.Img(id="linkedin",
                                 src="assets/linkedin.png"),
                                 href="https://www.linkedin.com/in/mitchell-pudil",
                                 target="_blank",
                                 rel="noopener noreferrer",
                                 style={"color": "inherit", 'margin-left': '50px'}
                    ),
                    dbc.Tooltip("Open my LinkedIn page in new tab",
                                target="linkedin",
                                placement="top",
                                delay={"show": 0, "hide": 0}),
                ],
                style={'text-align': 'center'}
            )



# Define the list of images
image_paths = [{"key": i, "src": f"assets/mitch_pics/mitch{i}.png"} for i in range(9)]
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
                style={'flex': '1', 'padding': '20px', 'overflow-wrap': 'break-word'},
                children=[
                    html.Div([
                        html.Div(
                            style={
                                'max-width': '500px',
                                'margin': '0 auto',
                                'position': 'relative',
                                'top': '2vh',
                            },
                            children=[
                                html.H1(html.B("About Me"), style={'text-align': 'center'}),
                                html.Br(),
                                html.P(bio, style={'color': 'dark gray', 'text-align': 'left', 'font-size': '20px'}),
                            ],
                        ),
                        html.Br(),
                        social_links
                    ])
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

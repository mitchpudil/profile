import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import ALL, Input, Output, dcc, html

CONTENT_STYLE = {
            'position': 'absolute',
            'top': '50%',
            'left': '75%',
            'transform': 'translate(-50%, -50%)',
            "width": "600px",
            "height": "auto",
            'text-align': 'center'
        }

perception_video = html.Iframe(
                src="https://www.youtube.com/embed/Yj0VRObArv8?autoplay=1",
                width="700",
                height="400",
                title="Perception",
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share",
                style={
                    'position': 'absolute',
                    'top': '50%',
                    'left': '75%',
                    'transform': 'translate(-50%, -50%)',
                }
            )

bulbs_movie = html.Div(
    html.Video(src='../assets/perception/bulbs.mov', autoPlay=True, controls=True,
                        style={
                            'width': '20%',
                            'position': 'absolute',
                            'top': '50%',
                            'left': '75%',
                            'transform': 'translate(-50%, -50%)',
                        }),
)

images = ["../assets/perception/palette_generator.png",
          "../assets/perception/pipeline.png",
          "../assets/perception/color_description.png",
          "../assets/perception/palette_terms.png",
          "../assets/perception/image_extractor.png"
]

def make_image(src):
    return html.Img(
        id={"type": "image-carousel", "index": 0},
        src=src,
        style=CONTENT_STYLE
    )


IMAGES_VIDEOS = [
    perception_video,
    make_image(images[0]),
    make_image(images[1]),
    bulbs_movie,
    make_image(images[2]),
    make_image(images[3]),
    make_image(images[4]),
]


summary = """As the lead data scientist of a small, dedicated team, I spearheaded the development
of [Perception](https://www.perception.io/) by leveraging advanced deep learning techniques.

Through the utilization of complex
methods such as conditional variational autoencoders, transformer architectures, and multi-modal
embeddings, we crafted an innovative solution that revolutionizes the way designers choose brand colors.

Our meticulous implementation of these cutting-edge technologies enabled us to create a powerful platform
that effortlessly generates visually compelling color palettes based on user inputs.
"""

palette_generator = """Perception's main functionality is centered around the input of a word or phrase,
which serves as a creative inspiration for designers. Upon entering a term, the app generates multiple
color palettes that closely align with the essence and meaning of the given word.

This feature allows designers to visually represent concepts, emotions, or characteristics
through a harmonious selection
of colors. """

pipeline = """I'm currently involved in designing a pipeline based on survey results, user feedback, and website
interactions to improve the generative models related to Perception.

We've integrated various AWS services into our pipeline for seamless updates.
By automating the model update process using these services, we provide users with the latest advancements
while maintaining data integrity and robustness.
"""

bulbs = """I enhanced the Palette Generator tool for personal use by syncing it with my smart bulbs via an API.
Now, when I enter a word or phrase into the app, my kitchen lights change accordingly. The colors
from the generated palettes transform my kitchen, creating a captivating and immersive experience.
"""

descriptions = """To enhance the user experience, I added a feature that auto-generate descriptive texts for the
colors, palettes, and associated terms.

These descriptions provide additional context and inspire designers
to make informed decisions when selecting colors."""

palette_to_text = """Perception offers a convenient feature where users can input a color palette
(list of hexcodes) and instantly discover the top associated terms along with a percentage match.

This helps designers gain insights into the emotional and visual connections elicited by their chosen
colors, enabling informed decision-making and creative refinement."""


color_extractor = """As the lead developer for Perception, I spearheaded the creation of another powerful tool.
This feature allows users to extract a color palette from an image and instantly view the corresponding top
terms. By analyzing the colors present in the image, the app generates descriptive terms that best match the palette.

This feature enables designers to derive inspiration from images and translate them into meaningful color
choices, enhancing their creative process and facilitating effective visual communication."""

descriptions = {
    "Perception": summary,
    "Palette Generator": palette_generator,
    "Continuous Improvement Pipeline": pipeline,
    "Smart Bulb Sync": bulbs,
    "Auto-generated Descriptions": descriptions,
    "Palette to Text": palette_to_text,
    "Color Extractor": color_extractor
}

card_contents = [
    dbc.CardBody([
        html.H4(title, className="card-title"),
        dcc.Markdown(description)
    ])
    for title, description in descriptions.items()
]


NAV_BUTTONS = html.Div([
    html.Button("<", style={'font-size': '48px', 'border': 'none', 'background-color': "transparent"}, #"#e9e9f2"},
                n_clicks=0, id={'type': 'perception-back-button', 'index': 0}),
    html.Div(
        [html.Span(className='circle', id={'type': 'perception-circle', 'index': i}) for i in range(7)],
        style={'display': 'inline-block', 'margin-left': '10px'}
    ),
    html.Button(">", style={'font-size': '48px', 'border': 'none', 'background-color': "transparent"},
                n_clicks=0, id={'type': 'perception-forward-button', 'index': 0}),
], style={
    'position': 'absolute',
    'top': '85%',
    'left': '50%',
    'transform': 'translate(-50%, -50%)',
    'font-size': '20px',
    'text-align': 'center'
})


BANNER_STYLE = {
    "position": "absolute",
    "top": 0,
    "left": 0,
    "right": 0,
    "height": "auto",
    "background-color": "#16688c",
    "color": "white",
    "display": "flex",
    "flex-direction": "column",  # Add flex-direction: column for vertical stacking
    "justify-content": "center",
    "align-items": "center",
    "white-space": "normal",
    "padding": "10px",  # Add padding for spacing between lines
}


LAYOUT = html.Div(
    style={"display": "flex", "justify-content": "center", "align-items": "center", "flex-direction": "column"},
    children=[
        html.Div(
            style=BANNER_STYLE,
            children=[
                html.H2("Perception"),
                html.H4("I taught semi conductors what colors feel like")
            ],
        ),
        html.Div(
            style={"margin-top": "200px", "display": "flex", "flex-direction": "column", "align-items": "center"},
            children=[
                html.Div(
                    style={"display": "flex", "flex-direction": "row"},
                    children=[
                        dbc.Card(
                            id={"type": "perception-text-carousel-cards", "index": 0},
                            children=card_contents[0],  # Initial card content
                            className="carousel-card",
                            style={
                                    'background-color': '#e4e4f2',
                                    'position': 'absolute',
                                    'top': '50%',
                                    'left': '25%',
                                    'transform': 'translate(-50%, -50%)',
                                    'font-size': '20px',
                                    'text-align': 'center',
                                    "width": "500px",
                                    "height": "auto"
                                }
                        ),
                        html.Div(id={"type": "content-carousel", "index": 0})
                    ]
                )
            ]
        ),
    NAV_BUTTONS
    ],
)

def add_callbacks(app: dash.Dash):
    @app.callback(
        Output({"type": "content-carousel", "index": 0}, "children"),
        Output({"type": "perception-text-carousel-cards", "index": 0}, "children"),
        Output({'type': 'perception-circle', 'index': ALL}, 'style'),
        Input({'type': 'perception-back-button', 'index': 0}, "n_clicks"),
        Input({'type': 'perception-forward-button', 'index': 0}, "n_clicks"),
    )
    def select_slide(back_clicks, forward_clicks):
        total_pages = 7
        current_page = 0

        # Calculate the effective number of clicks
        effective_clicks = forward_clicks - back_clicks

        # Determine the target page based on effective clicks
        target_page = (current_page + effective_clicks) % total_pages

        circle_styles = []
        for i in range(total_pages):
            if i <= target_page:
                circle_styles.append({'background-color': 'black'})
            else:
                circle_styles.append({'background-color': 'white'})
        return IMAGES_VIDEOS[target_page], card_contents[target_page], circle_styles




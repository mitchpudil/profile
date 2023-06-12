import dash_bootstrap_components as dbc
from dash import html, dcc
from dash_iconify import DashIconify


def get_card(title, text, icon, *args, **kwargs):
    card_content = dbc.Card(
        [
            dbc.CardBody(
                [
                    DashIconify(icon=icon, width=45, *args, **kwargs),
                    html.Div(html.B(html.U(html.H4(title, id=title))), style={'margin-top': '30px'}),
                    dcc.Markdown(text, className="card-text", style={"color": "dark gray"}),
                    html.Div(id="card-click-area", style={"cursor": "pointer"})
                ]
            ),
        ],
        style={"width": "24rem", 'background-color': "#e4e4f2", "text-align": 'center', "border-width": "0px"},
    )

    return card_content

titles = ["Computer Vision", "Cloud Computing", "Natural Language Processing (NLP)",
          "Python Web Development", "Deep Learning", "Statistics"]

descriptions = {
    "Computer Vision": "I develop and implement advanced image processing algorithms and applications.",
    "Cloud Computing": "I leverage Python and AWS products to train and deploy deep learning models.",
    "Natural Language Processing (NLP)": "I analyze and extract meaningful insights from textual data",
    "Python Web Development": """I build custom web apps in Python to showcase data science capabilities
    and build surveys for data collection. *In fact, I built this entire portfolio with Dash!*
    (see code [here](https://github.com/mitchpudil/profile))""",
    "Deep Learning": "I leverage PyTorch to design, train, and deploy deep neural networks for tasks such as image classification, NLP, and computer vision.",
    "Statistics": "I apply statistical methods, with a focus on machine learning, to analyze data and build advanced predictive models."
}

# Deep Learning: Perception
# Computer Vision: Paint by numbers demo
# NLP: ChatGPT training OR Aphasia
# Python Web Development: Dash apps (like this one)
# Statistics: Aphasia OR replace with data visualization FFT
# Cloud Computing: S3, Emr, ECS


card_div = html.Div(
    className="card-container",
    children=[
        dbc.Row(
            [
                dbc.Col(
                    get_card(
                        title=titles[0],
                        text=descriptions[titles[0]],
                        icon="streamline:computer-screen-tv-movies-television-cathode-crt-tv-ray-tube-vintage-video",
                    ),
                    width="auto",
                ),
                dbc.Col(
                    get_card(
                        title=titles[1],
                        text=descriptions[titles[1]],
                        icon="tabler:cloud-computing",
                    ),
                    width="auto",
                ),
                dbc.Col(
                    get_card(
                        title=titles[2],
                        text=descriptions[titles[2]],
                        icon="heroicons:chat-bubble-bottom-center-text",
                    ),
                    width="auto",
                ),
            ],
            className="card-row",
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    get_card(
                        title=titles[3],
                        text=descriptions[titles[3]],
                        icon="carbon:application-web",
                    ),
                    width="auto",
                ),
                dbc.Col(
                    get_card(
                        title=titles[4],
                        text=descriptions[titles[4]],
                        icon="mdi:graph-outline",
                        rotate=3
                    ),
                    width="auto",
                ),
                dbc.Col(
                    get_card(
                        title=titles[5],
                        text=descriptions[titles[5]],
                        icon="icomoon-free:stats-dots",
                    ),
                    width="auto",
                ),
            ],
            className="card-row",
        ),
    ]
)

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
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H1("Areas of Interest", style={"font-weight": "bold", "margin-top": '20px'}),
                        html.P("Take a look at some of the things I love working on."),
                    ],
                    style=BANNER_STYLE,
                )
            ],
            style={"text-align": "center", "font-size": "20px"},
        ),
        card_div,
    ]
)


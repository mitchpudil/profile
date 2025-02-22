import dash_html_components as html
#from pdf2image import convert_from_path
import dash_bootstrap_components as dbc
import base64
from dash import dcc
from dash_iconify import DashIconify

#from dash_iconify import DashIconify
#DashIconify(icon="uil:university", width=20, style={'margin-bottom': '12px', 'margin-right': '5px'}),

# Convert PDF to images
# pdf_path_display = 'assets/Resume_No_Links.pdf'
# images = convert_from_path(pdf_path_display)

pdf_path_download = 'assets/Mitchell_Pudil_Resume.pdf'

# # Function to encode PDF file
def encode_pdf():
    with open(pdf_path_download, 'rb') as file:
        encoded_pdf = base64.b64encode(file.read()).decode('utf-8')
    return encoded_pdf

download_image_button = dbc.Button(
    DashIconify(icon="formkit:downloadcloud", width=48),
    id="download-resume",
    className='resume-button',
    href=f"data:application/pdf;base64,{encode_pdf()}",
    download="Mitchell_Pudil_Resume.pdf",
    style={'background-color': "#16688c", "border": "none", "display": "flex", "flex-direction": "row"}
)

# Create the layout

def add_badges(badges_list):
    return html.P([dbc.Badge(badge, className="ms-1") for badge in badges_list], style={'margin-top': '10px'})

BANNER_STYLE = {
    "position": "absolute",
    "top": 0,
    "left": 0,
    "right": 0,
    "height": "auto",
    "background-color": "#16688c",
    "color": "white",
    "display": "flex",
    "flex-direction": "row",  # Add flex-direction: column for vertical stacking
    "justify-content": "center",
    "align-items": "center",
    "white-space": "normal",
    "padding": "10px",  # Add padding for spacing between lines,
}


LAYOUT = html.Div(
    style={'text-align': 'center'},
    children=[
        html.Div([
            html.H1("My Experience", style={"font-weight": "bold"}),
            download_image_button,
            dbc.Tooltip("Download Full Resume (pdf)", target="download-resume", placement="top",
                       delay={"show": 0, "hide": 0})
            ],
            style=BANNER_STYLE
            ),
        html.Div([
            html.Ul(
                children=[
                    html.Li(
                        style={"--accent-color": "#41516C", 'text-align': 'center'},
                        children=[
                            html.Div("June 2019", className="date"),
                            html.Div("B.S. Statistics, B.S. Economics, Math Minor", className="title"),
                            html.Div([
                                dcc.Markdown(
                                    """
                                    Brigham Young University

                                    **GPA**: 3.93/4.00
                                    """
                                ),
                                add_badges(["Machine Learning", "Econometrics", "Statistics",
                                            "Research Assistant", "Behavioral Economics",
                                            "Teaching Assistant"])
                            ], className="descr")
                        ]
                    ),
                    html.Li(
                        style={"--accent-color": "#FBCA3E"},
                        children=[
                            html.Div("May 2019 - August 2019", className="date"),
                            html.Div("Data Science Intern", className="title"),
                            html.Div([
                                dcc.Link("OrderBoard", href="https://www.orderboard.ai/"),
                                add_badges(["AWS", "R", "MySQL"])
                                ],
                                className="descr"
                                ),
                        ]
                    ),
                    html.Li(
                        style={"--accent-color": "#E24A68"},
                        children=[
                            html.Div("May 2020", className="date"),
                            html.Div("Master’s in Data Science: Statistical Practice Emphasis", className="title"),
                            html.Div([
                                html.P("Carnegie Mellon University", style={'margin-bottom': '5px'}),
                                dcc.Link("(Ranked #5 in Statistics)", href="https://www.usnews.com/best-graduate-schools/top-science-schools/statistics-rankings", 
                                         style={"font-size": "16px"}),
                                dcc.Markdown("**GPA**: 4.00/4.00", style={'margin-top': '15px'}),
                                add_badges(["Forecasting", "Machine Learning", "Python", "R", "Statistics", "Coauthor"])
                                ],
                                className="descr",
                            ),
                        ],
                    ),
                    html.Li(
                        style={"--accent-color": "#1B5F8C"},
                        children=[
                            html.Div("May 2020 - May 2021", className="date"),
                            html.Div("Data Scientist", className="title"),
                            html.Div([
                                dcc.Link("Codazen", href="https://www.codazen.com/"),
                                add_badges(["Deep Learning", "Computer Vision", "Recommendation Engines", "NLP", "AWS",
                                            "Pytorch", "Python", "Python Web Development"])
                                ],
                                className="descr"
                            ),
                        ],
                    ),
                    html.Li(
                        style={"--accent-color": "#4CADAD"},
                        children=[
                            html.Div("May 2021 - Present", className="date"),
                            html.Div("Lead Data Scientist & Data Science Manager", className="title"),
                            html.Div([
                                dcc.Link("Codazen", href="https://www.codazen.com/"),
                                add_badges(["Leadership", "Hiring", "Cloud Computing", "Generative Models", "API Deployment", "Client Meetings",
                                            "Point of Contact", "Team Building"])
                                ],
                                className="descr",
                            ),
                        ],
                    ),
                ],
            ),
        ], style={"margin-top": "200px", "font-size": '20px'}
    )
])

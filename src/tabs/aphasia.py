import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import ALL, Input, Output, dcc, html

abstract = """At Carnegie Mellon University in 2019-2020, I co-authored
[Enhancing the classification of aphasia: a statistical analysis using connected speech](https://pubmed.ncbi.nlm.nih.gov/36457942/) for the journal _Aphasiology_.

For this project I used a combination of machine learning algorithms to improve the classification
system of aphasia based on patterns in the language used by individuals with aphasia in an effort to improve predictions of patient recovery and interventions."""

analysis = """Before considering a new aphasia classification scheme with the language discourse data, I first took a look at the
distributions of various scores of tests popularly used in determining the current class of aphasia for an individual. 

Several of the metrics from
the tests significantly overlapped across aphasia type, even when looking at multiple scores simultaneously. This suggested that individuals
with different diagnoses may in reality exhibit similar attributes."""

kmeans = """In order to discover new classes of aphasia based on patterns and traits of language produced by the patients with aphasia,
I applied a modified version of the K-means algorithm on the language discourse data set.

The groups that resulted were immediately intuitive to the
psychology professor who had been studying aphasia for years. The groups were effectively chosen based on repetitions, revisions, paraphasias, fillers, and sound fragments."""

random_forest = """I used random forests based on multiple K-means models (K = 6, 7, and 8) to determine the importance of each feature.
By analyzing the averages of these random forests, we identified consistent feature importance rankings, which helped us understand the underlying
data structure and identify key variables driving the clustering patterns.

This approach provided a comprehensive evaluation of feature importance and supported data-driven decision-making."""

decision_tree = """To simplify the usage of the K-means algorithm for clinicians, I developed a decision tree based on the most effective K-means model.
The decision tree achieved a 91% similarity score, indicating its suitability as a replacement for the K-means model.

With its straightforward structure, the decision tree serves as a valuable tool for clinicians to reclassify aphasia, providing an
easier and more accessible method compared to directly using the K-means algorithm.

We also found that the majority of the tests currently conducted to determine aphasia type was redundant, as there were only two
measures (narrative and everyday discourse) that were used to create the decision tree."""

comparison = """After creating the decision tree, we compared the new classes to the original classes. Unsurprisingly, we found a fairly substantial
difference in the grouping, though there were a couple of new groups that appeared to largely be comprised of just a couple of the original groups.

Overall, this publication was the first to suggest a new classification system for aphasia using modern machine learning and data-driven techniques."""



images = ["../assets/aphasia/brain0.png",
          "../assets/aphasia/EDA0.png",
          "../assets/aphasia/kmeans0.png",
          "../assets/aphasia/RF0.png",
          "../assets/aphasia/DT0.png",
          "../assets/aphasia/compare0.png"
]

card_contents = [
    dbc.CardBody([
        html.H4("Summary", className="card-title"),
        dcc.Markdown(abstract),
    ]),
    dbc.CardBody([
        html.H4("Exploratory Data Analysis", className="card-title"),
        dcc.Markdown(analysis),
    ]),
    dbc.CardBody([
        html.H4("K-means", className="card-title"),
        dcc.Markdown(kmeans),
    ]),
    dbc.CardBody([
        html.H4("Random Forest", className="card-title"),
        dcc.Markdown(random_forest),
    ]),
    dbc.CardBody([
        html.H4("Decision Tree", className="card-title"),
        dcc.Markdown(decision_tree),
    ]),
    dbc.CardBody([
        html.H4("Comparison", className="card-title"),
        dcc.Markdown(comparison),
    ]),
]


NAV_BUTTONS = html.Div([
    html.Button("<", style={'font-size': '48px', 'border': 'none', 'background-color': "#e9e9f2"}, n_clicks=0, id={'type': 'back-button', 'index': 0}),
    html.Div(
        [html.Span(className='circle', id={'type': 'circle', 'index': i}) for i in range(6)],
        style={'display': 'inline-block', 'margin-left': '10px'}
    ),
    html.Button(">", style={'font-size': '48px', 'border': 'none', 'background-color': "#e9e9f2"}, n_clicks=0, id={'type': 'forward-button', 'index': 0}),
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
                html.H2("Reclassification of Aphasia"),
                html.H4("How I used machine learning and statistics to redefine the way clinicians understand Aphasia"),
            ],
        ),
        html.Div(
            style={"margin-top": "200px", "display": "flex", "flex-direction": "column", "align-items": "center"},
            children=[
                html.Div(
                    style={"display": "flex", "flex-direction": "row"},
                    children=[
                        dbc.Card(
                            id={"type": "text-carousel-cards", "index": 0},
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
                        html.Img(
                            id={"type": "image-carousel", "index": 0},
                            style={
                                'position': 'absolute',
                                'top': '50%',
                                'left': '75%',
                                'transform': 'translate(-50%, -50%)',
                                "width": "700px",
                                "height": "auto",
                                'text-align': 'center'
                            }
                        ),
                    ]
                )
            ]
        ),
    NAV_BUTTONS
    ],
)

def add_callbacks(app: dash.Dash):
    @app.callback(
        Output({"type": "image-carousel", "index": 0}, "src"),
        Output({"type": "text-carousel-cards", "index": 0}, "children"),
        Output({'type': 'circle', 'index': ALL}, 'style'),
        Input({'type': 'back-button', 'index': 0}, "n_clicks"),
        Input({'type': 'forward-button', 'index': 0}, "n_clicks"),
    )
    def select_slide(back_clicks, forward_clicks):
        total_pages = 6
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

        return images[target_page], card_contents[target_page], circle_styles

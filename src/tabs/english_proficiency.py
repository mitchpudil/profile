import dash
from dash import Input, Output, State, dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from english_proficiency_r import english_proficiency as ep

# Initialize the Dash app
app = dash.Dash(__name__)

with open("english_proficiency_r/example_submission.txt", 'r') as file:
    EXAMPLE_TEXT = file.read().replace('\n', ' ')


# Define the layout of the Dash app
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


LAYOUT = html.Div([
    html.Div(
        style=BANNER_STYLE,
        children=[
            html.H2("English as a Foreign Language Exam Prep"),
            html.H4("I developed an auto-grader for the TOEFL exam using NLP. Try the tool out below!")
            ],
    ),
    html.Div(children=[
        dcc.Markdown("""
        ### Instructions:

        1. Answer the following prompt by writing in the text area below (or choose your own prompt).
        2. Click "Grade" to see your score and how you can improve.
        3. Alternatively, click "Grade Placeholder" to grade a sample response.

        Example Prompt: Why is it more important for students to understand ideas and concepts rather than just learn facts? """),
        dbc.Textarea(id={'type': 'ep-input', 'index': 0}, size='lg', placeholder=EXAMPLE_TEXT, style={'height': '300px'}),
        html.Div(id={'type': 'toefl-modal', 'index': 0}),
        html.Br(),
        dbc.Button('Grade', id={'type': 'toefl-run-button', 'index': 0}),
        dbc.Button('Grade Placeholder', id={'type': 'toefl-grade-placeholder', 'index': 0}, style={'margin-left': '10px'}),
        html.Br(),
        dcc.Loading(html.Div(id={"type": 'toefl-output-div', "index": 0}), type="dot")
    ], style={'width': '80%', 'margin-left': '10%', "margin-top": "100px", 'font-size': '20px'})
])

def text_to_div(text):
    pred, pos_cols, english = ep.text2pred(text)
    figs = ep.get_figs(pos_cols, english)
    graph_row = dbc.Row(
        [dbc.Col(dcc.Graph(figure=fig, config={'displayModeBar': False}), width=6) for fig in figs]
    )
    return [html.H4(f"Your probability of passing the TOEFL is {pred}%."),
            dcc.Markdown("""Below are the top 4 ways you can improve your score,
                    alongside a histogram that compares your score (red line)
                    to the distribution of test-takers who passed the exam.""")] + [graph_row]

# Define the callback function to run the R script
def add_callbacks(app: dash.Dash):
    @app.callback(
        Output({"type": 'toefl-output-div', "index": 0}, 'children'),
        Output({"type": 'toefl-modal', "index": 0}, 'children'),
        Input({"type": "toefl-run-button", "index": 0}, 'n_clicks'),
        Input({'type': 'toefl-grade-placeholder', 'index': 0}, 'n_clicks'),
        State({'type': 'ep-input', 'index': 0}, 'value'),
        prevent_initial_call = True
    )
    def analyze_text(grade_clicks, placeholder_clicks, text):
        if dash.callback_context.triggered_id == {'index': 0, 'type': 'toefl-grade-placeholder'}:
            return text_to_div(EXAMPLE_TEXT), dash.no_update
        elif not text:
            return dash.no_update, dbc.Modal(dbc.ModalBody('Please enter text to grade or click "Grade Placeholer".'), is_open=True)
        else:
            return text_to_div(text), dash.no_update



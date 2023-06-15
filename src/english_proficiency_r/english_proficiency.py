import numpy as np
import pandas as pd
import plotly.express as px
import spacy
import yaml
from sklearn.ensemble import RandomForestRegressor
import pickle

nlp = spacy.load("en_core_web_sm")
try:
    nlp.add_pipe('sentencizer')
except:
    nlp.add_pipe(nlp.create_pipe('sentencizer'))

with open("english_proficiency_r/hedges_boosters.yml") as file:
    hb_dict = yaml.load(file, Loader=yaml.FullLoader)

imp = pd.read_csv('english_proficiency_r/rf_importance.csv')
english = pd.read_csv("english_proficiency_r/english_results_subset.csv")

try:
    with open('english_proficiency_r/random_forest_model.pkl', 'rb') as file:
        rf = pickle.load(file)
except:
    rf = RandomForestRegressor(random_state=42)
    rf.fit(english.drop("test_score", axis=1), english["test_score"])


def spacy_parse(text):
    """
    Parse text using spaCy.

    Args:
        text (str): Input text.

    Returns:
        pd.DataFrame: DataFrame with token, part of speech, and lemma columns.
    """
    doc = nlp(text)
    #sentences = [sent.string.strip() for sent in doc.sents]
    tokens = [token.text for token in doc]
    pos = [token.pos_ for token in doc]
    lemma = [token.lemma_ for token in doc]
    df = pd.DataFrame({"token": tokens, "pos": pos, "lemma": lemma})
    return df

def text2pred(text):
    """
    Perform text analysis and make predictions.

    Args:
        text (str): Input text.

    Returns:
        tuple: Prediction, pos_cols DataFrame, english DataFrame, and imp DataFrame.
    """
    df = spacy_parse(text)
    df["nextpos"] = df["pos"].shift(-1)
    df["bigram"] = df["pos"] + "." + df["nextpos"]
    pos_cols = pd.DataFrame(np.zeros((1, len(english.columns))), columns=english.columns)

    t = pd.Series(df["pos"]).value_counts()
    pos_cols.loc[0, t.index] = t.values

    b = pd.Series(df["bigram"]).value_counts()
    pos_cols.loc[0, b.index] = b.values

    pos_cols["uniquewords"] = df.loc[(df["pos"] != "PUNCT") & (df["pos"] != "SPACE"), "token"].str.lower().nunique()
    pos_cols["av_word_len"] = df.loc[(df["pos"] != "PUNCT") & (df["pos"] != "SPACE"), "lemma"].str.len().mean()
    pos_cols["words"] = len(df.loc[(df["pos"] != "PUNCT") & (df["pos"] != "SPACE")])
    pos_cols["sentences"] = len(df.loc[df["token"].isin([".", "!", "?"])])

    doc = nlp(text)
    hb_tokens = [hb_dict.get(token.text, 1) for token in doc]
    pos_cols["confidencehedged"] = sum(token == "ConfidenceHedged" for token in hb_tokens)
    pos_cols["confidencehigh"] = sum(token == "ConfidenceHigh" for token in hb_tokens)
    pos_cols = pos_cols.fillna(0)

    rf = RandomForestRegressor(random_state=42)
    rf.fit(english.drop("test_score", axis=1), english["test_score"])


    pred = np.clip(rf.predict(pos_cols[english.columns].drop("test_score", axis=1)), 0, 1) * 100

    return pred[0], pos_cols, english

def get_figs(pos_cols, english):
    """
    Generate histograms with vertical lines for top features.

    Args:
        pos_cols (pd.DataFrame): DataFrame with feature values.
        english (pd.DataFrame): English proficiency data.
        imp (pd.DataFrame): Importance data.

    Returns:
        list: List of histogram figures.
        list: List of top feature names.
    """
    percentiles = {}
    for column in english.drop("test_score", axis=1).columns:
        english_values = english[column].values
        pos_col_value = pos_cols[column].values[0]
        percentile = np.sum(english_values <= pos_col_value) / len(english_values)
        percentiles[column] = percentile
    # Create a new dataframe to store the percentiles
    percentiles_df = pd.DataFrame(percentiles.items(), columns=['feature', 'percentile'])
    merged_data = imp.merge(percentiles_df, on="feature", how="left")
    merged_data['relative_importance'] = [(0 if perc >= 0.5 else (1-perc)/0.5) * purity if good else ((0.5-perc)/0.5)*purity for perc,
                                          purity, good in zip(merged_data['percentile'], merged_data['IncNodePurity'],
                                                              merged_data['good_feature'])]
    sorted_data = merged_data.sort_values('relative_importance', ascending=False)
    top_features = sorted_data.head(4)['feature'].tolist()
    passing_scores = english[english['test_score'] == 1]
    figs = []
    feature_names = [imp.loc[imp['feature'] == feature, 'feature_name'].iloc[0] for feature in top_features]
    feature_titles = [imp.loc[imp['feature'] == feature, 'comment'].iloc[0] for feature in top_features]
    for i, feature in enumerate(top_features):
        fig = px.histogram(passing_scores, x=feature, nbins=30, histnorm='probability density')
        fig.update_traces(marker=dict(color='blue', line=dict(color='blue', width=1)
                                      , opacity=0.5), hoverinfo='none')
        fig.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', bargap=0)
        fig.update_layout(title=feature_titles[i])
        fig.add_vline(x=pos_cols[feature].iloc[0], line_color='red')
        fig.update_xaxes(title_text=feature_names[i], range=[0, max(passing_scores[feature])])
        fig.update_xaxes(title_text=feature_names[i])
        fig.update_yaxes(title_text='Fraction of Students who Passed')
        figs.append(fig)

    return figs

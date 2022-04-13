from typing import List
from typing import Tuple

import matplotlib.pyplot as plt
import pandas as pd
import spacy
import wordcloud

from src.tools.logging_utils import logger


def plot_nulls_per_column(
        df: pd.DataFrame, fig_size: Tuple[int, int] = (12, 8)) -> None:
    """
    Given a dataframe and figure size, this function plots the number of
    nulls for each column.

    Args:
        df (pd.DataFrame): dataframe to plot nulls per column
        fig_size (Optional, Tuple[int, int]): plot's size

    """
    nulls_per_column = df \
        .isnull() \
        .sum()

    if not nulls_per_column[nulls_per_column > 0].empty:
        logger.info(f"There are not nulls in columns.")
        _ = nulls_per_column \
            .sort_values(ascending=False) \
            .plot(kind="bar", xlabel="Column", ylabel="Null values",
                  title="Columns with nulls", figsize=fig_size)


def plot_annotations_visualisation(
        df: pd.DataFrame, patient_notes_df: pd.DataFrame,
        location_column: str = "location",
        annotation_column: str = "annotation",
        show_annotation: bool = True) -> None:
    """
    Given a dataframe with annotations and a dataframe with patient notes,
    this function generates an annotations plot. For each annotation it adds
    a label with the corresponding annotation.

    Args:
        df (pd.DataFrame): dataframe with locations and annotations
        patient_notes_df (pd.DataFrame): a dataframe with patient notes
            (previous filtered by only 1 client)
        location_column (Optional, str): location column's dataframe
        annotation_column (Optional, str): annotation column's dataframe
        show_annotation (Optional, bool): show or not the feature text for
            each annotation

    """
    location = df[location_column]
    if show_annotation:
        annotation = df[annotation_column]
    else:
        annotation = ["Annotation"] * df.shape[0]

    start_pos, end_pos, annotation_label = [], [], []
    for loc, label in zip(location, annotation):
        for pos in loc:
            # If it contains semicolon, this means that there
            # are more than one annotation
            if ";" in pos:
                for pos_i, label_i in zip(pos.split(";"), label):
                    start_pos.append(pos_i.split()[0])
                    end_pos.append(pos_i.split()[1])
                    annotation_label.append(label_i)
            else:
                start_pos.append(pos.split()[0])
                end_pos.append(pos.split()[1])
                annotation_label.append(label)

    ents = []
    for i in range(len(start_pos)):
        ents.append({
            'start': int(start_pos[i]),
            'end': int(end_pos[i]),
            "label": annotation_label[i],
        })

    doc = {
        "text": patient_notes_df["pn_history"].iloc[0],
        "ents": ents
    }

    colors = {"Annotation": "linear-gradient(90deg, #aa9cfc, #fc9ce7)"}
    options = {"colors": colors}
    spacy.displacy.render(
        doc, style="ent", options=options, manual=True, jupyter=True)


def plot_wordcloud(
        data: List[str], width: int = 600, height: int = 400,
        fig_size: Tuple[int, int] = (25, 10)) -> None:
    """
    Given a list of strings, this function creates a wordcloud plot.

    Args:
        data (List[str]): list of strings
        width (Optional, int): plot's width
        height (Optional, int): plot's height
        fig_size (Optional, Tuple[int]): plot's size
    """
    wordcloud_notes = wordcloud.WordCloud(
        stopwords=wordcloud.STOPWORDS, max_font_size=120, max_words=5000,
        width=width, height=height, background_color='white').generate(data)

    fig, ax = plt.subplots(figsize=fig_size)
    ax.imshow(wordcloud_notes, interpolation='bilinear')
    ax.set_axis_off()
    plt.imshow(wordcloud_notes)

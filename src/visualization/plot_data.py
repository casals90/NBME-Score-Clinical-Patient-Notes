import pandas as pd
from src.tools.logging_utils import logger
from typing import Tuple


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

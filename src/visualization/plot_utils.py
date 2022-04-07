from typing import Union, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_histogram(
        data: Union[np.array, pd.Series], bins: int = 10, title: str = None,
        y_label: str = None, x_label: str = None,
        fig_size: Tuple[int, int] = (15, 8), **kwargs) -> None:
    """
    Given data, this function creates a histogram plot.

    Args:
        data (Union[np.array, pd.Series]): data to plot histogram
        bins (Optional, int): number of bins
        title (Optional, str): plot's title
        y_label (Optional, str): plot's y label
        x_label (Optional, str): plot's x label
        fig_size (Optional, Tuple[int, int]): plot's size

    """
    _ = plt.figure(figsize=fig_size)
    ax = data.hist(bins=bins, **kwargs)
    _ = ax.set_title(title)
    _ = ax.set_ylabel(y_label)
    _ = ax.set_xlabel(x_label)

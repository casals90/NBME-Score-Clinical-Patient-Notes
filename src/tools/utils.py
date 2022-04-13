import pandas as pd
from typing import List, Tuple

def create_list_of_tuples(loc: List[str]) -> List[Tuple[int, int]]:
    """
    This function is a utility to convert the location format (e.x. ['1 2', '3 4]) to
    a list of tuples format (e.x. [(1,2), (3,4)]).

    Args:
        loc (List[str]): a locations list (from one dataframe row).

    Returns:
        a list of integer tuples.
    """
    result = []
    for l in loc:
        x = int(l.split()[0])
        y = int(l.split()[1])
        result.append((x, y))

    return result


def decode_location(location: pd.Series) -> pd.Series:
    """
    Given a location of annotations, this function converts the locations
    from string to list of tuples.

    Args:
        location (pd.Series): location dataframe's column

    Returns:
        a pd.Series with a list of tuples for each location.
    """
    # Fixed specific wrong cases
    location = location.str.replace(";", "', '")

    location = location \
        .apply(eval) \
        .apply(create_list_of_tuples)

    return location
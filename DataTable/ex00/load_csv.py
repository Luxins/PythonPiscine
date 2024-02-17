import pandas as pd
from pathlib import Path
import os


def load(path: str):
    if not isinstance(path, str):
        return None
    try:
        pathObj: Path = Path(path)
    except TypeError:
        return None
    if not pathObj.exists():
        return None
    if not os.access(pathObj, os.R_OK):
        return None
    # checking for ".csv" file extension
    fileExtension: str = os.path.splitext(pathObj)[-1].lower()
    if fileExtension != ".csv":
        return None
    try:
        df: pd.DataFrame = pd.read_csv(path, index_col=0)
    except (pd.errors.EmptyDataError, Exception):
        return None
    print(f"Loading dataset of dimensions {df.shape}")
    return df

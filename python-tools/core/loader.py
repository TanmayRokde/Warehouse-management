import pandas as pd
from .config import MAPPINGS_FILE

def load_mapping():
    return pd.read_csv(MAPPINGS_FILE)

def load_sales(file_path):
    return pd.read_csv(file_path)

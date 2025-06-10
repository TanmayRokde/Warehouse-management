import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

MAPPINGS_FILE = os.path.join(DATA_DIR, "mappings.csv")
SAMPLE_SALES_FILE = os.path.join(DATA_DIR, "sample_sales.csv")
MAPPED_OUTPUT_FILE = os.path.join(DATA_DIR, "mapped_output.csv")

"""Load and clean the data"""

import pandas as pd

FILE_PATH = "./data/processed_data/ERAWIJANTARI_GASTRIC_CANCER_2020/genera.tsv"

# Load data into a DataFrame
df = pd.read_csv(FILE_PATH, sep="\t")

# Drop rows with missing values (if appropriate)
df_clean = df.dropna()

# Fill missing values (if appropriate)
# Use ffill() for forward fill
df_filled_forward = df.ffill()
# Use bfill() for backward fill
df_filled_backward = df.bfill()
# Fill with a constant value if it makes sense for your data
df_filled_constant = df.fillna(0)

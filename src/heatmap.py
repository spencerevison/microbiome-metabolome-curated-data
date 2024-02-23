"""Display a heatmap representing all bacteria"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import the DataFrame
from data import df_clean as df

# Create a new DataFrame with the conditions extracted
conditions = df.index.to_series().apply(lambda x: x.split(".")[-1])

# Create a sorting key based on the conditions
sort_key = conditions.apply(lambda x: 0 if "Healthy" in x else 1)

# Combine the conditions and sorting key into the DataFrame
df_combined = pd.concat(
    [df, conditions.rename("Condition"), sort_key.rename("SortKey")], axis=1
)

# Sort the DataFrame based on the condition, with healthy samples first
df_sorted = df_combined.sort_values(by="SortKey", ascending=True).drop(
    columns=["Condition", "SortKey"]
)

# Convert all columns to numeric, except the sample name index
df_numeric = df_sorted.apply(pd.to_numeric, errors="coerce")

# Replace zeros with a very small positive number
df_numeric = df_numeric.replace(0, np.finfo(float).eps)

# Apply log transformation
df_log_transformed = np.log(df_numeric)

# Create the heatmap with the log-transformed data
plt.figure(figsize=(20, 10))
sns.heatmap(df_log_transformed, cmap="viridis", yticklabels=df_sorted.index)
plt.title("Log-transformed Heatmap of Bacteria Abundance Across Samples")
plt.xlabel("Bacteria Genera")
plt.ylabel("Samples")
plt.show()

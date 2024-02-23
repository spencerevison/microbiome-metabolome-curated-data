import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

# Import the DataFrame (assuming df_clean is your cleaned and preprocessed DataFrame)
from data import df_clean as df

# Select only numeric columns for PCA
df_numeric = df.select_dtypes(include=[np.number])

# Standardize the data
scaler = StandardScaler()
df_standardized = scaler.fit_transform(df_numeric)

# Determine the number of components such that 95% of the variance is retained
pca = PCA(0.95)
principal_components = pca.fit_transform(df_standardized)

# Explained variance ratio for each principal component
explained_variance_ratio = pca.explained_variance_ratio_
cumulative_explained_variance = np.cumsum(explained_variance_ratio)

# Plot the explained variance ratio
plt.figure(figsize=(10, 5))
plt.bar(
    range(1, len(explained_variance_ratio) + 1),
    explained_variance_ratio,
    alpha=0.6,
    align="center",
    label="Individual explained variance",
)
plt.step(
    range(1, len(cumulative_explained_variance) + 1),
    cumulative_explained_variance,
    where="mid",
    label="Cumulative explained variance",
)
plt.ylabel("Explained variance ratio")
plt.xlabel("Principal components")
plt.title("Explained Variance Ratio by PCA Components")
plt.legend(loc="best")
plt.tight_layout()
plt.show()

# Create a DataFrame with the principal components
pc_columns = [f"PC{i}" for i in range(1, len(principal_components[0]) + 1)]
df_pca = pd.DataFrame(data=principal_components, columns=pc_columns)

# Visualize the first two principal components (if they are present)
if len(pc_columns) > 1:
    plt.figure(figsize=(8, 5))
    plt.scatter(df_pca["PC1"], df_pca["PC2"], alpha=0.5)
    plt.title("Scatter Plot of First Two Principal Components")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("Not enough components for a scatter plot.")

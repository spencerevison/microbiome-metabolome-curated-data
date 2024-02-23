"""Basic script to load and display abundance of one type of bacteria"""

import matplotlib.pyplot as plt
from data import df

import matplotlib.pyplot as plt

# Subset the data for plotting
data_to_plot = df[
    [
        "Sample",
        "d__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rhodobacterales;f__Rhodobacteraceae;g__Oceaniglobus",
    ]
].copy()

# Considering the file might have a lot of samples, let's limit to the first 10 for clarity in the graph
data_to_plot = data_to_plot.head(10)

# Set the 'Sample' column as the index to use as labels on the x-axis
data_to_plot.set_index("Sample", inplace=True)

# Plotting
plt.figure(figsize=(10, 6))  # Set the figure size for better readability
data_to_plot.plot(kind="bar", legend=None)  # Plot a bar graph
plt.title("Abundance of Oceaniglobus Bacteria Across Samples")  # Title of the graph
plt.ylabel("Abundance")  # Y-axis label
plt.xticks(rotation=45, ha="right")  # Rotate the x-axis labels for better readability
plt.tight_layout()  # Adjust the layout to make room for the rotated x-axis labels
plt.show()

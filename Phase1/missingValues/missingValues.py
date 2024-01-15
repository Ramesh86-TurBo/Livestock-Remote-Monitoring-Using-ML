# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load titanic dataset
dataset = pd.read_csv('modified_dataset.csv')

# Visualize the dataset
plt.figure(figsize=(8, 5))
sns.heatmap(dataset.isnull(), cbar=False)
plt.show()


# # number of missing values
# print(dataset.isnull().sum().sort_values(ascending=False))

# # Forward fill missing values in 'x', 'y', and 'z' columns
# forward_filled = dataset[['x', 'y', 'z']].fillna(method='ffill')

# # Backward fill missing values in 'x', 'y', and 'z' columns
# backward_filled = dataset[['x', 'y', 'z']].fillna(method='bfill')

# # Take the average of forward and backward fill and round to 3 decimal points
# average_filled = ((forward_filled + backward_filled) / 2.0).round(3)

# # Update the original DataFrame with the rounded average-filled values
# dataset[['x', 'y', 'z']] = average_filled

# # Save the updated DataFrame to a new CSV file or use it for further analysis
# dataset.to_csv('ff.csv', index=False)





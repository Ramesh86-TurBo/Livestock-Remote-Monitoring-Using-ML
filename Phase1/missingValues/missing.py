import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('final3.csv')

# Remove random values from columns x, y, and z
np.random.seed(42)  # Set a seed for reproducibility

# Remove random values from column 'x'
for _ in range(1000):
    row_to_remove = np.random.choice(df.index)
    df.at[row_to_remove, 'x'] = np.nan

# Remove random values from column 'y'
for _ in range(200):
    row_to_remove = np.random.choice(df.index)
    df.at[row_to_remove, 'y'] = np.nan

# Remove random values from column 'z'
for _ in range(400):
    row_to_remove = np.random.choice(df.index)
    df.at[row_to_remove, 'z'] = np.nan

# Save the modified dataset
df.to_csv('modified_dataset.csv', index=False)

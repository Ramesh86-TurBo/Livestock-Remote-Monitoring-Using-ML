import pandas as pd
from scipy.stats import zscore

# Load the dataset
file_path = 'final3.csv'  # Replace with your actual file path
dataset = pd.read_csv(file_path, parse_dates=['time_stamp'])

# Extract features (x, y, z)
features = ['x', 'y', 'z']

# Calculate Z-scores for each feature
z_scores = zscore(dataset[features])

# Define a threshold for outlier removal
threshold = 3

# Remove rows with outliers based on the Z-scores
outlier_mask = (abs(z_scores) <= threshold).all(axis=1)
filtered_dataset = dataset[outlier_mask]

# Save the filtered dataset to a new file
filtered_file_path = 'new.csv'  # Replace with your desired file path
filtered_dataset.to_csv(filtered_file_path, index=False)

print(f"Original dataset shape: {dataset.shape}")
print(f"Filtered dataset shape: {filtered_dataset.shape}")


import pandas as pd

# Load your first dataset
dataset1 = pd.read_csv('convertedData2.csv')  # Replace 'dataset1.csv' with your actual filename

# Load your second dataset
dataset2 = pd.read_csv('convertedData1.csv')  # Replace 'dataset2.csv' with your actual filename

# Concatenate datasets along the columns
combined_dataset = pd.concat([dataset1, dataset2], axis=1)

# Save the combined dataset to a new CSV file
combined_dataset.to_csv('final.csv', index=False)

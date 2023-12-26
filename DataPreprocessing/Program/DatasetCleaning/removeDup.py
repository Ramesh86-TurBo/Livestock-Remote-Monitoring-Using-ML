import pandas as pd

# Load your dataset
dataset = pd.read_csv('final.csv')  # Replace 'your_dataset.csv' with your actual dataset file

# Remove duplicates based on all columns
dataset_no_duplicates = dataset.drop_duplicates()

# Save the dataset without duplicates to a new CSV file
dataset_no_duplicates.to_csv('final2.csv', index=False)

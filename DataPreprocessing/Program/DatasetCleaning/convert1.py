import pandas as pd

# Load your original dataset
original_dataset = pd.read_csv('combined_dataset.csv')  # Replace 'test2.csv' with your actual dataset file

# Initialize an empty list to store the extended data
extended_data = []

# Iterate through each row in the original dataset
for index, row in original_dataset.iterrows():
    # Extend each row 10 times
    for _ in range(10):
        extended_data.append(row[['sitting', 'standing', 'walking', 'grazing']])

# Create a new DataFrame from the extended data
extended_dataset = pd.DataFrame(extended_data)

# Save the extended dataset to a new CSV file
extended_dataset.to_csv('convertedData1.csv', index=False)

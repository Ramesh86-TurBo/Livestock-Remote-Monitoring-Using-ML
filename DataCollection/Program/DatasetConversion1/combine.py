import pandas as pd

# Load your three datasets (replace 'dataset1.csv', 'dataset2.csv', and 'dataset3.csv' with your actual file names)
dataset1 = pd.read_csv('testData1.csv')
dataset2 = pd.read_csv('testData2.csv')
dataset3 = pd.read_csv('testData3.csv')

# Concatenate the datasets vertically
combined_dataset = pd.concat([dataset1, dataset2, dataset3], ignore_index=True)

# Save the combined dataset to a new CSV file
combined_dataset.to_csv('combined_dataset.csv', index=False)

# Display a message
print("Datasets combined successfully and saved to combined_dataset.csv")

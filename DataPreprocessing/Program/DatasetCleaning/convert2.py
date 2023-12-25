import pandas as pd

# Load your original dataset
original_dataset = pd.read_csv('combined_dataset.csv')  # Replace 'your_original_dataset.csv' with your actual dataset file

# Create a new DataFrame for reshaped data
reshaped_data = pd.DataFrame()

# Extract columns for x, y, z
x_columns = ['x_0', 'x_29', 'x_59', 'x_89', 'x_119', 'x_149', 'x_179', 'x_209', 'x_239', 'x_269']
y_columns = ['y_0', 'y_29', 'y_59', 'y_89', 'y_119', 'y_149', 'y_179', 'y_209', 'y_239', 'y_269']
z_columns = ['z_0', 'z_29', 'z_59', 'z_89', 'z_119', 'z_149', 'z_179', 'z_209', 'z_239', 'z_269']

# Reshape data for each column
reshaped_data['x'] = original_dataset[x_columns].values.flatten()
reshaped_data['y'] = original_dataset[y_columns].values.flatten()
reshaped_data['z'] = original_dataset[z_columns].values.flatten()

# Save the reshaped dataset to a new CSV file
reshaped_data.to_csv('convertedData2.csv', index=False)

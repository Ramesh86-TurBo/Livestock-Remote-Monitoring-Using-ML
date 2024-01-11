import pandas as pd

df = pd.read_csv('final3.csv')

# Extract the x, y, z columns
x_values = df['x']
y_values = df['y']
z_values = df['z']

# Calculate mean and standard deviation for each feature
x_mean, x_std = x_values.mean(), x_values.std()
y_mean, y_std = y_values.mean(), y_values.std()
z_mean, z_std = z_values.mean(), z_values.std()

# Define the threshold in terms of standard deviations
threshold = 3

# Function to count readings more than 3 standard deviations from the mean
def count_beyond_threshold(feature_values, mean, std, threshold):
    beyond_threshold = ((feature_values > mean + threshold * std) | (feature_values < mean - threshold * std))
    return beyond_threshold.sum()

# Print the results for each feature
for feature_name, feature_values, feature_mean, feature_std in zip(['x', 'y', 'z'], [x_values, y_values, z_values], [x_mean, y_mean, z_mean], [x_std, y_std, z_std]):
    count = count_beyond_threshold(feature_values, feature_mean, feature_std, threshold)
    print(f"Number of readings in {feature_name} more than 3 standard deviations from the mean: {count}")



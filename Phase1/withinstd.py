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

# Define the thresholds in terms of standard deviations
thresholds = [1, 2, 3]

# Function to count readings within different standard deviations from the mean
def count_within_threshold(feature_values, mean, std, threshold):
    lower_bound = mean - threshold * std
    upper_bound = mean + threshold * std
    return ((feature_values >= lower_bound) & (feature_values <= upper_bound)).sum()

# Print the results for each feature
for feature_name, feature_values, feature_mean, feature_std in zip(['x', 'y', 'z'], [x_values, y_values, z_values], [x_mean, y_mean, z_mean], [x_std, y_std, z_std]):
    print(f"Feature: {feature_name}")
    for threshold in thresholds:
        count = count_within_threshold(feature_values, feature_mean, feature_std, threshold)
        print(f"  Number of readings within {threshold} standard deviations from the mean: {count}")

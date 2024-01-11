import pandas as pd
from scipy.stats import zscore

df = pd.read_csv('final3.csv')

# Extract the x, y, z columns
x_values = df['x']
y_values = df['y']
z_values = df['z']

# Calculate z-scores for each column
z_scores_x = zscore(x_values)
z_scores_y = zscore(y_values)
z_scores_z = zscore(z_values)



# # Print the number of points whose z-score is more than 3 or less than -3 for 'x', 'y', and 'z'
# count_x_z_greater_than_3 = (z_scores_x > 3).sum()
# count_x_z_less_than_minus_3 = (z_scores_x < -3).sum()

# count_y_z_greater_than_3 = (z_scores_y > 3).sum()
# count_y_z_less_than_minus_3 = (z_scores_y < -3).sum()

# count_z_z_greater_than_3 = (z_scores_z > 3).sum()
# count_z_z_less_than_minus_3 = (z_scores_z < -3).sum()

# print(f"Number of points whose z-score of 'x' is greater than 3: {count_x_z_greater_than_3}")
# print(f"Number of points whose z-score of 'x' is less than -3: {count_x_z_less_than_minus_3}")

# print(f"Number of points whose z-score of 'y' is greater than 3: {count_y_z_greater_than_3}")
# print(f"Number of points whose z-score of 'y' is less than -3: {count_y_z_less_than_minus_3}")

# print(f"Number of points whose z-score of 'z' is greater than 3: {count_z_z_greater_than_3}")
# print(f"Number of points whose z-score of 'z' is less than -3: {count_z_z_less_than_minus_3}")

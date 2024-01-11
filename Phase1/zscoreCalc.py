import pandas as pd
from scipy.stats import zscore

df = pd.read_csv('final3.csv')

# Extract the x, y, z columns
x_values = df['x']
y_values = df['y']
z_values = df['z']

# Calculate z-scores for each column
z_scores_x = zscore(x_values).round(3)
z_scores_y = zscore(y_values).round(3)
z_scores_z = zscore(z_values).round(3)

# Add z-scores to the DataFrame
df['z_score_x'] = z_scores_x
df['z_score_y'] = z_scores_y
df['z_score_z'] = z_scores_z

# Save the DataFrame with z-scores to a new CSV file
output_file_path = 'z_scores_output.csv'
df.to_csv(output_file_path, index=False)

print(f"Z-scores saved to: {output_file_path}")

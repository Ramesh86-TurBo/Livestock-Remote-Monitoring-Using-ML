import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
file_path = 'final3.csv'  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Task 1: Plot data visualization for outliers
plt.figure(figsize=(12, 8))
sns.boxplot(data=df[['x', 'y', 'z']])
plt.title('Boxplot for x, y, and z')
plt.show()

# Task 2: Calculate and plot the distribution of z-score
z_scores = stats.zscore(df[['x', 'y', 'z']])
df_z_scores = pd.DataFrame(z_scores, columns=['x', 'y', 'z'])

plt.figure(figsize=(12, 8))
sns.kdeplot(data=df_z_scores[['x', 'y', 'z']], fill=True)
plt.title('Distribution of Z-scores for x, y, and z')
plt.show()

# Task 3: Delete rows with outliers and save the cleaned dataset
threshold = 3
df_cleaned = df[(abs(z_scores) < threshold).all(axis=1)]

# Save the cleaned dataset to a new CSV file
output_file_path = 'cleaned_dataset.csv'  # Replace with the desired output file path
df_cleaned.to_csv(output_file_path, index=False)

print(f"Rows before removing outliers: {len(df)}")
print(f"Rows after removing outliers: {len(df_cleaned)}")
print(f"Cleaned dataset saved to {output_file_path}")

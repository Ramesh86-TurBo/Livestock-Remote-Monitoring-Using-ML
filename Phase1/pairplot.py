import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your labeled dataset
dataset = pd.read_csv('final3.csv')

# Select features for pair plot
features = ['x', 'y', 'z']

# Add target class to the features
features_with_target = features + ['grazing']

# Subset the dataset with selected features
subset_data = dataset[features_with_target]

# Create a pair plot
sns.set(style="ticks")
sns.pairplot(subset_data, hue='grazing', markers=["o", "s", "D", "X"])

# Show the plot
plt.show()

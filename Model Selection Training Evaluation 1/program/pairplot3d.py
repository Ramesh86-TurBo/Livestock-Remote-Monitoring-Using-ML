import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Assuming 'your_dataset.csv' is the name of your CSV file
# Update it with the actual name if needed
file_path = 'final3.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, parse_dates=['time_stamp'])

# Create a 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot for sitting
ax.scatter(df['x'][df['sitting'] == 1], df['y'][df['sitting'] == 1], df['z'][df['sitting'] == 1], label='Sitting', marker='o')
# Scatter plot for standing
ax.scatter(df['x'][df['standing'] == 1], df['y'][df['standing'] == 1], df['z'][df['standing'] == 1], label='Standing', marker='s')
# Scatter plot for walking
ax.scatter(df['x'][df['walking'] == 1], df['y'][df['walking'] == 1], df['z'][df['walking'] == 1], label='Walking', marker='^')
# Scatter plot for grazing
ax.scatter(df['x'][df['grazing'] == 1], df['y'][df['grazing'] == 1], df['z'][df['grazing'] == 1], label='Grazing', marker='x')

# Label the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Add a legend
ax.legend()

# Add a title to the plot
plt.title('3D Scatter Plot of Accelerometer Data and Target Behaviors')

# Show the plot
plt.show()

import csv
import matplotlib.pyplot as plt
import numpy as np

# Initialize empty lists to store the data
x_values = []
y_values = []
z_values = []

# Open the CSV file and read the data
with open('converted_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x_values.append(float(row['x']))
        y_values.append(float(row['y']))
        z_values.append(float(row['z']))


time = np.arange(0, len(x_values))

plt.figure(figsize=(12, 6))
plt.plot(time, x_values, label='X')
plt.plot(time, y_values, label='Y')
plt.plot(time, z_values, label='Z')

plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Accelerometer Data vs Time')

plt.legend()
plt.grid(True)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Assuming your dataset is in a CSV file named 'your_dataset.csv'
# Replace 'your_dataset.csv' with the actual file name.
df = pd.read_csv('final3.csv', parse_dates=['time_stamp'])

# Plotting
plt.figure(figsize=(12, 6))

plt.plot(df['time_stamp'], df['x'], label='x')
plt.plot(df['time_stamp'], df['y'], label='y')
plt.plot(df['time_stamp'], df['z'], label='z')

plt.title('Sensor Readings over Time')
plt.xlabel('Time(sec)')
plt.ylabel('Sensor Values(m/s^2)')
plt.legend()
plt.grid(True)
plt.show()

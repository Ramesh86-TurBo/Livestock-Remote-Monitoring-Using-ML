import pandas as pd
from datetime import datetime, timedelta

# Function to generate timestamp sequence
def generate_timestamps(start_timestamp, num_rows, interval_seconds=1):
    timestamps = [start_timestamp + timedelta(seconds=i * interval_seconds) for i in range(num_rows)]
    return timestamps

# Load your original dataset (replace this with your data loading logic)
original_dataset = pd.read_csv('final.csv')

# Set the start timestamp and generate timestamp sequence
start_timestamp = datetime.strptime('2018-12-10T13:51:41', '%Y-%m-%dT%H:%M:%S')
num_rows = len(original_dataset)
timestamps = generate_timestamps(start_timestamp, num_rows)

# Add the 'time_stamp' column to the original dataset
original_dataset['time_stamp'] = timestamps

# Reorder columns to match the desired order
column_order = ['time_stamp', 'x', 'y', 'z', 'sitting', 'standing', 'walking', 'grazing']
modified_dataset = original_dataset[column_order]

# Save the modified dataset to a new CSV file
modified_dataset.to_csv('final3.csv', index=False)

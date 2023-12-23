import pandas as pd

# Load the combined dataset (replace 'combined_dataset.csv' with your actual file name)
combined_dataset = pd.read_csv('combined_dataset.csv')

# Convert 'time_stamp' column to datetime format, handling errors
combined_dataset['time_stamp'] = pd.to_datetime(combined_dataset['time_stamp'], errors='coerce')

# Drop rows with NaT values (invalid datetime entries)
combined_dataset = combined_dataset.dropna(subset=['time_stamp'])

# Calculate the time difference between consecutive timestamps
time_diff = combined_dataset['time_stamp'].diff().dt.total_seconds()

# Display total time duration in hours
total_time_duration_hours = time_diff.sum() / 3600  # Convert seconds to hours
print(f"Total time duration: {total_time_duration_hours:.2f} hours")


# Display the number of rows
num_rows = combined_dataset.shape[0]
print(f"Number of rows: {num_rows}")

# Display the number of readings for each behavior
behavior_counts = combined_dataset[['sitting', 'standing', 'walking', 'grazing']].sum()
print("Number of readings for each behavior:")
print(behavior_counts)

# Display the number of readings falling in the intersection of behaviors
intersection_counts = combined_dataset[['sitting', 'standing', 'walking', 'grazing']].sum(axis=1)
num_intersection = (intersection_counts > 1).sum()
print(f"Number of readings falling in the intersection of behaviors: {num_intersection}")

import csv
import json

# Load JSON data from file or Firebase database response
with open('sample.json', 'r') as file:
    data = json.load(file)

# Extract relevant information and write to CSV
csv_file_path = 'overall.csv'
csv_columns = ['timestamp', 'x', 'y', 'z']

with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()

    for key, values in data.items():
        row = {
            'timestamp': values['timestamp'],
            'x': values['x'],
            'y': values['y'],
            'z': values['z']
        }
        writer.writerow(row)

print(f"CSV file has been created: {csv_file_path}")

import csv
from datetime import datetime

def convert_timestamp(timestamp):
    return datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

# Load CSV data
csv_file_path = 'grazing.csv'
output_csv_file = 'output.csv'

with open(csv_file_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    
    # Write to a new CSV file with time format
    with open(output_csv_file, 'w', newline='') as output_csv:
        csv_columns = reader.fieldnames + ['time_format']
        writer = csv.DictWriter(output_csv, fieldnames=csv_columns)
        writer.writeheader()

        for row in reader:
            row['time_format'] = convert_timestamp(row['timestamp'])
            writer.writerow(row)

print(f"CSV file with time format has been created: {output_csv_file}")

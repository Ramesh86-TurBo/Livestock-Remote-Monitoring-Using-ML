import pandas as pd
from datetime import datetime
import ast

# Read the original CSV file
with open('new.csv', 'r') as file:
    data_str = file.read()

# Convert the string to a dictionary
data_dict = ast.literal_eval(data_str)

# Extract the nested data into a list of dictionaries
converted_data = []
for timestamp, nested_data in data_dict.items():
    # Convert the timestamp to a human-readable format
    human_readable_time = datetime.fromtimestamp(int(nested_data['timestamp'])).strftime('%Y-%m-%d %H:%M:%S')

    # Create a dictionary with the desired format
    converted_entry = {
        'time': human_readable_time,
        'x': nested_data['x'],
        'y': nested_data['y'],
        'z': nested_data['z']
    }

    converted_data.append(converted_entry)

# Create a Pandas DataFrame from the converted data
df = pd.DataFrame(converted_data)

# Save the DataFrame to a CSV file
df.to_csv('lol.csv', index=False)

print("Data conversion completed and saved to lol.csv")

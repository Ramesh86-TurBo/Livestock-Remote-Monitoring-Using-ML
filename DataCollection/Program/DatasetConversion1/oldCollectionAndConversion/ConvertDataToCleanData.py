import csv
import pandas as pd
from datetime import datetime

# Your original data in dictionary format
original_data = 

}

# Create a list to store the converted data
converted_data = []

for timestamp, data in original_data.items():
    
    # Convert the timestamp to a human-readable format
    human_readable_time = datetime.fromtimestamp(int(data['timestamp'])).strftime('%Y-%m-%d %H:%M:%S')
    
    # Create a dictionary with the desired format
    converted_entry = {
        'time': human_readable_time,
        'x': data['x'],
        'y': data['y'],
        'z': data['z']
    }
    
    converted_data.append(converted_entry)

# Create a Pandas DataFrame from the converted data
df = pd.DataFrame(converted_data)

# Save the DataFrame to a CSV file
df.to_csv('converted_data.csv', index=False)

print("Data conversion completed and saved to converted_data.csv")
The sensor data is stored real time in fire base and downloaded as a CSV file. The data format that we receive form the sensor/CSV file is in this form:

**Format of data from the sensor:**

```
{'1695980330': {'driverId': '0000', 'lat': 0, 'lng': 0, 'timestamp': '1695980330', 'x': '-9.53', 'y': '3.14', 'z': '3.69'}, '1695980331': {'driverId': '0000', 'lat': 0, 'lng': 0, 'timestamp': '1695980331', 'x': '-9.53', 'y': '3.18', 'z': '3.69'}, '1695980332': {'driverId': '0000', 'lat': 0, 'lng': 0, 'timestamp': '1695980332', 'x': '-9.53', 'y': '3.18', 'z': '3.73'}, '1695980334': {'driverId': '0000', 'lat': 0, 'lng': 0, 'timestamp': '1695980334', 'x': '-9.49', 'y': '3.18', 'z': '3.69'}, '1695980335': {'driverId': '0000', 'lat': 0, 'lng': 0, 'timestamp': '1695980335', 'x': '-9.49', 'y': '3.10', 'z': '3.65'}
}
```

The data is in a nested dictionary format, similar to JSON. Each timestamp is a key, and its value is another dictionary with attributes like 'driverId', 'lat', 'lng', 'timestamp', 'x', 'y', and 'z'. While it resembles JSON, it's not exact—keys and string values use single quotes, and there's no top-level curly braces.

To analyze or process this data, we have to convert it into a format that is more suitable for the specific use case. In the context of livestock behavior prediction, there is a need to extract relevant features or reformat the data to suit the input requirements of your machine learning models.

**The Python Program to convert the data into format suitable for my use case:**

```python
import ast
import pandas as pd
from datetime import datetime

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
```

**Program Explained:**

1. **Read CSV Data:**
   - Reads the contents of a CSV file named 'new.csv'.

2. **Convert String to Dictionary:**
   - Uses the `ast.literal_eval` function to convert the string representation of a dictionary in the CSV file to an actual dictionary (`data_dict`).

3. **Extract Nested Data:**
   - Iterates over the nested dictionary (`data_dict`), where each key is a timestamp, and the corresponding value is another dictionary containing attributes.
   - Converts the timestamp to a human-readable format.
   - Creates a new dictionary (`converted_entry`) with the desired format, including timestamp, x, y, and z values.
   - Appends each converted entry to a list (`converted_data`).

4. **Create DataFrame:**
   - Utilizes the Pandas library to create a DataFrame (`df`) from the list of converted entries.

5. **Save to CSV:**
   - Saves the DataFrame to a new CSV file named 'lol.csv'.

6. **Print Completion Message:**
   - Prints a message indicating that the data conversion is completed and saved to 'lol.csv'.

**Output:**

```
|            time     |     x     |     y     |     z     |
|---------------------|-----------|-----------|-----------|
| 2023-09-29 15:08:50 |   -9.53   |    3.14   |    3.69   |
| 2023-09-29 15:08:51 |   -9.53   |    3.18   |    3.69   |
| 2023-09-29 15:08:52 |   -9.53   |    3.18   |    3.73   |
| 2023-09-29 15:08:54 |   -9.49   |    3.18   |    3.69   |
| 2023-09-29 15:08:55 |   -9.49   |    3.10   |    3.65   |

```


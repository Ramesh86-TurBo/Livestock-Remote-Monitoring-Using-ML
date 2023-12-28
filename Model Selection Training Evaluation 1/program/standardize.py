import pandas as pd
from sklearn.preprocessing import StandardScaler

# Assuming 'df' is your DataFrame with the training data
data = {
    'time_stamp': ['10-12-2018 13:51', '10-12-2018 13:51', '10-12-2018 13:51', '10-12-2018 13:51', '10-12-2018 13:51'],
    'x': [0.438, -0.184, 0.652, 1.031, 0.711],
    'y': [0.844, -0.82, 0.711, 0.703, 0.48],
    'z': [0.309, -0.68, 0.148, 0.395, 0.473],
    'sitting': [0, 0, 0, 0, 0],
    'standing': [0, 0, 0, 0, 0],
    'walking': [1, 1, 1, 1, 1],
    'grazing': [0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

# Extract features and labels
X = df[['x', 'y', 'z', 'sitting', 'standing', 'walking', 'grazing']]

# Standardize features using StandardScaler
scaler = StandardScaler()

# Fit and transform the training data
X_scaled = scaler.fit_transform(X)

# Print the scaled training data
print("Scaled Training Data:")
print(pd.DataFrame(X_scaled, columns=X.columns))

# Scale a new data point
new_data = {'x': [3], 'y': [2.4], 'z': [3.8], 'sitting': [0], 'standing': [0], 'walking': [1], 'grazing': [0]}
new_data_scaled = scaler.transform(pd.DataFrame(new_data))

# Print the scaled new data point
print("\nScaled New Data Point:")
print(pd.DataFrame(new_data_scaled, columns=X.columns))

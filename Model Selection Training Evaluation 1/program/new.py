import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

# Load the saved model
loaded_model = joblib.load('mark1.joblib')

# Provide new input data (replace this with your actual data)
new_data = pd.DataFrame({'x': [new_x_value], 'y': [new_y_value], 'z': [new_z_value]})

# Load your labeled dataset for label encoding
dataset = pd.read_csv('final3.csv')
y = dataset[['sitting', 'standing', 'walking', 'grazing']]

# Convert binary labels to class indices using the same label encoder
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y.idxmax(axis=1))

# Initialize MinMaxScaler
scaler = MinMaxScaler()
new_data_scaled = scaler.fit_transform(new_data)

# Make predictions on the new data
predicted_class = loaded_model.predict(new_data_scaled)

# Decode the predicted class to get the original label
predicted_label = label_encoder.inverse_transform(predicted_class)

print(f'The predicted class is: {predicted_label[0]}')


import joblib

# Load the XGBoost model from the .joblib file
model = joblib.load('mark1.joblib')

# Define new input data (replace these values with your actual data)
new_data = [[10, 3.4, 5]]

# Make predictions on the new input data
predictions = model.predict(new_data)

# Print the predicted class or value
print("Predictions:", predictions)

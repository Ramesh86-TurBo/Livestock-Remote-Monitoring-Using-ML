import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load your labeled dataset
dataset = pd.read_csv('combined_dataset.csv')  # Replace 'your_labeled_dataset.csv' with your actual dataset file

# Separate features (X) and labels (y)
X = dataset[['x_0', 'x_29', 'x_59', 'x_89', 'x_119', 'x_149', 'x_179', 'x_209', 'x_239', 'x_269',
             'y_0', 'y_29', 'y_59', 'y_89', 'y_119', 'y_149', 'y_179', 'y_209', 'y_239', 'y_269',
             'z_0', 'z_29', 'z_59', 'z_89', 'z_119', 'z_149', 'z_179', 'z_209', 'z_239', 'z_269']]

y = dataset[['sitting', 'standing', 'walking', 'grazing']]  # Replace 'behavior' with the actual column name containing behavior labels

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize a RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Print the results
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_rep)
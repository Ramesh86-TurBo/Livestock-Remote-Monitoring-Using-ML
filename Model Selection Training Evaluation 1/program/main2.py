import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load your labeled dataset
dataset = pd.read_csv('final3.csv')

# Separate features (X) and labels (y)
X = dataset[['x', 'y', 'z']]
y = dataset[['sitting', 'standing', 'walking', 'grazing']]

# Convert binary labels to class indices
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y.idxmax(axis=1))

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Initialize MinMaxScaler
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize XGBClassifier
model = XGBClassifier(objective='multi:softmax', num_classes=4, random_state=42)

# Train the model
model.fit(X_train_scaled, y_train)

# Evaluate the model using cross-validation
cv_accuracy = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='accuracy')
print(f'Cross-Validation Accuracy: {cv_accuracy.mean():.2f}')

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Print the results
print(f'Test Set Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_rep)

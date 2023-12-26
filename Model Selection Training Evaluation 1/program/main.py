import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load your labeled dataset
dataset = pd.read_csv('final2.csv')

# Separate features (X) and labels (y)
X = dataset[['x', 'y', 'z']]
y = dataset[['sitting', 'standing', 'walking', 'grazing']]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize a KNeighborsClassifier
knn_model = KNeighborsClassifier(n_neighbors=247)

# Train the model
knn_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Print the results
print(f'Test Set Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_rep)

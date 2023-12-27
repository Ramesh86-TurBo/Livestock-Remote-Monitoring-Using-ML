import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load your labeled dataset
dataset = pd.read_csv('final2.csv')

# Separate features (X) and labels (y)
X = dataset[['x', 'y', 'z']]
y = dataset[['sitting', 'standing', 'walking', 'grazing']]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Flatten the multi-dimensional y arrays
y_train_flat = y_train.values.ravel()
y_test_flat = y_test.values.ravel()

# Ensure the number of samples in X_train matches the number of samples in y_train_flat
X_train, X_train_ignore, y_train_flat, y_train_ignore = train_test_split(X_train, y_train_flat, test_size=0.8, random_state=42)

# Initialize an SVC (Support Vector Classification) model with hyperparameters
svm_model = SVC(
    C=1.0,             # Regularization parameter (default=1.0)
    kernel='rbf',       # Kernel type: 'linear', 'poly', 'rbf', 'sigmoid', etc. (default='rbf')
    gamma='scale',     # Kernel coefficient for 'rbf', 'poly', and 'sigmoid' (default='scale')
    degree=3,           # Degree of the polynomial kernel function ('poly' only, default=3)
    random_state=42,    # Seed for random number generation (default=None)
)

# Train the model
svm_model.fit(X_train, y_train_flat)

# Make predictions on the test set
y_pred = svm_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test_flat, y_pred)
classification_rep = classification_report(y_test_flat, y_pred)

# Print the results
print(f'Test Set Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_rep)

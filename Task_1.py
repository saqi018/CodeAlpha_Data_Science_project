import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load the Iris dataset
print("Loading dataset...")
iris = load_iris()
X = iris.data  # The features: sepal length, sepal width, petal length, petal width
y = iris.target  # The target: the species (setosa, versicolor, virginica)

# 2. Split the data into Training (80%) and Testing (20%) sets
# random_state ensures we get the same split every time we run the code
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 3. Initialize and Train the Machine Learning Model
print("Training the Random Forest model...")
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. Make predictions using the test data
print("Making predictions on test data...")
y_pred = model.predict(X_test)

# 5. Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"\n--- Results ---")
print(f"Model Accuracy: {accuracy * 100:.2f}%\n")

print("Detailed Classification Report:")
# This breaks down the accuracy for each specific flower type
print(classification_report(y_test, y_pred, target_names=iris.target_names))

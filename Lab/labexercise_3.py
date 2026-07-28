from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create Decision Tree using ID3 (Entropy)
model = DecisionTreeClassifier(criterion="entropy")

# Train the model
model.fit(X, y)

# New sample for prediction
sample = [[5.1, 3.5, 1.4, 0.2]]

# Predict
prediction = model.predict(sample)

print("Predicted Class:", iris.target_names[prediction[0]])

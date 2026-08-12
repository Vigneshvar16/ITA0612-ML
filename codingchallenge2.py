# ---------------------------------------------------------
# Logistic Regression using Gradient Descent
# ---------------------------------------------------------
# Aim:
# To implement Logistic Regression for binary classification
# using Gradient Descent and predict the class of test data.
# The program also displays sigmoid outputs and accuracy.
# ---------------------------------------------------------

import math


# ---------------------------------------------------------
# Sigmoid Function
# ---------------------------------------------------------
# Converts the linear output into a probability between 0 and 1.
#
# sigmoid(z) = 1 / (1 + e^(-z))
#
def sigmoid(z):

    # Prevent overflow when z becomes very negative
    if z < -500:
        return 0.0

    # Prevent unnecessary overflow for very large positive z
    if z > 500:
        return 1.0

    return 1 / (1 + math.exp(-z))


# ---------------------------------------------------------
# Training Dataset
# ---------------------------------------------------------
# X contains the input feature values.
# y contains the corresponding class labels.
#
# Class 0 -> Negative class
# Class 1 -> Positive class

X_train = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
]

y_train = [
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1
]


# ---------------------------------------------------------
# Test Dataset
# ---------------------------------------------------------

X_test = [
    [2.5],
    [4.5],
    [6.5],
    [8]
]

y_test = [
    0,
    1,
    1,
    1
]


# ---------------------------------------------------------
# Get Learning Rate and Number of Iterations
# ---------------------------------------------------------

learning_rate = float(input("Enter learning rate (example 0.1): "))
epochs = int(input("Enter number of iterations (example 1000): "))


# ---------------------------------------------------------
# Validate User Input
# ---------------------------------------------------------

if learning_rate <= 0:
    print("Learning rate must be greater than 0.")
    exit()

if epochs <= 0:
    print("Number of iterations must be greater than 0.")
    exit()


# ---------------------------------------------------------
# Initialize Weight and Bias
# ---------------------------------------------------------

weight = 0.0
bias = 0.0

n = len(X_train)


# ---------------------------------------------------------
# Gradient Descent Training
# ---------------------------------------------------------

for epoch in range(epochs):

    # Initialize gradients
    weight_gradient = 0.0
    bias_gradient = 0.0

    # Process every training sample
    for i in range(n):

        # Get input feature
        x = X_train[i][0]

        # Get actual class
        actual = y_train[i]

        # Calculate linear combination
        # z = wx + b
        z = weight * x + bias

        # Calculate probability using sigmoid
        prediction = sigmoid(z)

        # Calculate error
        error = prediction - actual

        # Calculate gradients
        weight_gradient += error * x
        bias_gradient += error

    # Find average gradient
    weight_gradient = weight_gradient / n
    bias_gradient = bias_gradient / n

    # Update weight
    weight = weight - learning_rate * weight_gradient

    # Update bias
    bias = bias - learning_rate * bias_gradient


# ---------------------------------------------------------
# Display Trained Model
# ---------------------------------------------------------

print("\nTraining Completed!")

print("Final Weight:", round(weight, 4))
print("Final Bias:", round(bias, 4))


# ---------------------------------------------------------
# Display Sigmoid Outputs for Test Data
# ---------------------------------------------------------

print("\nSigmoid Function Outputs")
print("------------------------------------------")

for i in range(len(X_test)):

    x = X_test[i][0]

    # Calculate linear output
    z = weight * x + bias

    # Calculate probability
    probability = sigmoid(z)

    print(
        "Input:", x,
        " Sigmoid Output:", round(probability, 4)
    )


# ---------------------------------------------------------
# Prediction and Classification
# ---------------------------------------------------------
# If probability >= 0.5 -> Class 1
# If probability < 0.5  -> Class 0

print("\nClassification Results")
print("------------------------------------------")

correct = 0

for i in range(len(X_test)):

    x = X_test[i][0]
    actual = y_test[i]

    # Calculate linear output
    z = weight * x + bias

    # Calculate sigmoid probability
    probability = sigmoid(z)

    # Convert probability into class
    if probability >= 0.5:
        predicted = 1
    else:
        predicted = 0

    # Check prediction
    if predicted == actual:
        correct += 1

    print(
        "Input:", x,
        "| Actual:", actual,
        "| Probability:", round(probability, 4),
        "| Predicted:", predicted
    )


# ---------------------------------------------------------
# Calculate Accuracy
# ---------------------------------------------------------

accuracy = (correct / len(X_test)) * 100

print("\nAccuracy:", round(accuracy, 2), "%")


# ---------------------------------------------------------
# Learning Rate Discussion
# ---------------------------------------------------------

print("\nLearning Rate Discussion")
print("------------------------------------------")

print("1. Small learning rate:")
print("   - Convergence is slow.")
print("   - More iterations may be required.")

print("2. Suitable learning rate:")
print("   - Provides stable convergence.")
print("   - Gives good performance.")

print("3. Very large learning rate:")
print("   - May overshoot the minimum.")
print("   - Can make training unstable.")

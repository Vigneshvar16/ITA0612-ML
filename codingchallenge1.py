# ---------------------------------------------------------
# Program: K-Nearest Neighbour (KNN) Algorithm
# ---------------------------------------------------------
# Aim:
# To implement the K-Nearest Neighbour (KNN) algorithm
# using Euclidean distance and classify a test instance.
# The program allows the user to enter the value of K
# and calculates the prediction accuracy.
# ---------------------------------------------------------

# Import required libraries
import math

# ---------------------------------------------------------
# Step 1: Create a small training dataset
# ---------------------------------------------------------
# Each data point contains:
# [Feature 1, Feature 2, Class Label]

training_data = [
    [1, 2, "A"],
    [2, 3, "A"],
    [3, 1, "A"],
    [6, 5, "B"],
    [7, 7, "B"],
    [8, 6, "B"]
]

# ---------------------------------------------------------
# Step 2: Function to calculate Euclidean distance
# ---------------------------------------------------------
def euclidean_distance(point1, point2):

    # Calculate the difference between the two features
    x_difference = point1[0] - point2[0]
    y_difference = point1[1] - point2[1]

    # Euclidean distance formula:
    # distance = sqrt((x1-x2)^2 + (y1-y2)^2)

    distance = math.sqrt(
        x_difference ** 2 +
        y_difference ** 2
    )

    return distance


# ---------------------------------------------------------
# Step 3: KNN prediction function
# ---------------------------------------------------------
def knn_predict(test_point, k):

    distances = []

    # Calculate distance between test point
    # and every point in the training dataset
    for data in training_data:

        point = data[:2]
        label = data[2]

        distance = euclidean_distance(test_point, point)

        # Store distance and corresponding class
        distances.append((distance, label))

    # Sort points based on distance
    distances.sort(key=lambda x: x[0])

    # Select the K nearest neighbours
    nearest_neighbors = distances[:k]

    print("\nNearest Neighbours:")

    for distance, label in nearest_neighbors:
        print("Distance =", round(distance, 2),
              "Class =", label)

    # Count the number of occurrences of each class
    class_count = {}

    for distance, label in nearest_neighbors:

        if label not in class_count:
            class_count[label] = 0

        class_count[label] += 1

    # Select the class having the highest count
    predicted_class = max(
        class_count,
        key=class_count.get
    )

    return predicted_class


# ---------------------------------------------------------
# Step 4: Get K value from the user
# ---------------------------------------------------------

k = int(input("Enter the value of K: "))

# Check whether K is valid
if k <= 0 or k > len(training_data):

    print("Invalid value of K!")

else:

    # -----------------------------------------------------
    # Step 5: Get test instance from the user
    # -----------------------------------------------------

    x = float(input("Enter Feature 1 of test instance: "))
    y = float(input("Enter Feature 2 of test instance: "))

    test_point = [x, y]

    # -----------------------------------------------------
    # Step 6: Predict the class of the test instance
    # -----------------------------------------------------

    predicted_class = knn_predict(test_point, k)

    print("\nTest Instance:", test_point)

    print("Predicted Class:", predicted_class)

    # -----------------------------------------------------
    # Step 7: Calculate accuracy
    # -----------------------------------------------------
    # We test all training points using leave-one-out
    # classification to estimate accuracy.

    correct_predictions = 0

    for i in range(len(training_data)):

        test = training_data[i][:2]
        actual_class = training_data[i][2]

        # Create a temporary dataset without the test point
        original_data = training_data.copy()

        training_data.pop(i)

        # Make prediction
        prediction = knn_predict(test, min(k, len(training_data)))

        # Compare prediction with actual class
        if prediction == actual_class:
            correct_predictions += 1

        # Restore original dataset
        training_data = original_data

    # Calculate accuracy
    accuracy = (
        correct_predictions /
        len(training_data)
    ) * 100

    print("\nAccuracy:",
          round(accuracy, 2), "%")

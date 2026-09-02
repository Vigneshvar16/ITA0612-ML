# Program E: Performance Analysis and Recommendation
# Overfitting / underfitting analysis across different tree depths
# Run 01_data_preparation.py first to create train_data.csv and test_data.csv

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

train_data = pd.read_csv("train_data.csv")
test_data = pd.read_csv("test_data.csv")

attributes = ["temperature", "vibration", "rotational_speed",
              "torque", "pressure", "operating_hours"]
target = "condition"

X_train = train_data[attributes]
y_train = train_data[target]
X_test = test_data[attributes]
y_test = test_data[target]

print(f"{'Depth':<8}{'Train Accuracy':<18}{'Test Accuracy':<15}")

results = []
for depth in range(1, 16):
    model = DecisionTreeClassifier(
        criterion="entropy",
        max_depth=depth,
        min_samples_leaf=5,
        random_state=42
    )
    model.fit(X_train, y_train)

    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))
    results.append((depth, train_acc, test_acc))

    print(f"{depth:<8}{train_acc:<18.4f}{test_acc:<15.4f}")

# ----------------------------------------------------
# Pick the depth with the best test accuracy
# ----------------------------------------------------

best_depth, best_train, best_test = max(results, key=lambda r: r[2])

print(f"\nBest depth on test data: {best_depth}")
print(f"Train accuracy at best depth: {best_train:.4f}")
print(f"Test accuracy at best depth: {best_test:.4f}")

gap = best_train - best_test
print(f"\nTrain-test accuracy gap: {gap:.4f}")

if gap > 0.15:
    print("Large gap -> deeper trees are overfitting the data.")
elif best_test < 0.75:
    print("Both accuracies are low -> tree may be underfitting.")
else:
    print("Train and test accuracy are close -> model generalises well.")

print(f"\nRecommendation: use max_depth = {best_depth} for the final model,")
print("since it gives the best trade-off between accuracy and tree complexity.")

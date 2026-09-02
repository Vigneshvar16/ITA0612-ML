# Program D: Model Evaluation and Interpretation
# Run 01_data_preparation.py first to create train_data.csv and test_data.csv

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)

train_data = pd.read_csv("train_data.csv")
test_data = pd.read_csv("test_data.csv")

attributes = ["temperature", "vibration", "rotational_speed",
              "torque", "pressure", "operating_hours"]
target = "condition"

X_train = train_data[attributes]
y_train = train_data[target]
X_test = test_data[attributes]
y_test = test_data[target]

tree_model = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=4,
    min_samples_leaf=5,
    random_state=42
)
tree_model.fit(X_train, y_train)

y_pred = tree_model.predict(X_test)

# ----------------------------------------------------
# Evaluation metrics
# ----------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="macro", zero_division=0)
recall = recall_score(y_test, y_pred, average="macro", zero_division=0)
f1 = f1_score(y_test, y_pred, average="macro", zero_division=0)

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1-score  : {f1:.4f}")

print("\nConfusion Matrix:")
labels = sorted(y_test.unique())
cm = confusion_matrix(y_test, y_pred, labels=labels)
cm_df = pd.DataFrame(cm, index=labels, columns=labels)
print(cm_df)

print("\nFull classification report:")
print(classification_report(y_test, y_pred, zero_division=0))

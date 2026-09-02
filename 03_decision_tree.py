# Program C: Decision Tree Construction and Implementation
# Run 01_data_preparation.py first to create train_data.csv and test_data.csv

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import matplotlib.pyplot as plt

train_data = pd.read_csv("train_data.csv")
test_data = pd.read_csv("test_data.csv")

attributes = ["temperature", "vibration", "rotational_speed",
              "torque", "pressure", "operating_hours"]
target = "condition"

X_train = train_data[attributes]
y_train = train_data[target]
X_test = test_data[attributes]
y_test = test_data[target]

# ----------------------------------------------------
# Build the Decision Tree (Information Gain = entropy criterion)
# ----------------------------------------------------

tree_model = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=4,
    min_samples_leaf=5,
    random_state=42
)
tree_model.fit(X_train, y_train)

print("Decision tree built successfully.")
print("Tree depth:", tree_model.get_depth())
print("Number of leaves:", tree_model.get_n_leaves())

# ----------------------------------------------------
# Print the tree as text rules (splitting/stopping shown)
# ----------------------------------------------------

rules_text = export_text(tree_model, feature_names=attributes)
print("\nDecision Tree structure:\n")
print(rules_text)

# ----------------------------------------------------
# Visualise the tree and save as an image
# ----------------------------------------------------

plt.figure(figsize=(18, 10))
plot_tree(
    tree_model,
    feature_names=attributes,
    class_names=tree_model.classes_,
    filled=False,
    fontsize=8
)
plt.savefig("decision_tree.png", dpi=150, bbox_inches="tight")
print("\nTree image saved as decision_tree.png")

# ----------------------------------------------------
# Extract IF-THEN decision rules manually from the tree
# ----------------------------------------------------

def get_rules(tree, feature_names, class_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != -2 else "undefined"
        for i in tree_.feature
    ]
    rules = []

    def recurse(node, conditions):
        if tree_.feature[node] != -2:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            recurse(tree_.children_left[node],
                    conditions + [f"{name} <= {threshold:.2f}"])
            recurse(tree_.children_right[node],
                    conditions + [f"{name} > {threshold:.2f}"])
        else:
            class_index = tree_.value[node].argmax()
            predicted_class = class_names[class_index]
            rule = "IF " + " AND ".join(conditions) + f" THEN {predicted_class}"
            rules.append(rule)

    recurse(0, [])
    return rules

print("\nExtracted IF-THEN decision rules:\n")
for rule in get_rules(tree_model, attributes, tree_model.classes_):
    print(rule)

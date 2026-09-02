# Program B: Concept Representation and Heuristic Search
# Attribute selection using Information Gain (entropy based)
# Run 01_data_preparation.py first to create maintenance_data.csv

import pandas as pd
import numpy as np

data = pd.read_csv("maintenance_data.csv")

target = "condition"
attributes = ["temperature", "vibration", "rotational_speed",
              "torque", "pressure", "operating_hours"]

# ----------------------------------------------------
# Entropy of the target concept
# ----------------------------------------------------

def entropy(column):
    probs = column.value_counts(normalize=True)
    return -np.sum(probs * np.log2(probs))

total_entropy = entropy(data[target])
print("Hypothesis space: all possible decision trees over the")
print("6 attributes, each attribute split at some threshold.")
print("Inductive bias: prefer shorter trees and attributes")
print("that reduce entropy the most (ID3 preference bias).\n")

print(f"Entropy of target concept (condition): {total_entropy:.4f}\n")

# ----------------------------------------------------
# Information Gain for each continuous attribute
# (attribute is binned into 2 groups using its median,
#  same idea as a threshold split in a decision tree)
# ----------------------------------------------------

def information_gain(data, attribute, target):
    median_val = data[attribute].median()
    left = data[data[attribute] <= median_val]
    right = data[data[attribute] > median_val]

    weighted_entropy = (
        (len(left) / len(data)) * entropy(left[target]) +
        (len(right) / len(data)) * entropy(right[target])
    )
    gain = entropy(data[target]) - weighted_entropy
    return gain, median_val

print("Information Gain for each attribute (split at median):\n")
gains = {}
for attr in attributes:
    gain, threshold = information_gain(data, attr, target)
    gains[attr] = gain
    print(f"{attr:20s}  threshold={threshold:8.2f}  gain={gain:.4f}")

print("\nAttributes ranked by Information Gain (best first):")
ranked = sorted(gains.items(), key=lambda x: x[1], reverse=True)
for attr, gain in ranked:
    print(f"{attr:20s}  {gain:.4f}")

print(f"\nBest attribute for the root node: {ranked[0][0]}")

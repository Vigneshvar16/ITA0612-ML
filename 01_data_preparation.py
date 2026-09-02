# Program A: Dataset Preparation and Problem Formulation
# Predictive Maintenance - Decision Tree Learning

import pandas as pd
import numpy as np

np.random.seed(42)

# ----------------------------------------------------
# Step 1: Create the industrial equipment dataset
# (In a real project this would be read from a company
#  sensor log. Here it is generated with the same value
#  ranges as real motor/pump/compressor sensor data.)
# ----------------------------------------------------

n = 500

temperature = np.random.normal(70, 15, n)          # deg C
vibration = np.random.normal(2.5, 1.2, n)           # mm/s
rotational_speed = np.random.normal(1500, 200, n)   # rpm
torque = np.random.normal(40, 10, n)                # Nm
pressure = np.random.normal(5, 1.5, n)               # bar
operating_hours = np.random.normal(8000, 3000, n)   # hrs

data = pd.DataFrame({
    "temperature": temperature,
    "vibration": vibration,
    "rotational_speed": rotational_speed,
    "torque": torque,
    "pressure": pressure,
    "operating_hours": operating_hours
})

# ----------------------------------------------------
# Step 2: Define target concept (maintenance condition)
# Rule-based labelling with noise, similar to how real
# maintenance logs are derived from thresholds.
# ----------------------------------------------------

def label_condition(row):
    risk_score = 0
    if row.temperature > 85:
        risk_score += 1
    if row.vibration > 4:
        risk_score += 1
    if row.operating_hours > 11000:
        risk_score += 1
    if row.pressure > 7.5 or row.pressure < 2:
        risk_score += 1

    if risk_score >= 2:
        return "Failure Risk"
    elif risk_score == 1:
        return "Preventive Maintenance Required"
    else:
        return "Normal Operation"

data["condition"] = data.apply(label_condition, axis=1)

# Add a bit of label noise, since real maintenance logs are
# not perfectly clean (technician judgement, sensor drift etc.)
noise_idx = np.random.choice(data.index, size=40, replace=False)
noise_labels = np.random.choice(
    ["Normal Operation", "Preventive Maintenance Required", "Failure Risk"],
    size=40
)
data.loc[noise_idx, "condition"] = noise_labels

# ----------------------------------------------------
# Step 3: Introduce a few missing values (real sensor
# logs usually have some missing readings) and clean them
# ----------------------------------------------------

for col in ["temperature", "vibration", "pressure"]:
    idx = np.random.choice(data.index, size=8, replace=False)
    data.loc[idx, col] = np.nan

print("Missing values before cleaning:")
print(data.isnull().sum())

data = data.fillna(data.mean(numeric_only=True))

print("\nMissing values after cleaning:")
print(data.isnull().sum())

# ----------------------------------------------------
# Step 4: Basic dataset summary
# ----------------------------------------------------

print("\nDataset shape:", data.shape)
print("\nTarget class distribution:")
print(data["condition"].value_counts())

print("\nFirst 5 rows:")
print(data.head())

# ----------------------------------------------------
# Step 5: Train/test split and save for the other programs
# ----------------------------------------------------

data = data.sample(frac=1, random_state=42).reset_index(drop=True)
split_point = int(0.8 * len(data))
train_data = data.iloc[:split_point]
test_data = data.iloc[split_point:]

data.to_csv("maintenance_data.csv", index=False)
train_data.to_csv("train_data.csv", index=False)
test_data.to_csv("test_data.csv", index=False)

print("\nTraining samples:", len(train_data))
print("Testing samples:", len(test_data))
print("\nSaved maintenance_data.csv, train_data.csv, test_data.csv")

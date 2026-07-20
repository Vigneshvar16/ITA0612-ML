# FIND-S Algorithm in Python
# Machine Learning Lab

import pandas as pd

# Training Dataset
data = {
    'Sky': ['Sunny', 'Sunny', 'Rainy', 'Sunny'],
    'AirTemp': ['Warm', 'Warm', 'Cold', 'Warm'],
    'Humidity': ['Normal', 'High', 'High', 'High'],
    'Wind': ['Strong', 'Strong', 'Strong', 'Strong'],
    'Water': ['Warm', 'Warm', 'Warm', 'Cool'],
    'Forecast': ['Same', 'Same', 'Change', 'Change'],
    'EnjoySport': ['Yes', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)

print("Training Data:\n")
print(df)

# Features and Target
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Initialize the most specific hypothesis
hypothesis = ['0'] * len(X[0])

# FIND-S Algorithm
for i in range(len(X)):
    if y[i] == "Yes":
        for j in range(len(hypothesis)):
            if hypothesis[j] == '0':
                hypothesis[j] = X[i][j]
            elif hypothesis[j] != X[i][j]:
                hypothesis[j] = '?'

print("\nFinal Most Specific Hypothesis:")
print(hypothesis)
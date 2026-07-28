data = [
    ["Sunny","Warm","Normal","Strong","Warm","Same","Yes"],
    ["Sunny","Warm","High","Strong","Warm","Same","Yes"],
    ["Rainy","Cold","High","Strong","Warm","Change","No"],
    ["Sunny","Warm","High","Strong","Cool","Change","Yes"]
]

print("Training Data:")
for row in data:
    print(row)

# Initialize S and G
num_attributes = len(data[0]) - 1
S = ['0'] * num_attributes
G = ['?'] * num_attributes

# Candidate Elimination
for row in data:
    attributes = row[:-1]
    target = row[-1]

    if target.lower() == "yes":
        for i in range(num_attributes):
            if S[i] == '0':
                S[i] = attributes[i]
            elif S[i] != attributes[i]:
                S[i] = '?'
    else:
        for i in range(num_attributes):
            if S[i] != attributes[i]:
                G[i] = S[i]
            else:
                G[i] = '?'

print("\nFinal Specific Hypothesis (S):")
print(S)

print("\nFinal General Hypothesis (G):")
print(G)
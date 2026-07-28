from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load Diabetes dataset
data = load_diabetes()
X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Display Mean Squared Error
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Predict for one sample
sample = [X[0]]
prediction = model.predict(sample)

print("Predicted Value:", prediction[0])

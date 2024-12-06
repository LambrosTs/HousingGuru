import pickle
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Load the dataset
data = fetch_california_housing(as_frame=True)
X = data.data  # Features
y = data.target  # Target variable (house prices)

# 2. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train a simple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Save the trained model to a file named "model.pkl"
with open("model.pkl", "wb") as file:  # Notice the 'wb' (write-binary) mode
    pickle.dump(model, file)

print("Model trained and saved to model.pkl")

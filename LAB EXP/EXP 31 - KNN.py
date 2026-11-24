from sklearn.neighbors import KNeighborsClassifier

# Sample data
X = [[1, 2], [2, 3], [3, 4],
     [6, 7], [7, 8], [8, 9]]

y = ["A", "A", "A", "B", "B", "B"]

# Create the model
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X, y)

# Predict the class
prediction = model.predict([[4, 5]])

print("Predicted class:", prediction[0])

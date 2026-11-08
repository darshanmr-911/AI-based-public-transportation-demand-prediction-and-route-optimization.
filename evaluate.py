import pandas as pd
import joblib
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_excel(
    "Dataset/Harohalli_Passenger_Details.xlsx",
    header=2
)

df = df.dropna(
    subset=[
        "FROM",
        "TO",
        "SERVICE TYPE",
        "INTERSTATE/\nINTRASTATE",
        "Total\n(Passengers)"
    ]
)

features = [
    "FROM",
    "TO",
    "SERVICE TYPE",
    "INTERSTATE/\nINTRASTATE"
]

X = df[features]
y = df["Total\n(Passengers)"]

# Same split used during training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Load trained model
model = joblib.load("models/passenger_model.pkl")

# Predict
predictions = model.predict(X_test)

# Compare results
results = pd.DataFrame({
    "FROM": X_test["FROM"].values,
    "TO": X_test["TO"].values,
    "Actual Passengers": y_test.values,
    "Predicted Passengers": predictions.round().astype(int)
})

results["Difference"] = (
    results["Actual Passengers"] -
    results["Predicted Passengers"]
).abs()

print(results.to_string(index=False))

# Save results
results.to_csv("evaluation_results.csv", index=False)

print("\nEvaluation completed!")
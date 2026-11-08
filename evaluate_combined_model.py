import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset and trained model
df = pd.read_csv("Dataset/actual_route_passengers_HRH_RMN.csv")
model = joblib.load("models/combined_passenger_model.pkl")

features = [
    "depot",
    "from",
    "to",
    "service_type",
    "interstate_type"
]

X = df[features]
y = df["total_passengers"]

# Recreate the same test split used during training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

predictions = model.predict(X_test)

results = X_test[["depot", "from", "to"]].copy()
results["actual"] = y_test
results["predicted"] = predictions
results["absolute_error"] = (
    results["actual"] - results["predicted"]
).abs()

print("===== OVERALL MODEL PERFORMANCE =====")
print("MAE:", round(mean_absolute_error(y_test, predictions), 2))
print("RMSE:", round(mean_squared_error(y_test, predictions) ** 0.5, 2))
print("R2:", round(r2_score(y_test, predictions), 3))

print("\n===== DEPOT-WISE PERFORMANCE =====")

for depot, group in results.groupby("depot"):
    print(f"\n{depot}")
    print("Test records:", len(group))
    print("MAE:", round(group["absolute_error"].mean(), 2))

print("\n===== LARGEST PREDICTION ERRORS =====")
print(
    results.sort_values("absolute_error", ascending=False)
    .head(5)
    .to_string(index=False)
)

results.to_csv("Dataset/model_evaluation_results.csv", index=False)

print("\nEvaluation results saved!")

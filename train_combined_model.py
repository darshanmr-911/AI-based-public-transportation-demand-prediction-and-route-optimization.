import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load actual route data
df = pd.read_csv(
    "Dataset/actual_route_passengers_HRH_RMN.csv"
)

features = [
    "depot",
    "from",
    "to",
    "service_type",
    "interstate_type"
]

target = "total_passengers"

X = df[features]
y = df[target]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Encode categorical features
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            features
        )
    ]
)

# Build model
model = Pipeline([
    ("preprocessor", preprocessor),
    (
        "regressor",
        RandomForestRegressor(
            n_estimators=200,
            random_state=42
        )
    )
])

# Train
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

print("===== COMBINED MODEL RESULTS =====")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("MAE:", round(mean_absolute_error(y_test, predictions), 2))
print("RMSE:", round(mean_squared_error(y_test, predictions) ** 0.5, 2))
print("R2 Score:", round(r2_score(y_test, predictions), 3))

# Save model
joblib.dump(model, "models/combined_passenger_model.pkl")

print("\nModel saved successfully!")
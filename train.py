
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_excel(
    "Dataset/Harohalli_Passenger_Details.xlsx",
    header=2
)

# Clean dataset
df = df.dropna(
    subset=[
        "FROM",
        "TO",
        "SERVICE TYPE",
        "INTERSTATE/\nINTRASTATE",
        "Total\n(Passengers)"
    ]
)

# Features and target
features = [
    "FROM",
    "TO",
    "SERVICE TYPE",
    "INTERSTATE/\nINTRASTATE"
]

X = df[features]
y = df["Total\n(Passengers)"]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("categorical", OneHotEncoder(handle_unknown="ignore"), features)
    ]
)

# Define model BEFORE using it
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ))
])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("Mean Absolute Error:", round(mae, 2))

# Save model
joblib.dump(model, "models/passenger_model.pkl")

print("Model trained successfully!")

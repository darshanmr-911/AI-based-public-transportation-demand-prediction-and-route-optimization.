
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 1. Load dataset
df = pd.read_excel(
    "Dataset/Harohalli_Passenger_Details.xlsx",
    header=2
)

# 2. Clean dataset
df = df.dropna(
    subset=[
        "FROM",
        "TO",
        "SERVICE TYPE",
        "Total\n(Passengers)"
    ]
)

# 3. Select input features
features = [
    "FROM",
    "TO",
    "SERVICE TYPE",
    "INTERSTATE/\nINTRASTATE"
]

X = df[features]

# 4. Select target
y = pd.to_numeric(
    df["Total\n(Passengers)"]
)

# 5. Convert categorical data
preprocessor = ColumnTransformer([
    (
        "encoder",
        OneHotEncoder(handle_unknown="ignore"),
        features
    )
])

# 6. Create Random Forest model
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ))
])

# 7. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 8. Train model
model.fit(X_train, y_train)

# 9. Evaluate model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("Mean Absolute Error:", round(mae, 2))

# 10. Save model
joblib.dump(model, "models/passenger_model.pkl")

print("Model trained successfully!")

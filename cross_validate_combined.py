import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GroupKFold, cross_val_score

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

X = df[features]
y = df["total_passengers"]

# Keep records for the same route together
groups = (
    df["depot"].astype(str) + "_" +
    df["from"].astype(str) + "_" +
    df["to"].astype(str) + "_" +
    df["service_type"].astype(str) + "_" +
    df["interstate_type"].astype(str)
)

preprocessor = ColumnTransformer([
    (
        "categorical",
        OneHotEncoder(handle_unknown="ignore"),
        features
    )
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ))
])

cv = GroupKFold(n_splits=5)

scores = cross_val_score(
    model,
    X,
    y,
    cv=cv,
    groups=groups,
    scoring="neg_mean_absolute_error"
)

mae_scores = -scores

print("===== 5-FOLD CROSS-VALIDATION =====")

for i, score in enumerate(mae_scores, start=1):
    print(f"Fold {i} MAE: {score:.2f}")

print("\nAverage MAE:", round(mae_scores.mean(), 2))
print("Standard deviation:", round(mae_scores.std(), 2))
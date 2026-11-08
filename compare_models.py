import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GroupKFold, cross_val_score

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("Dataset/actual_route_passengers_HRH_RMN.csv")

features = [
    "depot",
    "from",
    "to",
    "service_type",
    "interstate_type"
]

X = df[features]
y = df["total_passengers"]

groups = (
    df["depot"].astype(str) + "_" +
    df["from"].astype(str) + "_" +
    df["to"].astype(str) + "_" +
    df["service_type"].astype(str) + "_" +
    df["interstate_type"].astype(str)
)

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), features)
])

models = {
    "Random Forest": RandomForestRegressor(
        n_estimators=200, random_state=42
    ),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(random_state=42)
}

cv = GroupKFold(n_splits=5)

print("===== MODEL COMPARISON =====")

for name, algorithm in models.items():
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", algorithm)
    ])

    scores = -cross_val_score(
        pipeline,
        X,
        y,
        groups=groups,
        cv=cv,
        scoring="neg_mean_absolute_error"
    )

    print(f"\n{name}")
    print("Fold MAE:", scores.round(2))
    print("Average MAE:", round(scores.mean(), 2))
    
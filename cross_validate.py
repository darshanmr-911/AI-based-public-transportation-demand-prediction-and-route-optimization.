import pandas as pd
import joblib

from sklearn.model_selection import KFold, cross_val_score

# Load dataset
df = pd.read_excel(
    "Dataset/Harohalli_Passenger_Details.xlsx",
    header=2
)

# Clean data
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

# Load model pipeline
model = joblib.load("models/passenger_model.pkl")

# 5-fold cross-validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(
    model,
    X,
    y,
    cv=kfold,
    scoring="neg_mean_absolute_error"
)

mae_scores = -scores

print("MAE for each fold:")
for i, score in enumerate(mae_scores, start=1):
    print(f"Fold {i}: {score:.2f}")

print("\nAverage MAE:", round(mae_scores.mean(), 2))
print("Standard Deviation:", round(mae_scores.std(), 2))
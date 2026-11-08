
import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/passenger_model.pkl")

# New route details
data = pd.DataFrame([{
    "FROM": "Kalasipalya",
    "TO": "Malavalli",
    "SERVICE TYPE": "Vegadoota",
    "INTERSTATE/\nINTRASTATE": "INTRA STATE"
}])

# Predict
prediction = model.predict(data)

print("Predicted Passenger Count:", round(prediction[0]))

import joblib
import pandas as pd

model = joblib.load("models/combined_passenger_model.pkl")

print("===== PASSENGER DEMAND PREDICTION =====")

depot = input("Depot (HRH/RMN): ").upper()
start = input("Starting location: ")
destination = input("Destination: ")
service = input("Service type: ")
travel_type = input("INTRA STATE or INTER STATE: ").upper()

route = pd.DataFrame([{
    "depot": depot,
    "from": start,
    "to": destination,
    "service_type": service,
    "interstate_type": travel_type
}])

prediction = model.predict(route)[0]

print("\n===== PREDICTION RESULT =====")
print("Estimated monthly passengers:", round(prediction))

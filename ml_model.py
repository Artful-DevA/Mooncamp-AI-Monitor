import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(42)

normal_data = pd.DataFrame({
    "Pressure": rng.normal(101, 0.3, 300),
    "Temperature": rng.normal(22, 0.5, 300),
    "Oxygen": rng.normal(21, 0.1, 300),
    "Power": rng.normal(5, 0.15, 300)
})

print(normal_data.head())

pressure_model = IsolationForest(contamination=0.05, random_state=42)
pressure_model.fit(normal_data[["Pressure"]])

test_pressure = pd.DataFrame({"Pressure": [101, 100.5]})
results = pressure_model.predict(test_pressure)

print("Pressure predictions:", results)

temperature_model = IsolationForest(contamination=0.05, random_state=42)
temperature_model.fit(normal_data[["Temperature"]])

test_temperature = pd.DataFrame({"Temperature": [22, 21.5]})
results = temperature_model.predict(test_temperature)

print("Temperature predictions:", results)
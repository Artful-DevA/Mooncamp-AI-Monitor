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
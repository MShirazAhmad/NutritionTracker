global MassAnalytics
import pandas as pd

MassAnalytics = pd.read_csv("MassAnalytics.csv")
MassAnalytics.Date = pd.to_datetime(MassAnalytics.Date)
MassAnalytics["Mass"] = MassAnalytics["Mass"].astype(str)
print(MassAnalytics)
MassAnalytics=MassAnalytics.sort_values('Date').drop_duplicates('Mass',keep='last')
MassAnalytics=MassAnalytics.dropna()

import matplotlib.pyplot as plt




plt.plot(MassAnalytics.Date, MassAnalytics.Mass)
plt.set_xlabel("Time")
plt.set_ylabel("Mass")
plt.show()

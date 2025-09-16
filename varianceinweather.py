import pandas as pd
import numpy as np

# Example weather data
# Columns: "TemperatureC", "month", "day", "hour"
data = {
    "TemperatureC": [5, 7, 6, 15, 16, 15, 20, 21, 19, 25, 26, 24],
    "month":       [1, 1, 1, 6, 6, 6, 7, 7, 7, 12, 12, 12],
    "day":         [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    "hour":        [8, 12, 16, 8, 12, 16, 8, 12, 16, 8, 12, 16]
}

# Create DataFrame
london_data = pd.DataFrame(data)

# -----------------------------
# Overall statistics
# -----------------------------
temp = london_data["TemperatureC"]

average_temp = np.mean(temp)
temperature_var = np.var(temp)
temperature_standard_deviation = np.std(temp)

print("Overall Temperature Statistics:")
print("Average:", average_temp)
print("Variance:", temperature_var)
print("Standard Deviation:", temperature_standard_deviation)

# -----------------------------
# Filtering by month
# -----------------------------
# June (month = 6)
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]

# July (month = 7)
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]

# Mean temperatures
print("\nMean Temperatures:")
print("June:", np.mean(june))
print("July:", np.mean(july))

# Standard deviations
print("\nStandard Deviations:")
print("June:", np.std(june))
print("July:", np.std(july))

# -----------------------------
# Loop through all months (example)
# -----------------------------
print("\nMonthly Summary:")
for i in sorted(london_data["month"].unique()):
    month_temp = london_data.loc[london_data["month"] == i]["TemperatureC"]
    print(f"Month {i}: mean = {np.mean(month_temp)}, std = {np.std(month_temp)}")

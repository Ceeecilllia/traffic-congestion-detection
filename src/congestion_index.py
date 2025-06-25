import pandas as pd
import numpy as np
import os

# Load the vehicle counts data
data_path = os.path.join("data", "vehicle_counts.csv")
df = pd.read_csv(data_path)

# Simulate GPS coordinates for each frame (just for visualization purposes)
# Here we add small random noise around a center location (e.g., Times Square)
np.random.seed(42)
df["latitude"] = 40.758 + np.random.normal(0, 0.0005, size=len(df))
df["longitude"] = -73.9855 + np.random.normal(0, 0.0005, size=len(df))

# Define a simple congestion score (e.g., directly use vehicle count)
df["congestion_score"] = df["vehicle_count"]

# Assign congestion level labels based on thresholds
def assign_label(score):
    if score <= 3:
        return "Light"
    elif score <= 7:
        return "Moderate"
    else:
        return "Heavy"

df["congestion_level"] = df["congestion_score"].apply(assign_label)

# Save the output with GPS and labels
output_path = os.path.join("data", "gps_labels.csv")
df.to_csv(output_path, index=False)

print(f"Congestion labels with GPS saved to: {output_path}")

import os
import pandas as pd
import random
from datetime import datetime, timedelta

# Create output folder if not exists
os.makedirs("data", exist_ok=True)

# Simulation settings
num_frames = 300
start_time = datetime(2025, 6, 25, 15, 0, 0)
# Generate mock vehicle counts for each frame
records = []
for i in range(num_frames):
    timestamp = start_time + timedelta(seconds=i)
    vehicle_count = random.randint(5, 30)  # Vehicles detected per second
    records.append([i + 1, timestamp.strftime("%Y-%m-%d %H:%M:%S"), vehicle_count])

# Save as CSV
df = pd.DataFrame(records, columns=["frame_id", "timestamp", "vehicle_count"])
df.to_csv("data/vehicle_counts.csv", index=False)

print("✅ Mock vehicle_counts.csv generated!")

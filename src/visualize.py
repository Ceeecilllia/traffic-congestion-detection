import pandas as pd
import folium
import os

# Load the congestion data
data_path = os.path.join("data", "gps_labels.csv")
df = pd.read_csv(data_path)

# Define congestion level colors
level_colors = {
    "Light": "green",
    "Moderate": "orange",
    "Heavy": "red"
}

# Create a base Folium map centered on average coordinates
center_lat = df["latitude"].mean()
center_lon = df["longitude"].mean()
m = folium.Map(location=[center_lat, center_lon], zoom_start=15)

# Add congestion points to the map
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=6,
        popup=f"Score: {row['congestion_score']} ({row['congestion_level']})",
        color=level_colors.get(row["congestion_level"], "gray"),
        fill=True,
        fill_opacity=0.8
    ).add_to(m)

# Save the map to an HTML file
output_path = os.path.join("demo", "folium_map.html")
os.makedirs("demo", exist_ok=True)
m.save(output_path)
print(f"Congestion map saved to: {output_path}")

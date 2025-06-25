import pandas as pd
import lightgbm as lgb
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load processed data
data_path = os.path.join("data", "gps_labels.csv")
df = pd.read_csv(data_path)

# Define features and target
X = df[["congestion_score", "latitude", "longitude"]]
y = df["congestion_level"]

# Encode target labels
label_map = {"Light": 0, "Moderate": 1, "Heavy": 2}
y_encoded = y.map(label_map)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train LightGBM classifier
model = lgb.LGBMClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)

# Ensure labels are consistent even if some are missing in test set
labels_ordered = [0, 1, 2]
target_names = ["Light", "Moderate", "Heavy"]

print("Classification Report:\n")
print(classification_report(y_test, y_pred, labels=labels_ordered, target_names=target_names))

# Save model
joblib.dump(model, "src/lgbm_model.pkl")
print("Model saved to src/lgbm_model.pkl")


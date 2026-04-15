import os
os.environ["OMP_NUM_THREADS"] = "1"
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# --------- LOAD DATA -----------
data = pd.read_csv("Dataset.csv").sample(3000)
# ------------- PREPROCESSING -------
data = data[['Cuisines', 'City', 'Average Cost for two', 'Votes', 'Price range','Has Table booking', 'Has Online delivery']]
# Remove missing values
data = data.dropna()
# Simplify cuisines (take first cuisine only)
# Take first cuisine
data['Cuisines'] = data['Cuisines'].apply(lambda x: x.split(',')[0])
# Keep only top 10 cuisines
top_cuisines = data['Cuisines'].value_counts().head(10).index
data = data[data['Cuisines'].isin(top_cuisines)]
# Convert Yes/No to 1/0
data['Has Table booking'] = data['Has Table booking'].map({'Yes':1, 'No':0})
data['Has Online delivery'] = data['Has Online delivery'].map({'Yes':1, 'No':0})
# Convert target (Cuisines) into numbers
data['Cuisines'] = data['Cuisines'].astype('category')
data['Cuisines_code'] = data['Cuisines'].cat.codes
cuisine_mapping = dict(enumerate(data['Cuisines'].cat.categories))
# -------- FEATURES & TARGET ---------
data = pd.get_dummies(data, columns=['City'], drop_first=True)
X = data.drop(['Cuisines', 'Cuisines_code'], axis=1)
y = data['Cuisines_code']
# ----------- SPLIT -----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# -------------- MODEL ----------
model = RandomForestClassifier(n_estimators=50)
model.fit(X_train, y_train)
# ------- PREDICTION --------
predictions = model.predict(X_test)
# ------------ EVALUATION -----------
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, predictions))
# ----------------- SAMPLE OUTPUT --------
print("\nSample Predictions:")
for i in range(5):
    print("Predicted:", cuisine_mapping[predictions[i]],"| Actual:", cuisine_mapping[y_test.iloc[i]])
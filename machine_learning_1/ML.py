# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier

# Step 1: Load Dataset (Iris dataset as an example)
from sklearn.datasets import load_iris
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Step 2: Explore Data
print(df.head())
print(df.info())
print(df.describe())

# Step 3: Preprocessing
# Check for missing values
df.isnull().sum()

# No missing values in Iris, but if there were:
# df.fillna(df.mean(), inplace=True)

# Split data
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 4: Visualization
# Plot 1: Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True)
plt.title('Feature Correlation Heatmap')
plt.show()

# Plot 2: Scatter plot
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], c=df['target'])
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Sepal Length vs Petal Length')
plt.show()

# Step 5: Supervised Learning Example
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred_supervised = clf.predict(X_test)

# Step 5: Unsupervised Learning Example
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
clusters = kmeans.labels_

# Step 6: Regression Model (for demonstration, use a regression dataset)
from sklearn.datasets import load_diabetes

# Load a regression dataset
diabetes = load_diabetes()
df_reg = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df_reg['target'] = diabetes.target

Xr = df_reg.drop('target', axis=1)
yr = df_reg['target']
Xr_train, Xr_test, yr_train, yr_test = train_test_split(Xr, yr, test_size=0.3, random_state=42)

# Train Linear Regression
lr = LinearRegression()
lr.fit(Xr_train, yr_train)

# Predict and Evaluate
yr_pred = lr.predict(Xr_test)
mse = mean_squared_error(yr_test, yr_pred)
print(f"Mean Squared Error of Linear Regression: {mse:.2f}")

# --- END OF SCRIPT ---

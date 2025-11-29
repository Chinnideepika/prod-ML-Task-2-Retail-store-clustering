# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 23:11:48 2025

@author: Deepika
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Load the dataset
df = pd.read_csv(r" ")

# 2. Check columns and preview data
print(df.columns.tolist())
print(df[['Annual Income (k$)', 'Spending Score (1-100)']].head())

# 3. Select features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# 4. Elbow Method to find optimal k
inertia = []
k_values = range(1, 11)

for k in k_values:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertia.append(km.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(k_values, inertia, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia (sum of squared distances)")
plt.grid(alpha=0.4)
plt.show()

# 5. Apply KMeans with chosen k (example: k = 5)
K = 5
kmeans = KMeans(n_clusters=K, random_state=42, n_init=20)
df['Cluster'] = kmeans.fit_predict(X)
centers = kmeans.cluster_centers_

# 6. Print cluster information
print("\nCluster Centers (Annual Income, Spending Score):")
print(centers)

print("\nCluster Sizes:")
print(df['Cluster'].value_counts().sort_index())

# 7. Scatter plot for cluster visualization
plt.figure(figsize=(10, 6))
plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'],
            c=df['Cluster'], cmap='tab10', s=50, alpha=0.8)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=150, marker='X', label='Centers')
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title(f"Customer Segments (K = {K})")
plt.grid(alpha=0.4)
plt.legend()
plt.show()

# 8. Save the output
df.to_csv(r"C:\Users\Deepika\Downloads\Mall_Customers_Clustered.csv", index=False)
print("Saved as Mall_Customers_Clustered.csv")


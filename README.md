# PRODI GY_ML_02 – Customer Segmentation Using K-Means

This project is my submission for **Task 02** of the **Prodigy InfoTech Machine Learning Internship**.

The goal of this task is to segment retail customers based on their **Annual Income** and **Spending Score** using the **K-Means clustering algorithm**. This segmentation helps businesses understand purchasing patterns and design better marketing strategies.

---

## 📊 Dataset
The dataset used is **Mall_Customers.csv**, which contains:

- CustomerID  
- Gender  
- Age  
- Annual Income (k$)  
- Spending Score (1–100)

---

## 🧠 Methodology

### 🔹 Step 1: Load and Inspect Data  
Loaded the dataset using Pandas and examined key features.

### 🔹 Step 2: Select Features  
Used the two most relevant features:  
- `Annual Income (k$)`  
- `Spending Score (1-100)`

### 🔹 Step 3: Elbow Method  
Tested k = 1 to 10 and plotted the **Inertia Curve** to identify the “Elbow Point”.

The optimal **k = 5**.

### 🔹 Step 4: K-Means Clustering  
Applied K-Means with k = 5 to segment customers.

### 🔹 Step 5: Visualization  
Created a scatter plot showing 5 customer clusters with centroids.

### 🔹 Step 6: Save Results  
Saved the final dataset with an additional `Cluster` column as  
`Mall_Customers_Clustered.csv`.

---

## 📈 Output Plots

- **Elbow Method Plot** – Used to find optimal k  
- **Customer Segmentation Scatter Plot** – Shows clustered groups

---

## 📁 Files in this Repository

- `Mall_Customers.csv` – Dataset  
- `task2.py` – Main clustering script  
- `Mall_Customers_Clustered.csv` – Output file  
- `README.md` – Documentation

---

## 🏁 Conclusion  
This project demonstrates how customer segmentation helps identify meaningful groups such as:

- **High Income – High Spend** (Premium Customers)  
- **Low Income – Low Spend** (Budget Shoppers)  
- **Mid Income – Mid Spend** (Standard Customers)

Such insights guide targeted marketing, loyalty programs, and personalized recommendations.

---

### 🚀 Developed by Deepika  
Prodigy InfoTech – Machine Learning Internship


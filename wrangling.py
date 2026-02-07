import pandas as pd

# Load your dataset (replace 'data.csv' with your file name)
data = pd.read_csv(r"C:\Users\soniy\OneDrive\Documents\Intership\tesla_stock_data_2010_2025.csv")

# Immersion: explore the dataset
print("First 5 rows:")
print(data.head())

print("\nShape (rows, columns):", data.shape)
print("\nColumn names:", data.columns)
print("\nSummary of numbers:")
print(data.describe())
print("\nMissing values per column:")
print(data.isnull().sum())


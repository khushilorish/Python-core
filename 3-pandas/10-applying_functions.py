import pandas as pd
import numpy as np

data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago'],
    'PurchaseAmount': [150.50, 220.75, 95.00, 310.20, 180.00, 450.50, 75.90, 290.00, 120.00, 550.00, 210.00, 300.00],
    'Category': ['Electronics', 'Clothing', 'Home Goods', 'Electronics', 'Clothing', 'Home Goods', 'Electronics', 'Clothing', 'Home Goods', 'Electronics', 'Clothing', 'Home Goods']
}
df_customers = pd.DataFrame(data)

# Define a function to calculate range
def calculate_range(series):
    # Ensure the series is numeric and handle potential NaNs
    numeric_series = pd.to_numeric(series, errors='coerce')
    if numeric_series.isnull().all():
        return np.nan
    return numeric_series.max() - numeric_series.min()

# Apply the function to each column
column_ranges = df_customers.apply(calculate_range, axis=0)

print("Range (Max - Min) for each column:")
print(column_ranges)


# Define a function to categorize purchase amounts
def categorize_purchase(row):
    if row['PurchaseAmount'] > 300:
        return 'High Value'
    elif row['PurchaseAmount'] > 100:
        return 'Medium Value'
    else:
        return 'Low Value'

# Apply the function row-wise
df_customers['PurchaseCategory'] = df_customers.apply(categorize_purchase, axis=1)

print("DataFrame with new 'PurchaseCategory' column:")
print(df_customers)

# Apply a lambda function to convert string columns to uppercase
for col in df_customers.columns:
    if df_customers[col].dtype == 'object': # Check if column is of object type (often strings)
        df_customers[col] = df_customers[col].apply(lambda x: x.upper() if isinstance(x, str) else x)

print("DataFrame with string columns converted to uppercase:")
print(df_customers)


import pandas as pd
import numpy as np

# DataFrame 1: Customer Demographics
data_customers = {
    'CustomerID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles']
}
df_demographics = pd.DataFrame(data_customers)

# DataFrame 2: Order Information
data_orders = {
    'OrderID': [1, 2, 3, 4, 5, 6],
    'CustomerID': [101, 102, 101, 103, 104, 106], # Customer 106 is not in demographics
    'Product': ['Laptop', 'Keyboard', 'Mouse', 'Monitor', 'Webcam', 'Desk'],
    'Amount': [1200, 75, 25, 300, 50, 150]
}
df_orders = pd.DataFrame(data_orders)

print("Customer Demographics DataFrame:")
print(df_demographics)
print("Order Information DataFrame:")
print(df_orders)

inner_merged = pd.merge(df_demographics, df_orders, on='CustomerID', how='inner')
print("Inner Merge (Customers with Orders):")
print(inner_merged)

left_merged = pd.merge(df_demographics, df_orders, on='CustomerID', how='left')
print("Left Merge (All Customers, their Orders if any):")
print(left_merged)

right_merged = pd.merge(df_demographics, df_orders, on='CustomerID', how='right')
print("Right Merge (All Orders, their Customer Info if any):")
print(right_merged)

outer_merged = pd.merge(df_demographics, df_orders, on='CustomerID', how='outer')
print("Outer Merge (All Records from Both):")
print(outer_merged)


# Example: Join df_orders (indexed by OrderID) with df_demographics (on CustomerID)
# This requires setting an index first. Let's re-index df_orders by CustomerID for demonstration.
df_orders_indexed = df_orders.set_index('CustomerID')
print("Order DataFrame indexed by CustomerID:")
print(df_orders_indexed)

# Join df_demographics (on CustomerID column) with df_orders_indexed (on its index)
# Note: .join() defaults to a left join
joined_df = df_demographics.join(df_orders_indexed, on='CustomerID', how='left')
print("DataFrame joined using .join():")
print(joined_df)
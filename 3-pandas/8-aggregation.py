import pandas as pd
import numpy as np

data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago'],
    'PurchaseAmount': [150.50, 220.75, 95.00, 310.20, 180.00, 450.50, 75.90, 290.00, 120.00, 550.00, 210.00, 300.00],
    'Category': ['Electronics', 'Clothing', 'Home Goods', 'Electronics', 'Clothing', 'Home Goods', 'Electronics', 'Clothing', 'Home Goods', 'Electronics', 'Clothing', 'Home Goods']
}
df_customers = pd.DataFrame(data)

print("Original DataFrame:")
print(df_customers)

# Group by 'City' and 'Category'
grouped_data = df_customers.groupby(['City', 'Category'])

# Calculate the average PurchaseAmount for each City-Category combination
average_purchase_per_category_in_city = grouped_data['PurchaseAmount'].mean()

print("Average Purchase Amount per Category within each City:")
print(average_purchase_per_category_in_city)

# Reset the index to convert the Series back into a DataFrame
average_purchase_df = average_purchase_per_category_in_city.reset_index()

# Rename the aggregated column for clarity
average_purchase_df = average_purchase_df.rename(columns={'PurchaseAmount': 'AveragePurchaseAmount'})

print("Average Purchase Amount per Category within each City (as DataFrame):")
print(average_purchase_df)
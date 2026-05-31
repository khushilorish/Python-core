import pandas as pd
import numpy as np
import os

# --- Create dummy CSV files ---
# customers.csv
# customer_data = {
#     'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Boston', 'New York', 'Chicago', 'New York', 'Los Angeles'],
#     'SignupDate': pd.to_datetime(['2022-01-15', '2022-02-20', '2022-03-10', '2022-01-25', '2022-04-05', '2022-05-12', '2022-02-01', '2022-03-22', '2022-01-30', '2022-04-18'])
# }
# df_customers_csv = pd.DataFrame(customer_data)
# df_customers_csv.to_csv('customers.csv', index=False)

# # orders.csv
# order_data = {
#     'OrderID': range(1, 16),
#     'CustomerID': [101, 102, 101, 103, 104, 105, 101, 106, 107, 108, 103, 109, 110, 102, 107],
#     'Product': ['Laptop', 'Keyboard', 'Mouse', 'Monitor', 'Webcam', 'Desk', 'Charger', 'Chair', 'Lamp', 'Notebook', 'Pen', 'Tablet', 'Phone', 'Mousepad', 'Stapler'],
#     'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Furniture', 'Electronics', 'Furniture', 'Home Goods', 'Office Supplies', 'Office Supplies', 'Electronics', 'Electronics', 'Electronics', 'Office Supplies'],
#     'Price': [1200, 75, 25, 300, 50, 150, 30, 200, 40, 10, 5, 400, 800, 15, 8],
#     'Quantity': [1, 2, 3, 1, 1, 1, 2, 1, 5, 10, 20, 1, 1, 1, 5]
# }
# df_orders_csv = pd.DataFrame(order_data)
# df_orders_csv.to_csv('orders.csv', index=False)

# print("Dummy CSV files created: customers.csv, orders.csv")

#load the datasets
df_customers = pd.read_csv('customers.csv')
df_orders = pd.read_csv('orders.csv')

#calculate total amount for each order
df_orders['TotalAmount'] = df_orders['Price']*df_orders['Quantity']

print("Loaded Customer DataFrame:")
print(df_customers.head())
print("Loaded Orders DataFrame (with TotalAmount):")
print(df_orders.head())

# Group orders by CustomerID and sum the TotalAmount
customer_total_sales = df_orders.groupby('CustomerID')['TotalAmount'].sum().reset_index()
customer_total_sales = customer_total_sales.rename(columns= {'TotalAmount': 'TotalSpending'})
print("Total Spending per Customer:")
print(customer_total_sales.head())

# Merge customer demographics with their total spending
# Use a left merge to keep all customers, even if they have not ordered yet
customer_spending_details = pd.merge(df_customers, customer_total_sales, on='CustomerID', how='left')

# Fill NaN TotalSpending with 0 for customers who have not ordered
customer_spending_details['TotalSpending']= customer_spending_details['TotalSpending'].fillna(0)

print("Customer Spending Details (Demographics + Total Spending):")
print(customer_spending_details.head())

top_customers = customer_total_sales.sort_values(by='TotalSpending', ascending=False)
# Select the top 5 customers
top_5_customers = top_customers.head(5)

print("Top 5 Customers by Total Spending:")
print(top_5_customers)

# Group orders by CustomerID and calculate count and sum
customer_order_stats = df_orders.groupby('CustomerID').agg(NumberOfOrders=('OrderID', 'count'),TotalSpending=('TotalAmount', 'sum')).reset_index()

# Calculate Average Order Value
customer_order_stats['AverageOrderValue'] = customer_order_stats['TotalSpending'] / customer_order_stats['NumberOfOrders']

print("Customer Order Statistics (Count, Total, Average):")
print(customer_order_stats.head())

# Most Popular Category for Customers in 'New York'

# 1. Filter customers from 'New York'
ny_customer_df = df_customers[df_customers['City'] == "New York"]
ny_customer_id = ny_customer_df['CustomerID'].tolist()

# 2. Filter orders placed by these 'New York' customers
ny_orders = df_orders[df_orders['CustomerID'].isin(ny_customer_id)]

# 3. Group these orders by 'Category' and count them
ny_category_counts = ny_orders.groupby('Category').size().reset_index(name='Count')

# 4. Find the category with the maximum count
most_popular_ny_category = ny_category_counts.sort_values(by='Count', ascending=False).iloc[0]

print("Order Counts by Category for Customers in New York:")
print(ny_category_counts)
print(f"Most Popular Category for New York Customers: {most_popular_ny_category['Category']}(with {most_popular_ny_category['Count']} orders)")

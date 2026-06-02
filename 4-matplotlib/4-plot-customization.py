import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# sample data: Monthly sales for 2 different items
months =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_a =np.array([100, 120, 150, 130, 160, 180])
sales_b = np.array([80, 90, 110, 100, 130, 140])

plt.figure(figsize=(10, 6))

plt.plot(months, sales_a,marker='o', linestyle='-', label="Product A")
plt.plot(months, sales_b,marker='x',linestyle='--', label="Product B")

plt.title('Monthly Sales Performance', fontsize = 16)
plt.xlabel('Month', fontsize = 12)
plt.ylabel('Sales ($)', fontsize = 12)
plt.legend(loc='upper left', fontsize=10)
# Adding a grid for better readability
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()


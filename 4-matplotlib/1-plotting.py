import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# basic plotting
# x_label = np.array([1,2,3,4,5])
# y_label = np.array([2,4,5,6,8])

# plt.plot(x_label, y_label)
# plt.show()

# Hours studied
hours_studied = np.array([1, 2, 3, 4, 5])
# Quiz scores
quiz_scores = np.array([55, 65, 70, 80, 85])

# plt.plot(hours_studied, quiz_scores)
# plt.title('Quiz Scores vs. Hours Studied')
# plt.xlabel('Hours studied')
# plt.ylabel('Quiz Score')
# plt.show()



# Create date range for the x-axis
dates = pd.date_range(start='2024-01-01', periods=10, freq='D')

# Generate some sample data that shows a trend
# Let's simulate daily sales with a general upward trend and some noise
sales_data = np.linspace(100, 150, 10) + np.random.randn(10)*10

# Create a Pandas Series for easier handling
sales_series = pd.Series(sales_data, index=dates)

# Plotting using Pandas' plot method (which uses Matplotlib)
sales_series.plot(figsize=(10, 6)) # figsize sets the plot dimensions

# Add title and labels (we'll cover this in detail later)
plt.title('Daily Sales Trend Over 10 Days')
plt.xlabel('Date')
plt.ylabel('Sales Amount ($)')
plt.grid(True) # Add a grid for better readability

# Display the plot
plt.show()

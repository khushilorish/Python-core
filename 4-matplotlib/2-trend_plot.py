import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import calendar

# months of year
months = list(calendar.month_name)[1:]

# Average monthly temperatures
temp = [5,7,12,16,25,27,30, 26, 23, 19, 16, 12]

# plot months vs. temperatures
plt.figure(figsize=(10, 6))
plt.plot(months, temp, marker = 'o', linestyle='-', color='skyblue')
# Add title and labels
plt.title('Average Monthly Temperature in City X')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)

# Display the plot
plt.show()

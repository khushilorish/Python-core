import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data for height and weight
# Let's assume a positive correlation: taller people tend to weigh more
heights = 150 + 25 * np.random.randn(100)
weights = heights * 0.7 + np.random.randn(100)*10

# Ensure heights and weights are within reasonable bounds if necessary
heights = np.clip(heights, 140, 210)
weights = np.clip(weights, 40, 120)

# create scatter plot
plt.figure(figsize=(10,6))
plt.scatter(heights, weights, alpha=0.6, edgecolors='w', s=50) # alpha for transparency, s for size, edgecolors for border

# Add title and labels
plt.title('Relationship Between Height and Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True)

# Display the plot
plt.show()
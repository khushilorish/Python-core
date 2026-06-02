import matplotlib.pyplot as plt
import numpy as np

# categories = ['Very Long Category Name 1', 'Another Very Long Category Name', 'Short Name', 'Yet Another Long Name']
# values = [10, 15, 8, 12]

# plt.figure(figsize=(8, 5))
# plt.bar(categories, values)
# plt.title('Plot with Long Category Names')
# # Incorrect without rotation: plt.show()
# # Corrected:
# plt.xticks(rotation=45, ha='right') # Rotate labels and align them
# plt.tight_layout()  #Adjust layout
# plt.show()





# categories = ['A', 'B', 'C', 'D']
# values_small_diff = [100, 102, 105, 101]

# # Misleading plot (y-axis does not start at 0)
# plt.figure(figsize=(6, 4))
# plt.bar(categories, values_small_diff)
# plt.title('Misleading Bar Chart (Y-axis not at 0)')
# plt.show()

# # Corrected plot (y-axis starts at 0)
# plt.figure(figsize=(6, 4))
# plt.bar(categories, values_small_diff)
# plt.ylim(0, max(values_small_diff) * 1.1) # Ensure y-axis starts at 0 and has some padding
# plt.title('Accurate Bar Chart (Y-axis at 0)')
# plt.show()



# Generate a large number of points with some correlation
np.random.seed(1)
x = np.random.rand(500)
y = x * 2 + np.random.randn(500) * 0.5

# Overplotted scatter plot
plt.figure(figsize=(7, 5))
plt.scatter(x, y)
plt.title('Overplotted Scatter Plot')
plt.show()

# Improved scatter plot with transparency and smaller markers
plt.figure(figsize=(7, 5))
plt.scatter(x, y, alpha=0.3, s=10) # Reduced alpha and size
plt.title('Improved Scatter Plot (Transparency)')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Set a seed for reproducibility
np.random.seed(0)

# Generate hours studied (e.g., between 1 and 10 hours)
hours_studied = np.random.uniform(1, 10, 20)

# Generate practice test scores, with a positive correlation to hours studied
# Base score increases with hours, plus some random variation
practice_test_scores = 50 + hours_studied * 4 + np.random.randn(20) * 8

# Ensure scores are within a reasonable range (e.g., 0-100)
practice_test_scores = np.clip(practice_test_scores, 0, 100)

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(hours_studied, practice_test_scores, color='coral', marker='^', s=70, alpha=0.7, label='Student Performance')

# Add title and labels
plt.title('Practice Test Scores vs. Hours Studied', fontsize=16)
plt.xlabel('Hours Studied',fontsize=12)
plt.ylabel('Practice Test Score',fontsize=12)

# Add legend
plt.legend(loc='upper left', fontsize=10) # Position the legend
plt.grid(True, linestyle=':', alpha=0.6)

# Display the plot
plt.show()
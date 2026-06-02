import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# create a figure and a single axes object
# fig, ax = plt.subplots()

# x = np.linspace(0,10,100)
# y = np.sin(x)

# ax.plot(x,y)

# ax.set_title('sinwave')
# ax.set_xlabel('x-axis')
# ax.set_ylabel('y-axis')
# ax.grid(True)

# plt.show()


# creating multiple axes
fig, a = plt.subplots(nrows=2, ncols=1,figsize=(8,8))

x = np.linspace(0,10,100)
y1 = np.sin(x)

y2= np.cos(x)

a[0].plot(x,y1, color='blue')
a[0].set_title('Sine Wave')
a[0].set_xlabel('x-axis')
a[0].set_ylabel('y-axis')
a[0].grid(True)


a[1].plot(x,y2, color='red')
a[1].set_title('Cos Wave')
a[1].set_xlabel('x-axis')
a[1].set_ylabel('y-axis')
a[1].grid(True)

plt.tight_layout()
fig.suptitle('Trigonometric Functions', fontsize=16, y=1.02) # y adjusts the title position
plt.show()
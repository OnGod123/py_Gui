import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 3D data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 7]
z = [5, 3, 7, 8, 2]

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.title('3D Scatter Plot')
plt.show()

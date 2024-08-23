import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 4D data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 7]
z = [5, 3, 7, 8, 2]
c = [10, 20, 30, 40, 50]  # 4th dimension represented by color

# Create a 3D scatter plot with color representing the 4th dimension
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(x, y, z, c=c, cmap='viridis')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.colorbar(sc, label='Color (4th Dimension)')
plt.title('4D Scatter Plot Using Color')
plt.show()

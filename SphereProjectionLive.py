import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation

# initiates array to be plotted. first is used to help delete initial [0,0,0] from array
first = True
x = np.array([[0, 0, 0]])


# Adds a given [x,y,z] to the 'x' array. The first run will remove [0,0,0] from the initialized array
def plotPoint(x_coord, y_coord, z_coord):
    global first
    global x
    if first:
        y = np.array([[x_coord, y_coord, z_coord]])
        z = np.append(x, y, axis=0)
        z = np.delete(z, 0, axis=0)
        first = False
        return z
    else:
        y = np.array([[x_coord, y_coord, z_coord]])
        z = np.append(x, y, axis=0)
        return z


# Updates the plot from 0 to the end of the array
def update(i):
    sc._offsets3d = (df.x.values[:i], df.y.values[:i], df.z.values[:i])


# used for testing
# x = plotPoint(1, 2, 3)
# x = plotPoint(5, 6, 9)
# x = plotPoint(1, -4, -4)


# Creates the dataframe using the 'x' array and assigns x,y,z columns
df = pd.DataFrame(x, columns=["x", "y", "z"])

# used for creating the graphic
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# sc is passed to update() for plotting. 'c' changes plotted dot color
sc = ax.scatter([], [], [], c='darkblue', alpha=0.5)

# sets labels for the X, Y, and Z axis
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Sets limits for the X, Y, and Z axis
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

# Initial point representing the drone. Color and size can be changed according to preference.
ax.scatter([0], [0], [0], color="y", s=100)

# Interval can be removed if needed. It helps to stop too many points from being plotted at once.
ani = matplotlib.animation.FuncAnimation(fig, update, interval=500)

# shows the plot
plt.tight_layout()
plt.show()

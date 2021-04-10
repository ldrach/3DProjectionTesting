import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation

x = np.random.normal(scale=4, size=(20, 3))
df = pd.DataFrame(x, columns=["x", "y", "z"])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter([], [], [], c='darkblue', alpha=0.5)


def update(i):
    sc._offsets3d = (df.x.values[:i], df.y.values[:i], df.z.values[:i])


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.scatter([0], [0], [0], color="y", s=100)

ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(df), interval=500)

plt.tight_layout()
plt.show()

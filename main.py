import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

mu=3
n=30

x=np.random.normal(mu,1,size=n)
y = np.random.normal(mu , 1, size=n)
z = np.random.normal(mu , 1 , size=n)

plt.rcParams['figure.figsize'] = (8,6)


ax = plt.axes (projection = '3d')
ax.scatter3D(x,y,z , s = 100)
ax.set_xlabel ('X')
ax.set_ylabel ('Y')
ax.set_zlabel('Z')
ax.view_init(10 , 150)
plt.show()
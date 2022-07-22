#importing modules
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt
#setting plot style
plt.style.use(['default'])
#making array of plot points
x=[62.002,71.99,85.01,99.99,111.99,120.005,133.99,148.01]
y=[1.58**2,1.705**2,1.849**2,2.009**2,2.119**2,2.201**2,2.319**2,2.449**2]
z=[1.58,1.705,1.849,2.009,2.119,2.201,2.319,2.449]
#modifying plot 
plt.plot(x,y,z,'.--',lw=0.8,color='red')
plt.savefig('fig',  format=None, metadata=None,
        bbox_inches=None, pad_inches=0.1,
        facecolor='auto', edgecolor='auto',
        backend=None, 
       )
#3d
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
ax.plot(x, y, z, label='parametric curve')
ax.legend()
plt.show()

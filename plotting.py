'''import pandas as pd
import os
import matplotlib.pyplot as plt
excel=pd.read_excel('C:\\Users\\USER\\Desktop\\Buddi AI\\Day 1.xlsx')
datas=excel[['b1','b2','ξ']]
plt.plot(datas['ξ'])
plt.show()'''

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
excel = pd.read_excel('C:\\Users\\USER\\Desktop\\Buddi AI\\Day 1.xlsx')
X = excel['b1']
Y = excel['b2']
Z = excel['ξ']
image = plt.figure()
ax = image.add_subplot(111, projection='3d')
surface = ax.plot_trisurf(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('Surface Plot')
image.colorbar(surface, ax=ax, shrink=0.1, aspect=2)
plt.show()


# create image q1

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

// ellipse paraboloid
u = np.linspace(-2, 2, 200);
v = np.linspace(0, 2 * np.pi, 60);
[u, v] = np.meshgrid(u, v);
x = np.cosh(u)*np.cos(v)
y = np.cosh(u)*np.sin(v)
z = np.sinh(u)
plt.figure(figsize=plt.figaspect(1)).add_subplot(111, projection='3d').plot_surface(x, y, z,  rstride=4, cstride=4, color='gray')
plt.show()

// basic paraboloid
a = np.linspace(-7.0, 7.0, 100)
x = np.cos(a)
y = np.sin(a)
x, y = np.meshgrid(x, y)
z = x**2 + y**2
plt.axes(projection='3d').contour3D(x, y, z, levels=100, cmap='gray')

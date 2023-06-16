
import numpy as np, matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.integrate import odeint

mp = 939.5654133
mn = 938.2720813
e2 = 1.44

q = 2
Q = 79 
m = 2*mp + 2*mn #mass of the alpha particle

R_init = (0, 0, 0) # potition of Au in fm
r_init = (-100, 10, 10) # position of Alpha in fm (y part is b - )

RT = 7 #radius of Au nucleus in fm
# RT = 0.146e6 #radius of Au atom in fm


def systemxyt(state, t):
    z1, z2, z3, z4, z5, z6 = state
    r = max(np.sqrt((z1-R_init[0])**2 + (z3-R_init[1])**2), RT)
    dz1 = z2
    dz2 = (q*Q*e2*z1)/(m*(r**3))
    dz3 = z4
    dz4 = (q*Q*e2*z3)/(m*(r**3))
    dz5 = z6
    dz6 = (q*Q*e2*z5)/(m*(r**3))
    return [dz1, dz2, dz3, dz4, dz5, dz6]

plt.style.use('dark_background')

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title(f"Rutherford's Gold Foil Scattering")


time_points = np.linspace(0, 10000, 10001)
blim = 4

for i in np.linspace(-blim,blim,5):
    for j in np.linspace(-blim,blim,5):
        init_state = [r_init[0], .0512, i*r_init[1], 0, j*r_init[2], 0]
        xyz = odeint(systemxyt, init_state, time_points)
        x = xyz[:, 0]; y = xyz[:, 2]; z = xyz[:, 4]
        ax.plot3D(x,y,z, linewidth=3)

# au_pt = ax.scatter(R_init[0],R_init[1], color="#FFEE05")

# Au_atom = plt.Sphere(R_init, RT, color='#DDBB05') 
# ax.add_artist(Au_atom)
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
sx = np.cos(u)*np.sin(v)
sy = np.sin(u)*np.sin(v)
sz = np.cos(v) 
ax.plot_wireframe(sx, sy,sz, color='#DDBB05')

# ax.set_aspect(auto)
xlim = 50
ylim = xlim
zlim = xlim
ax.set(xlim=(-xlim, xlim),
       ylim=(-ylim, ylim),
       zlim=(-zlim, zlim))

plt.show()
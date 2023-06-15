# This program is as if JJ Thompson were right and the atom was really a plum pudding

import numpy as np, matplotlib.pyplot as plt
from scipy.integrate import odeint

mp = 939.5654133
mn = 938.2720813
e2 = 1.44

q = 2
Q = 79 
m = 2*mp + 2*mn #mass of the alpha particle

R_init = (0, 0) # potition of Au in fm
r_init = (-100e4, 10) # position of Alpha in fm (y part is b - )

# RT = 7 #radius of Au nucleus in fm
RT = 0.146e6 #radius of Au atom in fm


def systemxyt(state, t):
    z1, z2, z3, z4 = state
    r = max(np.sqrt((z1-R_init[0])**2 + (z3-R_init[1])**2), RT)
    dz1 = z2
    dz2 = (q*Q*e2*z1)/(m*(r**3))
    dz3 = z4
    dz4 = (q*Q*e2*z3)/(m*(r**3))
    return [dz1, dz2, dz3, dz4]

plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.set_title(f"Rutherford's Gold Foil Scattering")


time_points = np.linspace(0, 10000*10000, 10001)
blim = 10000

for i in np.linspace(-blim,blim,11):
    init_state = [r_init[0], .0512, i*r_init[1], 0]
    xy = odeint(systemxyt, init_state, time_points)
    x = xy[:, 0]; y = xy[:, 2]
    ax.plot(x,y)

# au_pt = ax.scatter(R_init[0],R_init[1], color="#FFEE05")

Au_atom = plt.Circle(R_init, RT, color='#DDBB05')  
ax.add_artist(Au_atom)

ax.set_aspect(1)
xlim = abs(r_init[0])
ylim = 100*10000
ax.set(xlim=(-xlim, xlim),
       ylim=(-ylim, ylim))

plt.show()
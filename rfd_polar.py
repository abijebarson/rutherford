# WARNING: This code is all over the place.
# I will clean the code, once I figure out how to clean this code.
# The values are arbitrary = Which means this is not gold and alpha particle system.
# -> The values are adjusted to produce visual output for now. Will be corrected to fit real systems later.
# There are extra lines which are remenants of hyperbola equation. It can be removed programatically.

import numpy as np
import matplotlib.pyplot as plt

mp = 939.5654133
mn = 938.2720813
e2 = 1.44

q = 2
Q = 79 
m = 2*mp + 2*mn # mass of the alpha particle
v = 0.0514

R_init = (0, 0) # potition of Au in fm
r_init = (-1, 10) # position of Alpha in fm (y part is b - ) -> Here this will act as the radius instead

# Unused yet
RT = 7 #radius of Au nucleus in fm
# RT = 0.146e6 #radius of Au atom in fm

blim = 0.1

plt.style.use('dark_background')

# fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
fig, ax = plt.subplots()

for i in np.linspace(-blim,blim,11):

    b = i*r_init[1]
    k = (q*Q*e2)/(m*(v**2)*(b**2))

    theta_0 = np.arctan2(b, r_init[0])
    theta_i = np.linspace(-np.pi, np.pi, 1001)
    # theta_0 = np.pi/2 + np.arctan(b*k) -> found online.. what is this?

    # Using the analytical solution directly
    u_i = -k*(1 + (np.cos(theta_i - theta_0))/(np.cos(theta_0)))
    r_i = 1/u_i

    # I don't like plotting directly in polar plot from matplotlib.
    x = r_i * np.cos(theta_i)
    y = r_i * np.sin(theta_i)

    ax.plot(x, y)

# Will add the nucleus later
# Au_atom = plt.Circle(R_init, 1)  
# ax.add_artist(Au_atom)
    
ax.set_aspect(1)
xlim = 0.2
ylim = xlim
ax.set(xlim=(-xlim, xlim),
       ylim=(-ylim, ylim))

plt.show()
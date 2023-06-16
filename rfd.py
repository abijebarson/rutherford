
import numpy as np, matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.widgets import Slider

mp = 939.5654133
mn = 938.2720813
e2 = 1.44

q = 2
Q = 79 
m = 2*mp + 2*mn #mass of the alpha particle

R_init = (0, 0) # potition of Au in fm
r_init = (-100, 10) # position of Alpha in fm (y part is b - )

RT = 7 #radius of Au nucleus in fm
# RT = 0.146e6 #radius of Au atom in fm

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
ax.set_title(f"Alpha Particle Scattering off Gold Nucleus")


Au_atom = plt.Circle(R_init, RT, color='#DDBB05')  
ax.add_artist(Au_atom)

plt.subplots_adjust(bottom=0.25)

axbslide = plt.axes([0.25, 0.15, 0.65, 0.03])
axvslide = plt.axes([0.25, 0.1, 0.65, 0.03])
axtslide = plt.axes([0.25, 0.05, 0.65, 0.03])

bslide = Slider(axbslide, 'Spread', 1, 30, 10)
vslide = Slider(axvslide, 'Velocity (KE)', 0.001, 0.1, .0512)
tslide = Slider(axtslide, 'End Time', 1e3, 1e5, 1e4)

# dummy_plot
blim = 4
traject = {key: ax.plot([0], [0]) for key in np.linspace(-blim, blim, 11)}
#

def update(val):
    bval = bslide.val
    vval = vslide.val
    tval = tslide.val

    time_points = np.linspace(0, tval, 10001)

    for i in np.linspace(-blim,blim,11):
        init_state = [r_init[0], vval, i*bval, 0]
        xy = odeint(systemxyt, init_state, time_points)
        x = xy[:, 0]; y = xy[:, 2]
        traject[i][0].set_xdata(x)
        traject[i][0].set_ydata(y)

bslide.on_changed(update)
vslide.on_changed(update)
tslide.on_changed(update)

update(None)

ax.set_aspect(1)
xlim = abs(r_init[0])
ylim = xlim
ax.set(xlim=(-xlim, xlim),
       ylim=(-ylim, ylim))

manager = plt.get_current_fig_manager()
manager.set_window_title("Rutherford's Gold Foil Scattering Experiment - Simulation")

plt.show()
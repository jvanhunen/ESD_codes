# bath.py
#
# Subitop modelling course, Edinburgh 2017
# Jeroen van Hunen, March 2017
# purpose: calculates water volume in emptying bath 
# method: explicit time integration

import numpy as np
import matplotlib.pyplot as plt

# Initialisation of the parameters:
v_ini  = 500           # Volume at time t=0
v_old  = v_ini         
a      = -0.01         # parameter related to emptying bathtub
t      = 0             # set start time to 0
dt     = 25            # time step size
nt     = 25            # number of time steps
volume = np.zeros(nt)  # create some arrays to put solutions in
an     = np.zeros(nt)
time   = np.zeros(nt)

# Start time-stepping
for it in range(0,nt):
    # save old solutions in arrays:
    volume[it] = v_old 
    time[it]   = t     
    v_new      = v_old + dt*a*v_old # Calculate new solution
    t          = t + dt             # Update time
    v_old      = v_new              # Prepare for next time step

# Calculate analytical solution:
an=v_ini*np.exp(a*time) #*np.exp(a*time)

# Plot solution:
plt.clf()
plt.figure(1)
plt.plot (time,an,'--')
plt.plot (time,volume,'o-')
plt.xlabel('t(sec)')
plt.ylabel('V(liters)')
plt.title('Bath tub volume through time')
plt.show()
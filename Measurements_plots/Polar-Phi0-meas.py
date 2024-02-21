import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
from math import pi

# Set the font family and serif font
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = 'Times New Roman'
matplotlib.rcParams['font.size'] = 14

#-----------------------------------------------------------------------
#-------------------- PLOTS from .txt ASCII simulations ----------------
#-----------------------------------------------------------------------

# import sheet from .txt ASCII simulations
fileName = 'Gain-sim.txt' #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------- HERE
filePath = Path().resolve() / 'Data' / fileName
raw = np.loadtxt(filePath, skiprows=2)
gain = raw[:, 5]
gain = np.transpose(gain.reshape((72, 37)))
# angles axes
phi = np.linspace(0, 360, 73)*pi/180

# plot Elevation planes
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
gainPhi0 = np.append(gain[:-1, 0], np.flip(gain[:, 36]))
ax.plot(phi, gainPhi0, 'C0', lw=3, ls='-', label='Simulated RHCP')

gain = raw[:, 3]
gain = np.transpose(gain.reshape((72, 37)))
# angles axes
phi = np.linspace(0, 360, 73)*pi/180

# plot Elevation planes
gainPhi0 = np.append(gain[:-1, 0], np.flip(gain[:, 36]))
ax.plot(phi, gainPhi0, 'C0', lw=3, ls='--', label='Simulated RHCP')



# import sheet from .xlsx SATIMO measurements
fileName = 'LoRAK-20022024.xlsx' #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------- HERE
sheetName = 'RHCP@870'

filePath = Path().resolve() / 'Data' / fileName
data = np.array(pd.read_excel(filePath, sheet_name=sheetName))
gain = data[:, 1:]

# angles axes
phi = np.linspace(0, 360, 120)*pi/180
theta = data[:, 0]*pi/180

# plot Elevation planes
ax.plot(theta, gain[:, 0], 'C1', lw=3, ls='-', label='Measured RHCP')

sheetName = 'LHCP@870'

filePath = Path().resolve() / 'Data' / fileName
data = np.array(pd.read_excel(filePath, sheet_name=sheetName))
gain = data[:, 1:]

# angles axes
phi = np.linspace(0, 360, 120)*pi/180
theta = data[:, 0]*pi/180

# plot Elevation planes
ax.plot(theta, gain[:, 0], 'C1', lw=3, ls='--', label='Measured LHCP')

# graphic settings
ax.set_ylim([-30, 5])  #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------- HERE
ax.set_theta_zero_location('N')
angle = np.deg2rad(67.5)
ax.legend(loc="lower left", bbox_to_anchor=(.5 + np.cos(angle)/2, .5 + np.sin(angle)/2))

# save image
plt.savefig('Polar-Phi0-meas.png', bbox_inches='tight')
plt.show()


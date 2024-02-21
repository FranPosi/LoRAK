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

# plot Elevation planes
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

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
ax.plot(theta, gain[:, 30], 'C0', lw=3, ls='-', label='Measured RHCP')

sheetName = 'LHCP@870'

filePath = Path().resolve() / 'Data' / fileName
data = np.array(pd.read_excel(filePath, sheet_name=sheetName))
gain = data[:, 1:]

# angles axes
phi = np.linspace(0, 360, 120)*pi/180
theta = data[:, 0]*pi/180

# plot Elevation planes
ax.plot(theta, gain[:, 30], 'C1', lw=3, ls='-', label='Measured LHCP')

# graphic settings
ax.set_ylim([-30, 5])  #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------- HERE
ax.set_theta_zero_location('N')
angle = np.deg2rad(67.5)
ax.legend(loc="lower left", bbox_to_anchor=(.5 + np.cos(angle)/2, .4 + np.sin(angle)/2))
plt.title('RHCP and LHCP @$\phi = 90^\circ$')

# save image
plt.savefig('Polar-Phi90-measAlone.png', bbox_inches='tight')
plt.show()



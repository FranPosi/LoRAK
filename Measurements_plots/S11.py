import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import skrf as rf
from math import pi
import matplotlib

# Set the font family and serif font
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = 'Times New Roman'
matplotlib.rcParams['font.size'] = 14

#-----------------------------------------------------------------------
#-------------------- PLOTS from .txt ASCII simulations ----------------
#-----------------------------------------------------------------------

fig, ax1 = plt.subplots()

# import from .txt ASCII simulations
fileName = 'S11@0+S22@90.txt' #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------- HERE
filePath = Path().resolve() / 'Data' / fileName
raw = np.loadtxt(filePath, skiprows=2)
f = raw[:, 0]*1e3
S11 = raw[:, 1]

# plot simulated --------------  S11  -----------------
ax1.plot(f, S11, lw=3, ls='-', label='Simul.')

# import from .s1p measurement file
fileName = 'S11-meas.s1p' #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------- HERE
filePath = Path().resolve() / 'Data' / fileName
ntwk = rf.Network(filePath)
ntwk.frequency.f /= 1e6      # normalize frequencies
ntwk.plot_s_db(ax=ax1, lw=3, ls='-', label='Meas.')
# ax1.legend().set_visible(False)

ax1.set_xlabel('Frequency [MHz]')
ax1.set_ylabel('$S_{11}$ parameter [dB]')
# plt.ylim(-25, 1)

plt.legend()

plt.grid()
plt.xlim(600, 1100)
# save image
plt.savefig('S11-meas.png', bbox_inches='tight')
plt.show()



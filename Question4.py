import math
import matplotlib as plt
import scipy.stats
from scipy.stats import norm
from scipy.stats import uniform
import collections
from scipy import stats
import copy
from copy import deepcopy
from decimal import Decimal
from datetime import datetime
import matplotlib.pyplot as plt; plt.rcdefaults()
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import NullFormatter
import time
# from Master import*

#			QUESTION 4

#********************* Local vertical soil heat flux (depth in meters)
# dry clay, 40% porosity
ks = 0.25 # (W m K)

# Depth 1 
Temp1 = -2.22
# TempK = (273.15+(Temp))
Depth1 = 0.5
G1 = -ks*(Temp1/Depth1)
print G1


# Depth 2 
Temp2 = 1.11
# TempK = (273.15+(Temp))
Depth2 = 1.5
G2 = -ks*(Temp2/Depth2)
print G2


# Values show that energy is leaving the soil in the lower depth
# while the higher depth is absorbing energy. So its radiating 
# towards the surface.

#************************ Local vertical soil heat flux for new depth

# Depth 4 
Temp4 = 3.33
# TempK = (273.15+(Temp))
Depth4 = 2.5
G4 = -ks*(Temp4/Depth4)
print "here"
print G4
# (x, y) == (Depth2, Temp2) 

# Calculate heat flux at 2m depth (depth 3)
Slope = (Depth2-Depth1)/(Temp2-Temp1)

# New depth (m):
Depth3 = 2 
# Temp at depth 2m (slope = y2-y1/x2-x1)
Temp3 = -1*((Slope*(Depth2-Depth3))-Temp2)

# Depth 3
# TempK = (273.15+(Temp3))
G3 = -ks*(Temp3/Depth3)
print G3
#********************** 5 am temperature

# Soil heat flow

# Based upon the observations, our sample closest to the surface is 
# showing a positive heat flux. This means it's beginning to absorb heat 
# from the surface. The flux value for the 0.5 meter sample was 1.11 W/m.
# The deepest sample had a flux of -0.333 W/m. This decreased with decreasing 
# depth (see figures). This suggests that the surface is gaining energy.
# By 5 am the gradient for temperature and flux will begin to level, as the 
# surface begins transferring energy downward as opposed to releasing it.
# The results are somewhat accurate, the figures show the estimate between
# my 2.5 meter and 1.5 meter sample (for 2 meters) is not accurate. 
# The temperature trend is smooth; however, the flux trend is irregular at 2 
# meters. Missing variables from this are surface temperatures and ground 
# coverage. I think in order to increase the accuracy of the results, 
# those variables should be accounted for. In addition, the most accurate
# way to estimate the 2 meter depth would have been to calculate an area
# of soil to estimate its heat capacity and determine the transfer between
# the 1.5 meter and 2.5 meter readings. Keeping energy transfer variable, k,
# as a constant.














































# x = [G1, G2, G3, G4]
# x2 = [Temp1, Temp2, Temp3, Temp4]
# y = [Depth1, Depth2, Depth3, Depth4]

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.grid(True)
# fig.subplots_adjust(top=0.85)
# ax.set_xlabel('Flux (W/m)')
# ax.set_ylabel('Depth (m))')
# ax.set_title('Flux Gradient vs Depth', fontweight='bold')
# plt.plot(x,y,  '-')
# plt.gca().invert_yaxis()


# plt.show()

# plt.close()

# x = [G1, G2, G3, G4]
# x2 = [Temp1, Temp2, Temp3, Temp4]
# y = [Depth1, Depth2, Depth3, Depth4]

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.grid(True)
# fig.subplots_adjust(top=0.85)
# ax.set_xlabel('Temperature (C)')
# ax.set_ylabel('Depth (m))')
# ax.set_title('Temperature Gradient vs Depth', fontweight='bold')
# plt.plot(x2,y,  '-')
# plt.gca().invert_yaxis()


# plt.show()

# plt.close()






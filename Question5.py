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
import numpy as np


# Surface Temperature Over Time
def fnc(t):
	Tm = 25
	Ta = 15
	t = float(t*3600)
	P = (24*3600)
	to = 6*3600
	P = (t-to)/(24*3600)
	y = Tm + Ta*math.sin((2*math.pi*P))
	return y

time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
SurfaceT = []
for aRow in time:
	v = fnc(aRow)
	SurfaceT.append(v)
x = time
y = SurfaceT
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)
fig.subplots_adjust(top=0.85)
ax.set_xlabel('Time (Hours)')
ax.set_ylabel('Temp (C)')
ax.set_title('Surface Temperature over Time', fontweight='bold')
plt.plot(x,y,  '-')

# plt.show()

plt.close()

#************************************** SOIL 

def fnc(t):
	Depth = 0.05
	SD = 0.1
	Tm = 25
	Ta = 15
	D = Tm
	Shift = -(Depth/SD)
	t = float(t*3600)
	P = (24*3600)
	to = 6*3600
	P = (t-to)/(24*3600)
	y = D + (Ta*np.exp(-Depth/SD))*(math.sin((2*math.pi*P+Shift)))
	return y

#Graph
time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
var = []
for aRow in time:
	v = fnc(aRow)
	var.append(v)

x = time
y = var
# Graph
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)
fig.subplots_adjust(top=0.85)
ax.set_xlabel('Time (Hours)')
ax.set_ylabel('Temp (C)')
ax.set_title('Temperature over Time', fontweight='bold')
plt.plot(x,y,  '-')
# plt.show()
plt.close()

# VALUES
# 12 pm:
# 0.05 Meters = 32.98421095323506 Celsius
# 0.1 Meters = 27.981491655196194 Celsius
# 0.2 Meters = 24.155209750118082 Celsius
# 12 am:
# 0.05 Meters = 17.01578904676494 Celsius
# 0.1 Meters = 22.018508344803806 Celsius
# 0.2 Meters = 25.844790249881918 Celsius

# The results show that the larges fluctuations occur at the 0.05 meter 
# depth. This is the sample closest to the surface. Between noon and midnight,
# we see much larger fluctuations for the 0.05 and 0.1 meter depths, while the 
# 0.2 meter depth shows less of a fluctuation and more of a delayed response
# to the surface temeperatures.

# I feel these calculations still lack accuracy without the aspect of 
# ground coverage. In addition, we do not include any environmental variables.
# The soil is given the same porosity and water content. The use of multiple 
# measuring instruments could aid in predicting large areas. Since the latter
# soil sample shows the least fluctuation, I believe that could be the
# simplest to predict.




def fnc(t, Depth):
	SD = 0.1
	Tm = 25
	Ta = 15
	D = Tm
	Shift = -(Depth/SD)
	t = float(t*3600)
	P = (24*3600)
	to = 6*3600
	P = (t-to)/(24*3600)
	y = D + (Ta*np.exp(-Depth/SD))*(math.sin((2*math.pi*P+Shift)))
	return y

Depth1 = []
for aRow in time:
	v = fnc(aRow, 0.05)
	Depth1.append(v)
print Depth1

Depth2 = []
for aRow in time:
	v = fnc(aRow, 0.1)
	Depth2.append(v)

Depth3 = []
for aRow in time:
	v = fnc(aRow, 0.2)
	Depth3.append(v)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)
fig.subplots_adjust(top=0.85)
ax.set_xlabel('Time (Hours)')
ax.set_ylabel('Temp (C)')
ax.set_title('Soil Temperature Over Time', fontweight='bold')
plt.plot(x, Depth1,  '-', label='0.05 Meters')
plt.plot(x, Depth2,  '-.', label='0.1 Meters')
plt.plot(x, Depth3,  '.', label='0.2 Meters')
plt.plot(x, SurfaceT,  '-', color='black', label='Surface Temperature')
plt.legend()
plt.show()
plt.close()
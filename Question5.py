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


# This equation shows large varitions in heat
t = float(1)
frac = t/24
Depth = float(.02)
SD = float(.1)
Tm = 40
# Tm = (273.15+(Tm))
Ta = float(15)
A = 15
B = (2*math.pi)
P = A/B
t = frac*P
D = Tm
Shift = -(Depth/SD)
# Ta = (273.15+(Ta))

y = A*math.sin(2*math.pi*((P-t)/P))+D
# Equals 40 at 0 and 12
# print y

# BASE TEMP OVER TIME
def fnc(t):
	t = float(t)
	frac = t/24
	# Depth = float(.02)
	# SD = float(.1)
	Tm = 40
	# Tm = (273.15+(Tm))
	Ta = float(15)
	A = 15
	B = (2*math.pi)
	P = A/B
	t = frac*P
	D = Tm
	# Shift = -(Depth/SD)
	# Ta = (273.15+(Ta))

	y = A*math.sin(2*math.pi*((P-t)/P))+D
	return y


time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
var = []
for aRow in time:
	v = fnc(aRow)
	var.append(v)


x = time
y = var

fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)
fig.subplots_adjust(top=0.85)
ax.set_xlabel('Time (Hours)')
ax.set_ylabel('Temp (C)')
ax.set_title('Temperature over Time', fontweight='bold')
plt.plot(x,y,  '-')

plt.show()

plt.close()


#***************************************TRY SOIL 

def fnc(t):
	Depth = float(.02)
	SD = float(.1)
	Tm = 40
	# Tm = (273.15+(Tm))
	Ta = 15
	# Ta = 273.15+Ta
	A = (Ta*(-Depth/SD))
	# print A
	B = (2*math.pi)
	P = A/B
	D = Tm
	# D = 273.15+D
	Shift = -(Depth/SD)
	# Shift = 0

	t = float(t*3600)
	# frac = t/24
	Pt = (P/24)
	to = (Pt*6)*3600
	# print to
	# print t
	to = float(to)

	y = A*math.sin(2*math.pi*((t-to)/P)+Shift)+D
	return y


time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
var = []
for aRow in time:
	v = fnc(aRow)
	var.append(v)


x = time
y = var

fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)
fig.subplots_adjust(top=0.85)
ax.set_xlabel('Time (Hours)')
ax.set_ylabel('Temp (C)')
ax.set_title('Temperature over Time', fontweight='bold')
plt.plot(x,y,  '-')

plt.show()

plt.close()


# Depth = float(.02)
# SD = float(.1)
# Tm = 40
# # Tm = (273.15+(Tm))
# Ta = float(15)
# A = 15*math.pi
# B = (2*math.pi)
# P = A/B
# D = Tm

# Hour = float(6)
# HourR = Hour/24
# tVar = HourR*P
# t = float(tVar*math.pi)


# y = A*math.sin(2*math.pi*(t-P/P))+D
# # Changes? wrong
# # print y


# Depth = float(.02)
# SD = float(.1)
# Tm = 40
# # Tm = (273.15+(Tm))
# Ta = 15
# Ta = 273.15+Ta
# A = (Ta**(-Depth/SD))

# # print A
# B = (2*math.pi)
# P = A/B
# D = Tm
# D = 273.15+D
# Shift = -(Depth-SD)

# Hour = float(0)
# HourR = Hour/48
# tVar = HourR*P
# t = float(tVar*math.pi)


# y = A*math.sin(2*math.pi*(t-P/P)+Shift)+D
# # print y
# # print y-273.15



# Depth = float(.02)
# SD = float(.1)
# Tm = 40
# # Tm = (273.15+(Tm))
# Ta = 15
# # Ta = 273.15+Ta
# A = (Ta*(-Depth/SD))

# print A
# B = (2*math.pi)
# P = A/B
# D = Tm
# # D = 273.15+D
# Shift = -(Depth-SD)

# Hour = float(6)
# HourR = Hour/48
# tVar = HourR*P
# t = float(tVar*math.pi)


# y = A*math.sin(2*math.pi*(t-P/P)+Shift)+D

# print y
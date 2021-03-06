import math
from datetime import datetime

#			QUESTION 3

#*********************************** Net Daily Ave Longwave Radiation
#***** Determine Solar Constant

# Stefan-Boltzmann Constant (W/m^2.K^4)
o = 5.67*10**-8

# Sun Radius (m)
R = 696*10**6

# Average Distance Between Sun and Earth (m)
D = 150*10**9

# Sun temp (K):
T = 5777

# Solar Constant Gsc: (Given as 1367 W/m^2)

Gsc = o*(T**4)*(((4*math.pi*R)/(4*math.pi*D))**2)
# Calculated at 1359.65426762 W/m^2

#***** Latitude and Longitude
Lat = 47.925259
# Convert to Raidans:
Lat = (Lat*math.pi)/180

Lon = -97.032852
# Convert to Raidans
Lon = (Lon*math.pi)/180

#***** Declination (D) angle (-23.45<=D<=23.45)
# n as day of year
Date = datetime.strptime('16/9/2018', '%d/%m/%Y')
n = Date.strftime('%j')
n = int(n)

DA = 0.4093*math.sin((((2*math.pi)/365)*n)-1.405)

#***** Hour Angle
Ws = math.acos((-(math.tan(DA)))*math.tan(Lat))

#***** Day lenght
# Data check online source with: http://aa.usno.navy.mil/data/docs/Dur_OneYear.php
N = ((24/math.pi)*Ws)

#***** Seconds in Hour
Hs = 3600

#***** Hours per Day
Hd = 24

#***** Distance Variable (estimate at 1)
dr = 1

#***** Daily Insolation
# Convert Solar Constant W/m^2 to MJ
Gsc = Gsc/1000000
# Calculate Daily Solar Insolation (MJ/m^2)
S = ((Hs*Hd/math.pi)*Gsc)*dr*(Ws*math.sin(Lat)*math.sin(DA)
	+math.cos(Lat)*math.cos(DA)*math.sin(Ws))
print S
# Actual daily solar radiation at ground:
As = 0.25
Bs = 0.75
Sd = (As+(N/24)*Bs)*S

# Average cloud coverage in octas:
c = 0.4

# Vapor Pressure
Dp = 17.6
e = 6.11*(10**((7.5*Dp)/(237.3+Dp)))

# Sat Vapor Pressure
Temp = 23.3
# es = 6.11*(10**((7.5*Temp)/(237.3+Temp)))

# f for equation (Sd and S are for computing fractional solar E!
# units do not transfer to equation)
f = (Sd/S)*((As+(1-c)*Bs)/(As+Bs))

# e for the equation
e = 0.34-(0.14*(math.sqrt(Dp)))

# Compute Daily Average Net Longwave Radiation units transfer 
# from Stefan-Boltzmann Constant (W/m^2)
Temp = Temp+273.15
L = (-f)*e*o*(Temp**4)
print L
# Convert Daily Average Net Longwave Radiation to daily average
# Watts = Joules
# Joules per day
Total = (3600*24)*(L)
# MJ per day
Total = Total/1000000
print Total

# My result for total daily insolation was 26.6308 MJ/m^2. This led
# to 48.1085 W/m^2 of daily average net longwave radiation, resulting
# in a total of 4.1565 MJ/m^2 of daily net longwave radiation.

# This analysis fails to incorporate cloud coverage, atmospheric reflection/
# scattering, and total daily sunlight. The initial average for net longwave
# radiation is in the units W/m^2, but this is over a time frame of 24
# hours. The average is multiplied to calculate total net longwave radiation
# then converted to MJ per day. 


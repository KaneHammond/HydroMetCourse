import math
from datetime import datetime

#			QUESTION 1

#*****************************************Total daily solar E!
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
# Date = datetime.strptime('1/10/2018', '%d/%m/%Y')
Date = datetime.strptime('1/12/2018', '%d/%m/%Y')
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

# For October 1st, 2018, my daily Solar Insolation was 22.0525 MJ/m^2.
# My calculation for December 1st, 2018, was 9.25258994325 MJ/m^2.
# The value from December was much lower due to the declination angle
# change. By December Grand Forks has tilted further away from the sun
# and day lengths have decreased. Where in October, the tilt is at 
# less of an angle. The main issues with this calcualtion would
# be that local weather is not accounted for. Cloud cover could reduce
# the amount of radiation reaching the surface. In addition, other varibles 
# for the lower troposphere could reduce solar insolation. Such as the presence
# of greenhouse gases or other molecules which could scatter the solar 
# insolation back into space, or absorb it into the atmosphere. I think the 
# accuracy of these results are ok. Using cloud coverage would have allowed
# for results yielding greater accuracy.






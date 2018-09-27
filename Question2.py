import math
from datetime import datetime

#			QUESTION 2

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
Lat = 39.3508
# Convert to Raidans:
Lat = (Lat*math.pi)/180

Lon = -101.7102
# Convert to Raidans
Lon = (Lon*math.pi)/180

#***** Declination (D) angle (-23.45<=D<=23.45)
# n as day of year
Date = datetime.strptime('15/8/2018', '%d/%m/%Y')
# Date = datetime.strptime('15/3/2018', '%d/%m/%Y')
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
#************************************************* Water evap
# DeltaH of Vaporization for Water 40.79 kj/mol
# Density of water (estimate without temp) 997kg/m^3

# Actual Solar using hours of light as opposed to cloud coverage (given 0)
As = 0
Bs = 1
# As 0 & Bs at 1, representing no E! loss, only sunlight hours 
# will calc into total E!
Sd = (As+(N/24)*Bs)*S

# Albedo of water approx 0.08
# Get Net Daily Solar Radiation
Sdn = (1-(0.08))*Sd

# Water variables
# Total Water
Volume = 8*4.5*0.5 #(ft^3)
VolumeM = Volume*(0.0283168) # Convert to cubic meters
Density = 977 #(kg/m^3)
Mass = VolumeM*Density

# Area
Area = 8*4.5

AreaM = Area*(0.0283168)
# Area is equal to 1.0194048 Meters. Output of E! calcualtions
# are in MJ per M^2. 

# Mol of H2O
# g/mol H2O is 18g/mol 
MolsH2O = (Mass*1000)/18

# E! to evaporate (DeltaH of Vaporization for Water 40.79 kj/mol)
# 1MJ = 1000kj
HeatVap = 40.79

#Convert to kj
Sdn = Sdn*1000
MolPerDay = Sdn/HeatVap

# Estimate days for evap with net solar and latent heat of vap:
# Estimate days for evap with net solar and latent heat of vap:
Days = MolsH2O/MolPerDay
print Days

# Estimate days for evap with Equivalent depth of evaporated water equation:
# Estimate days for evap with Equivalent depth of evaporated water equation:
S = 15.39*dr*(Ws*math.sin(Lat)*math.sin(DA)
	+math.cos(Lat)*math.cos(DA)*math.sin(Ws))
# Rate is in mm per day
Rate = S
print S
# Convert depth from in to mm
Depth = 6*25.4

Days = Depth/Rate
print Days

# The Kansas site showed a daily solar insolation of 26.9092820836 MJ/m^2
# on March, 15th, 2019. This resulted in a water loss of about 11.075 mm 
# per day. Leading to a total of 13.76 days for the water to evaporate. 
# On August, 15th, 2019, the total solar insolation was 37.6461644165 MJ/m^2.
# Resulting in an evaporation rate of 15.494 mm per day, and 9.835 days
# till total evaporation. The equation used to estimate the evaporation 
# rate added reduciton variables to total solar insolation value. This was
# to account for the lenght day and total estimated sunshine. Other variables
# such as wind, surface temperatures, and seepage into the soil were not 
# accounted for. This reduced the accuracy of my results. Regardless, I 
# feel that the estimate is accurate enough to use for larger scale studies
# where specific variables are missing.
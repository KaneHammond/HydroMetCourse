import math

# from Master import*

#			QUESTION 4

#********************* Local vertical soil heat flux (depth in meters)
# dry clay, 40% porosity
# Homogeneous soil, temperature in Celsius
ks = 0.25 # (W/m K)

# Depth 1 *****
Temp1 = -2.22
Temp1 = (273.15+(Temp1))
print Temp1
Depth1 = float(0.5)

# Depth 2 *****
Temp2 = 1.11
Temp2 = (273.15+(Temp2))
print Temp2
Depth2 = 1.5

G1 = -ks*((Temp2-Temp1)/(Depth2-Depth1))
print G1
# -0.8325 W/m^2

# Value shows that energy is leaving the soil between the 0.5 and 1.5
# meter depth at a rate of -0.8325 W/m^2. Hence, the heat flux at 1 meter
# is showing a heat loss at a rate of approximately -0.8325 W/m^2.

#************************ Local vertical soil heat flux for new depth

# Depth 4 *****
Temp4 = 3.33
Temp4 = (273.15+(Temp4))
Depth4 = 2.5

# Estimated heat flux between 2.5 and 2 meters

G2= -ks*((Temp2-Temp4)/(Depth2-Depth4))
print G2
# -0.555 W/m^2

# Value shows that energy is leaving the soil between the 1.5 and 2.5
# meter depth at a rate of -0.555 W/m^2. Hence, the heat flux at 2 
# meters will approximately -0.555 W/m^2 overall.

#********************** 5 am temperature

# Soil heat flow

# Our results show that energy is leaving the system at the depths of 1 meter
# and 2 meters. The flux at the 1 meter sample (0.5-1.5 meters) is -0.8325 W/m^2,
# while the flux at the 2 meter sample (1.5-2.5) is -0.555 W/m^2. This means
# that energy in the form of heat is leaving the surface sample more quickly
# than the latter. This makes sense as the time variable, albeit not
# a variable in the inital equation, is 4 am. Over night surface temperatures drop and
# the surface energy flux will become negative, as energy accumulated during 
# the day is released.

# If we were to estimate the values for heat flux at 5 am for the 1 meter and 2
# meter depths, we could expect that energy will continue to be lost. This
# is an assumption based upon sunrise ocurring later than 5 am, and that the 
# surface air temperatures do not increase. It would be more likely that surface
# temperature will continue to decrease by 5 am. This would lead to an increasing
# trend of heat loss for both the 1 meter and 2 meter samples.

# However, if surface temperature were to increase we could expect a positive shift in 
# heat flux. I would assume it to still be negative as one hour may not be enough
# time for the surface to warm to reverse the trend entirely. Despite surface 
# warming, the 2 meter soil flux (1.5-2 meter sample) would not show a shift as 
# drastic as the higher sample. The flux change would be fractional compared
# to the upper most sample. Regardless, it is unlikely that surface warming
# will occur at 5 am. In which case the trend for the 1 meter and 2 meter sample
# will increase negatively.

# The equation used for these estimates are useful for below surface fluxes.
# In order to increase the accuracy of these calculations, surface soil 
# temperatures and surface coverage would need to be considered. The insulation, 
# or lack of, could affect how rapid heat loss occurs at the surface. Altering
# the temperature and heat flux gradients below the surface.













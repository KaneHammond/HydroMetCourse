import math

# Local vertical soil heat flux
# dry clay, 40% porosity
ks = 0.25 # (W m K)

# Depth 1
Temp = -2.22
TempK = (273.15+(Temp))
Depth = 0.5
G = -ks*(Temp/Depth)
# print G
# Value of 1.11 W m 

# Depth 2
Temp = 1.11
TempK = (273.15+(Temp))
Depth = 1.5
G = -ks*(Temp/Depth)
# print G
# Value of 1.11 W m

# Values show that energy is leaving the soil in the lower depth
# while the higher depth is absorbing energy. So its radiating 
# towards the surface.

# Depth 1
Temp = 1.11
TempK = (273.15+(Temp))
Depth = 1.5
G = -ks*(Temp/Depth)
print G
# Value of 1.11 W m 

# Depth 2
Temp = 3.33
TempK = (273.15+(Temp))
Depth = 2.5
G = -ks*(Temp/Depth)
print G
# Value of 1.11 W m




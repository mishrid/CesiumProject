

from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv


#would we need to create a TLE for every point of data in the ephemeris?
line1 = ('1 00005U 58002B   00179.98495062  .00000023  00000-0  28098-4 0  4753')
line2 = ('2 00005  34.2682 348.7242 1859667 331.7664  19.3264 10.82419157413667')

satellite = twoline2rv(line1, line2, wgs72)


#once we have the satellite with the TLE attribute do we propogate to one specific time? 
#is there any way to import a range of TLE elements and then propogate to a date range?
position, velocity = satellite.propagate(2010, 7, 29, 12, 50, 19)

print(satellite.error)

print(position)

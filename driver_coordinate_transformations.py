import coordinate_transformations
import datetime
azimuth,altitude = coordinate_transformations.eq_to_hor(17,-20,datetime.datetime.now(),
                                           13,76,82.5)
print(azimuth)
print(altitude)

print(coordinate_transformations.hor_to_eq(azimuth,altitude,datetime.datetime.now(),
                                           13,76,82.5))
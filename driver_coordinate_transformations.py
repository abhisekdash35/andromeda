import coordinate_transformations
import datetime
azimuth,altitude = coordinate_transformations.eq_to_hor(12,20,datetime.datetime.now(),
                                                        13,76,82.5)
print("actual azimuth")
print(azimuth)
print()
print("actual altitude: ")
print(altitude)
print()
print(coordinate_transformations.hor_to_eq(azimuth,altitude,datetime.datetime.now(),
                                           13,76,82.5))

# print(coordinate_transformations.new_longitude(76,-388))
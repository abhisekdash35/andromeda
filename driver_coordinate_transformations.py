import coordinate_transformations
import datetime
# azimuth,altitude = coordinate_transformations.eq_to_hor(1,70,datetime.datetime.now(),
#                                                         13,76,82.5)
# print(azimuth)
# print(altitude)
# print()
# print(coordinate_transformations.hor_to_eq(20,30,datetime.datetime.now(),
#                                            13,76,82.5))

# print(coordinate_transformations.rotate_point_about_arbitrary_axis_in_3d(position_vector_of_tail_of_rotation_axis=[0,0,0],
#                                                                          position_vector_of_tip_of_rotation_axis=[1,1,1],
#                                                                          coordinates_to_rotate=[2,2,2],
#
#
#                                                                          rotation_angle_in_degrees=90))
print(coordinate_transformations.diff_longitude(76,200))
import coordinate_transformations
import datetime
import time
while True:
    azimuth,altitude = coordinate_transformations.eq_to_hor(ra=3.6,
                                                            dec=0,
                                                            time_of_observation_in_datetime_format=datetime.datetime.now(),
                                                            latitude_of_observer=13,
                                                            longitude_of_observer=76,
                                                            local_standard_time_meridian=82.5)
    print("azimuth: "+str(azimuth))
    print("altitude: "+str(altitude))
    RA,DEC = coordinate_transformations.hor_to_eq(azimuth=azimuth,
                                                  altitude=altitude,
                                                  time_of_observation_in_datetime_format=datetime.datetime.now(),
                                                  latitude_of_observer=13,
                                                  longitude_of_observer=76,
                                                  local_standard_time_meridian=82.5)
    print("RA: "+str(RA))
    print("DEC: "+str(DEC))
    print()
    time.sleep(1)

# RA,DEC = coordinate_transformations.hor_to_eq(90,90,datetime.datetime.now(),0,76,82.5)
# print("RA: "+str(RA))
# print("DEC: "+str(DEC))
# print()
#
# RA,DEC = coordinate_transformations.hor_to_eq(180,90,datetime.datetime.now(),0,76,82.5)
# print("RA: "+str(RA))
# print("DEC: "+str(DEC))
# print()
#
# RA,DEC = coordinate_transformations.hor_to_eq(270,90,datetime.datetime.now(),0,76,82.5)
# print("RA: "+str(RA))
# print("DEC: "+str(DEC))
# print()
#
# RA,DEC = coordinate_transformations.hor_to_eq(45,90,datetime.datetime.now(),0,76,82.5)
# print("RA: "+str(RA))
# print("DEC: "+str(DEC))
# print()
#
# RA,DEC = coordinate_transformations.hor_to_eq(46,90,datetime.datetime.now(),0,76,82.5)
# print("RA: "+str(RA))
# print("DEC: "+str(DEC))
# print()
#
# RA,DEC = coordinate_transformations.hor_to_eq(47,90,datetime.datetime.now(),0,76,82.5)
# print("RA: "+str(RA))
# print("DEC: "+str(DEC))
# print()
# print(coordinate_transformations.new_longitude(76,-388))

# adc = coordinate_transformations.rotate_point_about_arbitrary_axis_in_3d(position_vector_of_tail_of_rotation_axis=[1,1,1],
#                                                                          position_vector_of_tip_of_rotation_axis=[0,0,0],
#                                                                          coordinates_to_rotate=[1,0,0],
#                                                                          rotation_angle_in_degrees=90)
# print(adc)
# rot_axis_coord = coordinate_transformations.rotate_point_about_arbitrary_axis_in_3d(position_vector_of_tail_of_rotation_axis=[0,0,1],
#                                                                          position_vector_of_tip_of_rotation_axis=[0,0,2],
#                                                                          coordinates_to_rotate=adc,
#                                                                          rotation_angle_in_degrees=-90)
#
# print(rot_axis_coord)
#
#
# adc =  coordinate_transformations.rotate_point_about_arbitrary_axis_in_3d(position_vector_of_tail_of_rotation_axis=[0,0,1],
#                                                                          position_vector_of_tip_of_rotation_axis=rot_axis_coord,
#                                                                          coordinates_to_rotate=adc,
#                                                                          rotation_angle_in_degrees=90)
# print(adc)
# print()
# adc = coordinate_transformations.rotate_point_about_arbitrary_axis_in_3d(position_vector_of_tail_of_rotation_axis=[0,0,1],
#                                                                          position_vector_of_tip_of_rotation_axis=[0,0,2],
#                                                                          coordinates_to_rotate=[1,0,1],
#                                                                          rotation_angle_in_degrees=90)
# print(adc)
# #
# rot_axis_coord = coordinate_transformations.rotate_point_about_arbitrary_axis_in_3d(position_vector_of_tail_of_rotation_axis=[0,0,1],
#                                                                          position_vector_of_tip_of_rotation_axis=[0,0,2],
#                                                                          coordinates_to_rotate=adc,
#                                                                          rotation_angle_in_degrees=90)
# print(rot_axis_coord)
# adc = coordinate_transformations.rotate_point_about_arbitrary_axis_in_3d(position_vector_of_tail_of_rotation_axis=[0,0,1],
#                                                                          position_vector_of_tip_of_rotation_axis=rot_axis_coord,
#                                                                          coordinates_to_rotate=adc,
#                                                                          rotation_angle_in_degrees=-90)
# print(adc)

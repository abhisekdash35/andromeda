import coordinate_transformations
import datetime
import time
while True:
    azimuth,altitude = coordinate_transformations.eq_to_hor(ra=15,
                                                            dec=20,
                                                            time_of_observation_in_datetime_format=datetime.datetime.now(),
                                                            latitude_of_observer=13,
                                                            longitude_of_observer=76,
                                                            local_standard_time_meridian=82.5)
    print("actual azimuth")
    print(azimuth)
    print("actual altitude: ")
    print(altitude)
    print()

    # RA,DEC = coordinate_transformations.hor_to_eq(azimuth,altitude,datetime.datetime.now(),13,76,82.5)
    # print(DEC)
    time.sleep(1)
# print(coordinate_transformations.new_longitude(76,-388))
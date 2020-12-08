from time_functions import local_solar_time,local_sidereal_time,eot_offset
import datetime
print(eot_offset(datetime.datetime.now()))
print(local_solar_time(datetime.datetime.now(),82.5,76.11,consider_eot_boolean=True))
print(local_sidereal_time(datetime.datetime.now(),82.5,76.11))



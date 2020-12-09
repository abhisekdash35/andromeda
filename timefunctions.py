import math
import datetime
from final_variables import equinox_epoch_in_UT

# Calculates the equation of time offset between clock time and actual solar time.
# Output is in minutes +ve or -ve
def eot_offset(day_of_the_year):

    B = 360 * (day_of_the_year - 81) / 365
    B = (3.14 / 180) * B
    EOT = 9.87 * math.sin(2 * B) - 7.53 * math.cos(B) - 1.5 * math.sin(B)
    return EOT

# Calculates local solar time by taking into account the local standard time meridian, longitude of observer,
# and the equation of time offset. Returns local solar time in datetime format.
def local_solar_time(local_date_and_clock_time_in_datetime_format,local_standard_time_meridian,longitude_of_observation):
    delta_hours = datetime.timedelta(hours=4*(local_standard_time_meridian - longitude_of_observation) / 60)
    local_solar_time = local_date_and_clock_time_in_datetime_format - delta_hours
    day_of_year = local_date_and_clock_time_in_datetime_format.timetuple().tm_yday
    eot = eot_offset(day_of_year)
    delta_hours =  datetime.timedelta(hours=eot/60)
    local_solar_time = local_solar_time + delta_hours
    return local_solar_time

# Calculates local sidereal time at a given longitude.
def local_sidereal_time(local_date_and_clock_time_in_datetime_format,local_standard_time_meridian,longitude_of_observation):
    equinox_epoch_in_decimal = (equinox_epoch_in_UT.hour * 3600 + equinox_epoch_in_UT.minute * 60 + equinox_epoch_in_UT.second) / 3600
    # Find longitude at which it is 12 noon solar time at moment of vernal equinox considering equation of time
    day_of_year_during_equinox = equinox_epoch_in_UT.timetuple().tm_yday
    eot = eot_offset(day_of_year_during_equinox)
    longitude_of_solar_noon_at_vernal_equinox_moment = (12 - equinox_epoch_in_decimal)*15 - eot/4
    # Clock time at 12 solar noon longitude during equinox
    time_delta = (longitude_of_solar_noon_at_vernal_equinox_moment) * 4 / 60
    time_delta = datetime.timedelta(hours=time_delta)
    clock_time_at_longitude_of_solar_noon_at_vernal_equinox_moment = equinox_epoch_in_UT + time_delta

    # Calculate local clock time now at the noon longitude during equinox
    long_diff = longitude_of_solar_noon_at_vernal_equinox_moment - longitude_of_observation
    time_delta = datetime.timedelta(hours=(long_diff)*4/60)
    clock_time_now_at_longitude_of_solar_noon_at_vernal_equinox_moment = local_date_and_clock_time_in_datetime_format + time_delta

    # Calculate number of  seconds that have passed since equinox
    num_of_seconds = int((clock_time_now_at_longitude_of_solar_noon_at_vernal_equinox_moment -
                            clock_time_at_longitude_of_solar_noon_at_vernal_equinox_moment).total_seconds())
    num_of_sidereal_days = num_of_seconds / 86164
    frac_part_of_sidereal_days = num_of_sidereal_days - int(num_of_sidereal_days)

    sidereal_time_now_at_longitude_of_solar_noon_at_vernal_equinox_moment = (frac_part_of_sidereal_days) * 24
    # Find sidereal time at observer longitude
    sidereal_time_at_observer_longitude = sidereal_time_now_at_longitude_of_solar_noon_at_vernal_equinox_moment - (24 / 360) * long_diff
    hr = int(sidereal_time_at_observer_longitude)
    min_with_frac = (sidereal_time_at_observer_longitude - hr)*60
    min = int(min_with_frac)
    sec = int((min_with_frac - min)*60)
    sidereal_time_at_observer_longitude_in_datetime_format = datetime.time(hr,min,sec)
    return sidereal_time_at_observer_longitude_in_datetime_format
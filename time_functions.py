import math
import datetime
from final_variables import equinox_epoch_in_UT

# Return true if year is leap year
# else return false
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Calculates the equation of time offset between clock time and actual solar time.
# Output is in minutes +ve or -ve
def eot_offset(local_datetime_in_datetime_format):
    day_of_the_year = local_datetime_in_datetime_format.timetuple().tm_yday
    year = local_datetime_in_datetime_format.year
    if is_leap_year(year):
        B = 360 * (day_of_the_year - 81) / 366
    else:
        B = 360 * (day_of_the_year - 81) / 365
    B = (3.14 / 180) * B
    EOT = 9.87 * math.sin(2*B) - 7.53 * math.cos(B) - 1.5 * math.sin(B)
    return EOT

# Calculates local solar time by taking into account the local standard time meridian, longitude of observer,
# and the equation of time offset. Returns local solar time in datetime format.
def local_solar_time(local_date_and_clock_time_in_datetime_format,local_standard_time_meridian,longitude_of_observation,consider_eot_boolean):
    delta_hours = datetime.timedelta(hours=4*(local_standard_time_meridian - longitude_of_observation) / 60)
    local_solar_time = local_date_and_clock_time_in_datetime_format - delta_hours

    if (consider_eot_boolean == True):
        eot = eot_offset(local_date_and_clock_time_in_datetime_format)
        delta_hours =  datetime.timedelta(hours=eot/60)
        local_solar_time = local_solar_time + delta_hours
    return local_solar_time

# Calculates local sidereal time at a given longitude.
def local_sidereal_time(local_date_and_clock_time_in_datetime_format,
                        local_standard_time_meridian,
                        longitude_of_observation):
    equinox_epoch_in_decimal = convert_time_to_decimal(equinox_epoch_in_UT)
    # Find longitude at which it is 12 noon solar time at moment of vernal equinox considering equation of time
    eot = eot_offset(equinox_epoch_in_UT)
    longitude_of_solar_noon_at_vernal_equinox_moment = (12 - equinox_epoch_in_decimal)*15 - eot/4
    # Clock time at 12 solar noon longitude during equinox
    time_delta = longitude_of_solar_noon_at_vernal_equinox_moment * 4 / 60
    time_delta = datetime.timedelta(hours=time_delta)
    clock_time_at_longitude_of_solar_noon_at_vernal_equinox_moment = equinox_epoch_in_UT + time_delta

    # Calculate local longitude time now at the noon longitude during equinox
    longitude_time_now_at_longitude_of_observation = local_solar_time(local_date_and_clock_time_in_datetime_format,
                                                                  local_standard_time_meridian,
                                                                  longitude_of_observation,
                                                                  False)
    long_diff = longitude_of_solar_noon_at_vernal_equinox_moment - longitude_of_observation
    time_delta = datetime.timedelta(hours=(long_diff)*4/60)
    clock_time_now_at_longitude_of_solar_noon_at_vernal_equinox_moment = \
        longitude_time_now_at_longitude_of_observation + time_delta

    # Calculate number of  seconds that have passed since equinox
    num_of_seconds = int((clock_time_now_at_longitude_of_solar_noon_at_vernal_equinox_moment -
                            clock_time_at_longitude_of_solar_noon_at_vernal_equinox_moment).total_seconds())
    num_of_sidereal_days = num_of_seconds / 86164
    frac_part_of_sidereal_days = num_of_sidereal_days - int(num_of_sidereal_days)

    sidereal_time_now_at_longitude_of_solar_noon_at_vernal_equinox_moment = (frac_part_of_sidereal_days) * 24
    # Find sidereal time at observer longitude
    sidereal_time_at_observer_longitude = sidereal_time_now_at_longitude_of_solar_noon_at_vernal_equinox_moment - (24 / 360) * long_diff

    if sidereal_time_at_observer_longitude < 0:
        sidereal_time_at_observer_longitude = 24 + sidereal_time_at_observer_longitude

    hr = int(sidereal_time_at_observer_longitude)
    min_with_frac = (sidereal_time_at_observer_longitude - hr)*60
    min = int(min_with_frac)
    sec = int((min_with_frac - min)*60)
    sidereal_time_at_observer_longitude_in_datetime_format = datetime.time(hr,min,sec)
    return sidereal_time_at_observer_longitude_in_datetime_format

def convert_time_to_decimal(time_in_time_format):
    return (time_in_time_format.hour * 3600 +
            time_in_time_format.minute * 60 +
            time_in_time_format.second) / 3600
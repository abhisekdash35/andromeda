# project_andromeda
A python library for astronomers (Under Construction)

## Files:

### coordinate_transformations.py
To be added
### 1. time_functions.py
#### time_functions.is_leap_year(year)
Checks whether year passed is a leap year or not.
##### Parameters: 
year
##### returns:
True if year is leap year else returns False

#### time_functions.eot_offset(local_datetime_in_datetime_format)
Calculates the equation of time offset depending on the day of the year.
##### Parameters: 
local_datetime_in_datetime_format: Local date and time in standard datetime format 
##### returns:
EOT offset in minutes.

#### time_functions.eot_offset(local_datetime_in_datetime_format)
Calculates the equation of time offset depending on the day of the year.
##### Parameters: 
local_datetime_in_datetime_format: Local date and time in standard datetime format 
##### returns:
EOT offset in minutes.

#### local_solar_time(local_date_and_clock_time_in_datetime_format,local_standard_time_meridian,longitude_of_observation,consider_eot_boolean)
Calculates the local solar time.
##### Parameters: 
local_date_and_clock_time_in_datetime_format: Local date and clock time in standard datetime format.
local_standard_time_meridian: The standard time meridian (for e.g. +82.5 for Indian Standard Time)
longitude_of_observation: The longitude at which solar time is required. Range is -180 to +180
consider_eot_boolean: Whether to consider equation of time offset.
##### returns:
The local solar time at observer position.




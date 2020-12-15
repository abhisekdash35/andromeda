# project_andromeda
A python library for astronomers (Under Construction)

## Files:

### 1. coordinate_transformations.py

#### calculate_projection_of_vector_on_plane(vector, surface_normal_of_plane)
Calculates projection of a vector on a plane given by its surface normal.
##### Parameters: 
vector: The input vector
surface_normal_of_plane: The surface normal of the plane on which the projection of vector is sought.
##### returns:
True if year is leap year else returns False


### 2. time_functions.py

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

#### local_sidereal_time(local_date_and_clock_time_in_datetime_format,
####                        local_standard_time_meridian,
####                        longitude_of_observation)
Calculates the local sidereal time.
##### Parameters: 
local_date_and_clock_time_in_datetime_format: Local date and clock time in standard datetime format.
local_standard_time_meridian: The standard time meridian (for e.g. +82.5 for Indian Standard Time)
longitude_of_observation: The longitude at which solar time is required. Range is -180 to +180
##### returns:
The local sidereal time at observer position.

#### convert_time_to_decimal(time_in_time_format)
Converts time in time or datetime format to decimal. For e.g 2020-12-15 23:30:00 is converted to 23.5
##### Parameters: 
time_in_time_format: Local date and clock time in standard datetime format. Also accepts time
##### returns:
The time in decimal.

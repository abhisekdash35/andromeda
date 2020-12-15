# project_andromeda
A python library for astronomers (Under Construction)

## Files:

### <span style="color:blue"> 1. coordinate_transformations.py </span>

Functions in this file:
####  coordinate_transformations.calculate_projection_of_vector_on_plane(vector, surface_normal_of_plane)

Calculates projection of a vector on a plane given by its surface normal.

##### Parameters: 
vector: The input vector.

surface_normal_of_plane: The surface normal of the plane on which the projection of vector is sought.

##### returns:
The projection of vector on the plane defined by its surface normal.

####  coordinate_transformations.rotate_point_about_arbitrary_axis_in_3d(position_vector_of_tail_of_rotation_axis, position_vector_of_tip_of_rotation_axis, coordinates_to_rotate, rotation_angle_in_degrees)

Rotates a point about an arbitrary vector in 3D. Returns coordinates of rotated points.
##### Parameters:

position_vector_of_tail_of_rotation_axis: The position vector of the tail of rotation axis.

position_vector_of_tip_of_rotation_axis: The position vector of the tip of rotation axis.

coordinates_to_rotate: Coordinates to rotate

rotation_angle_in_degrees: Rotation angle in degrees.

##### returns:

The rotated coordinates.

#### coordinate_transformations.eq_to_hor(ra, dec, time_of_observation_in_datetime_format, latitude_of_observer, longitude_of_observer, local_standard_time_meridian)

Converts equatorial coordinates of right ascension and declination to horizon coordinates of azimuth ad elevation.

##### Parameters: 

ra: The right ascension of the object in decimal hours between 0 and 24. 

dec: The declination of the object in degrees. Negative for southern latitudes.

time_of_observation_in_datetime_format: The local time of observation in standard datetime format.

latitude_of_observer: Latitude of observer.

longitude_of_observer: Longitude of observer.

local_standard_time_meridian: The local standard time meridian. For e.g +82.5 for Indian Standard Time

##### returns:
The azimuth and altitude at observer's location.

####  coordinate_transformations.hor_to_eq(azimuth, altitude,  time_of_observation_in_datetime_format, latitude_of_observer, longitude_of_observer, local_standard_time_meridian)

Converts equatorial coordinates of right ascension and declination to horizon coordinates of azimuth ad elevation.

##### Parameters: 

azimuth: The azimuth angle of the object at observer's location.

altitude: The altitude angle of the object at observer's location.

time_of_observation_in_datetime_format: The local time of observation in standard datetime format.

latitude_of_observer: Latitude of observer.

longitude_of_observer: Longitude of observer.

local_standard_time_meridian: The local standard time meridian. For e.g +82.5 for Indian Standard Time

##### returns:

The right ascension and declination of the object.


### 2. time_functions.py

Functions in this file:
####  time_functions.is_leap_year(year)

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

#### local_solar_time(local_date_and_clock_time_in_datetime_format, local_standard_time_meridian, longitude_of_observation, consider_eot_boolean)

Calculates the local solar time.

##### Parameters: 

local_date_and_clock_time_in_datetime_format: Local date and clock time in standard datetime format.

local_standard_time_meridian: The standard time meridian (for e.g. +82.5 for Indian Standard Time)

longitude_of_observation: The longitude at which solar time is required. Range is -180 to +180

consider_eot_boolean: Whether to consider equation of time offset.

##### returns:

The local solar time at observer position.

#### local_sidereal_time(local_date_and_clock_time_in_datetime_format, local_standard_time_meridian, longitude_of_observation)

Calculates the local sidereal time.

##### Parameters:

local_date_and_clock_time_in_datetime_format: Local date and clock time in standard datetime format.

local_standard_time_meridian: The standard time meridian (for e.g. +82.5 for Indian Standard Time)

longitude_of_observation: The longitude at which solar time is required. Range is -180 to +180

##### returns:

The local sidereal time at observer position.

####  convert_time_to_decimal(time_in_time_format)

Converts time in time or datetime format to decimal. For e.g 2020-12-15 23:30:00 is converted to 23.5

##### Parameters: 

time_in_time_format: Local date and clock time in standard datetime format. Also accepts time in time format.

##### returns:

The time in decimal.

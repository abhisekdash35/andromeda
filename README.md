# project_andromeda 
(Under construction)

A python library for astronomers. 

Borne simply out of boredom and nothing much to do in the pandemic stricken year of 2020, project_andromeda is a humble library written to satiate my need for mathematical gratification. I started working on it after planning to buy a telescope. The question that spurred the development of this library was "at which direction do I need to point to see a certain celestial object ?". 

The library primarily uses elementary vector algebra to convert between horizon and equatorial coordinate systems and vice versa. The library also calculates things like sidereal time and solar time.
Currently the library has 3 files with 10 functions. It has been tested with calculators available online and other third party libraries. I plan on expanding the scope of this library with time.

## Files:

### 1. coordinate_transformations.py

This file contains functions related to transformations from one coordinate system to another. (Mainly from horizon coordinates of azimuth and altitude to equatorial coordinates of declination and right ascension and vice versa.). 

The functions implemented till now are listed below

* coordinate_transformations . calculate_projection_of_vector_on_plane(vector, surface_normal_of_plane)
  
  _Calculates projection of a vector on a plane given by its surface normal._

  **_Parameters:_**
  
  _vector: The input vector._

  _surface_normal_of_plane: The surface normal of the plane on which the projection of vector is sought._

  **_returns:_**
  
  _The projection of vector on the plane defined by its surface normal._

* coordinate_transformations.rotate_point_about_arbitrary_axis_in_3d(position_vector_of_tail_of_rotation_axis, position_vector_of_tip_of_rotation_axis, coordinates_to_rotate, rotation_angle_in_degrees)

Rotates a point about an arbitrary vector in 3D. Returns coordinates of rotated points.
**_Parameters:_**

_position_vector_of_tail_of_rotation_axis: The position vector of the tail of rotation axis._

_position_vector_of_tip_of_rotation_axis: The position vector of the tip of rotation axis._

_coordinates_to_rotate: Coordinates to rotate_

_rotation_angle_in_degrees: Rotation angle in degrees._

**_returns:_**:

_The rotated coordinates._

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

This file deals with the time related functionalities in astronomy such as solar time, sidereal time etc.

The functions implemented till now are listed below.

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

### 3. final_variables.py
This file contains variables which are required for the internal workings of the library.

import math
import time_functions
import numpy as np
import sys


# Function calculates projection of an arbitrary vector
# on an arbitrary plane given by its normal vector representation.
def calculate_projection_of_vector_on_plane(vector, surface_normal_of_plane):
    k = np.dot(vector, surface_normal_of_plane) / np.sum(np.square(surface_normal_of_plane))
    vp = vector - k * surface_normal_of_plane
    return vp


# Function rotates a point about an arbitrary axis.
# Accomplished by aligning the rotation axis with z axis and then rotating by required angle.
# Then the backward transformation is done.
def calculate_theta_phi(rotation_axis):
    x = rotation_axis[0]
    y = rotation_axis[1]
    z = rotation_axis[2]
    theta = math.atan(x/z)
    phi = math.atan(y/math.sqrt(x**2 + z**2))
    if x == 0 and z < 0:
        return math.pi,phi
    elif x > 0 and y > 0 and z > 0:
        return theta,phi
    elif x > 0 and y > 0 and z < 0:
        return math.pi + theta,phi
    elif x > 0 and y < 0 and z > 0:
        return theta,phi
    elif x > 0 and y < 0 and z < 0:
        return theta,-(math.pi + phi)
    elif x < 0  and y > 0 and z > 0:
        return theta,phi
    elif x < 0 and y > 0 and z < 0:
        return theta,math.pi - phi
    elif x < 0 and y < 0 and z > 0:
        return theta,phi
    elif x < 0 and y < 0 and z < 0:
        return theta,-(math.pi + phi)


def rotate_point_about_arbitrary_axis_in_3d(position_vector_of_tail_of_rotation_axis,
                                            position_vector_of_tip_of_rotation_axis,
                                            coordinates_to_rotate,
                                            rotation_angle_in_degrees):
    rad_rotation_angle = math.radians(rotation_angle_in_degrees)

    # Convert to homogenous coordinates
    rotation_axis = np.round(np.array(position_vector_of_tip_of_rotation_axis) - np.array(position_vector_of_tail_of_rotation_axis),5)
    coordinates_to_rotate = list(coordinates_to_rotate)
    coordinates_to_rotate.append(1)
    coordinates_of_rotation_axis = position_vector_of_tail_of_rotation_axis
    translation_to_origin_matrix = [[1, 0, 0, -coordinates_of_rotation_axis[0]],
                                    [0, 1, 0, -coordinates_of_rotation_axis[1]],
                                    [0, 0, 1, -coordinates_of_rotation_axis[2]],
                                    [0, 0, 0, 1]]

    # Find angle between z axis and the projection of the shifted rotation axis on xz plane
    # Find angle between transformed rotation axis and z axis
    theta,phi = calculate_theta_phi(rotation_axis)

    # # Matrix for Rotating the shifted north tangent vector by -theta about y axis
    rotate_by_negative_theta_about_y_axis_matrix = [[math.cos(theta), 0, -math.sin(theta), 0],
                                                    [0, 1, 0, 0],
                                                    [math.sin(theta), 0, math.cos(theta), 0],
                                                    [0, 0, 0, 1]]

    # # Matrix for Rotating transformed north tangent vector by phi about x axis
    rotate_by_phi_about_x_axis_matrix = [[1, 0, 0, 0],
                                         [0, math.cos(phi), -math.sin(phi), 0],
                                         [0, math.sin(phi), math.cos(phi), 0],
                                         [0, 0, 0, 1]]

    # Rotate coordinates_to_rotate by rotation angle about z axis
    rotate_by_negative_azimuth_about_z_axis_matrix = [
        [math.cos(rad_rotation_angle), -math.sin(rad_rotation_angle), 0, 0],
        [math.sin(rad_rotation_angle), math.cos(rad_rotation_angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]]
    # Rotate by negative phi about x
    rotate_by_negative_phi_about_x_matrix = [[1, 0, 0, 0],
                                             [0, math.cos(phi), math.sin(phi), 0],
                                             [0, -math.sin(phi), math.cos(phi), 0],
                                             [0, 0, 0, 1]]
    # Rotate by theta about y
    rotate_by_theta_about_y_matrix = [[math.cos(theta), 0, math.sin(theta), 0],
                                      [0, 1, 0, 0],
                                      [-math.sin(theta), 0, math.cos(theta), 0],
                                      [0, 0, 0, 1]]
    # Translate point from origin to observer location
    translation_to_observer_location_matrix = [[1, 0, 0, coordinates_of_rotation_axis[0]],
                                               [0, 1, 0, coordinates_of_rotation_axis[1]],
                                               [0, 0, 1, coordinates_of_rotation_axis[2]],
                                               [0, 0, 0, 1]]

    rot_coord = np.matmul(translation_to_observer_location_matrix,rotate_by_theta_about_y_matrix)
    rot_coord = np.matmul(rot_coord,rotate_by_negative_phi_about_x_matrix)
    rot_coord = np.matmul(rot_coord,rotate_by_negative_azimuth_about_z_axis_matrix)
    rot_coord = np.matmul(rot_coord,rotate_by_phi_about_x_axis_matrix)
    rot_coord = np.matmul(rot_coord,rotate_by_negative_theta_about_y_axis_matrix)
    rot_coord = np.matmul(rot_coord,translation_to_origin_matrix)
    rot_coord = np.matmul(rot_coord,coordinates_to_rotate)

    return rot_coord[0:3]


# Converts equatorial coordinates of RA/DEC to horizon coordinates of azimuth and
# altitude. Returns azimuth and altitude in degrees.

def eq_to_hor(ra,
              dec,
              time_of_observation_in_datetime_format,
              latitude_of_observer,
              longitude_of_observer,
              local_standard_time_meridian):
    # Calculate sidereal time at observer's location
    sidereal_time_at_observer_longitude = \
        time_functions.local_sidereal_time(time_of_observation_in_datetime_format,
                                           local_standard_time_meridian,
                                           longitude_of_observer)
    # Calculate hour angle

    sidereal_time_at_observer_longitude = time_functions.convert_time_to_decimal(sidereal_time_at_observer_longitude)
    HA = sidereal_time_at_observer_longitude - ra

    # Calculate longitude of substellar point
    longitude_of_substellar_point = new_longitude(longitude_of_observer,-HA*360/24)
    latitude_of_substellar_point = dec

    # Convert angles in degrees to radians.
    # Find the sine and cosine of all angles involved to convert spherical coordinates
    # of  location of observer and location of substellar point at observation time to cartesian coordinates.

    rad_lat_obs = math.radians(latitude_of_observer)
    rad_lon_obs = math.radians(longitude_of_observer)
    rad_lat_ss = math.radians(latitude_of_substellar_point)
    rad_lon_ss = math.radians(longitude_of_substellar_point)

    cos_lat_obs = math.cos(rad_lat_obs)
    sin_lat_obs = math.sin(rad_lat_obs)
    cos_lon_obs = math.cos(rad_lon_obs)
    sin_lon_obs = math.sin(rad_lon_obs)

    cos_lat_ss = math.cos(rad_lat_ss)
    sin_lat_ss = math.sin(rad_lat_ss)
    cos_lon_ss = math.cos(rad_lon_ss)
    sin_lon_ss = math.sin(rad_lon_ss)

    # Unit position vectors of observer and substellar points in cartesian coordinates

    position_vector_of_observer = np.array([cos_lat_obs * cos_lon_obs,
                                            cos_lat_obs * sin_lon_obs,
                                            sin_lat_obs])
    position_vector_of_substellar_point = np.array([cos_lat_ss * cos_lon_ss,
                                                    cos_lat_ss * sin_lon_ss,
                                                    sin_lat_ss])
    # Project the vector from observer location and North Pole on the tangent plane at observer.
    # This gives the direction vector of local North.
    # Also project the vector from observer to substellar point to the same plane
    # to provide the direction of azimuth.
    # Angle between these 2 vectors gives the azimuth if HA is <0.
    # If HA is greater than 0, subtract from 360 to get azimuth.

    # Project observer to substellar point vector to surface tangent plane at observer.
    observer_to_substellar_point_vector = position_vector_of_substellar_point - position_vector_of_observer + 1e-12
    surface_normal_to_local_tangent_plane_at_observer = position_vector_of_observer
    projection_of_observer_to_substellar_point_vector_on_surface_tangent_plane_at_observer = calculate_projection_of_vector_on_plane(
            observer_to_substellar_point_vector,
            surface_normal_to_local_tangent_plane_at_observer)
    projection_of_observer_to_substellar_point_vector_on_surface_tangent_plane_at_observer = \
        projection_of_observer_to_substellar_point_vector_on_surface_tangent_plane_at_observer / np.sqrt(
            np.sum(np.square(projection_of_observer_to_substellar_point_vector_on_surface_tangent_plane_at_observer)))
    # Project the observer to north pole vector to get local north vector
    position_vector_of_north_pole = np.array([0, 0, 1])
    observer_to_north_pole_vector = position_vector_of_north_pole - position_vector_of_observer
    local_tangent_pointing_north_vector = \
        calculate_projection_of_vector_on_plane(observer_to_north_pole_vector,
                                                surface_normal_to_local_tangent_plane_at_observer)
    local_tangent_pointing_north_vector = \
        local_tangent_pointing_north_vector / \
        np.sqrt(np.sum(np.square(local_tangent_pointing_north_vector)))
    azimuth = math.acos(np.dot(local_tangent_pointing_north_vector,
                               projection_of_observer_to_substellar_point_vector_on_surface_tangent_plane_at_observer))
    azimuth = math.degrees(azimuth)

    if sidereal_time_at_observer_longitude > ra:
        d1 = np.abs(sidereal_time_at_observer_longitude - ra)
        d2 = np.abs(sidereal_time_at_observer_longitude - (ra + 24))

        if d1 < d2:
            azimuth = 360 - azimuth
        else:
            azimuth = azimuth
    elif ra > sidereal_time_at_observer_longitude:
        d1 = np.abs(ra - sidereal_time_at_observer_longitude)
        d2 = np.abs(ra - (sidereal_time_at_observer_longitude + 24))

        if d1 < d2:
            azimuth = azimuth
        else:
            azimuth = 360 - azimuth
    elif ra == sidereal_time_at_observer_longitude:
        azimuth = 180

    # # Calculate Altitude
    altitude_ = math.acos(cos_lat_obs * cos_lat_ss * math.cos(rad_lon_obs - rad_lon_ss) +
                          sin_lat_obs * sin_lat_ss)

    altitude_ = math.degrees(altitude_)
    altitude = 90 - altitude_
    return azimuth, altitude


# Function converts horizon coordinates of altitude and azimuth to
# equatorial coordinates of RA and DEC. RA is returned as hour between 0 and 24
# and DEC is returned in degrees.

def hor_to_eq(azimuth,
              altitude,
              time_of_observation_in_datetime_format,
              latitude_of_observer,
              longitude_of_observer,
              local_standard_time_meridian):
    # Calculate sidereal time at observer's location
    sidereal_time_at_observer_longitude = \
        time_functions.local_sidereal_time(time_of_observation_in_datetime_format,
                                           local_standard_time_meridian,
                                           longitude_of_observer)
    # Convert all known angles to radians and compute sine and cosine of the angles
    rad_lat_obs = math.radians(latitude_of_observer)
    rad_lon_obs = math.radians(longitude_of_observer)
    cos_lat_obs = math.cos(rad_lat_obs)
    sin_lat_obs = math.sin(rad_lat_obs)
    cos_lon_obs = math.cos(rad_lon_obs)
    sin_lon_obs = math.sin(rad_lon_obs)

    # Compute vectors in cartesian coordinates
    position_vector_of_observer = np.array([cos_lat_obs * cos_lon_obs, cos_lat_obs * sin_lon_obs, sin_lat_obs])
    surface_normal_to_local_tangent_plane_at_observer = position_vector_of_observer
    position_vector_of_north_pole = np.array([0, 0, 1])

    observer_to_north_pole_vector = position_vector_of_north_pole - position_vector_of_observer
    local_tangent_pointing_north_vector = calculate_projection_of_vector_on_plane(observer_to_north_pole_vector,
                                                                                  surface_normal_to_local_tangent_plane_at_observer)
    coordinates_of_local_tangent_pointing_north = position_vector_of_observer + \
                                                  np.array(local_tangent_pointing_north_vector)


    position_vector_of_tail_of_rotation_axis = position_vector_of_observer
    position_vector_of_tip_of_rotation_axis = 2*position_vector_of_observer

    # Find expression for azimuth direction coordinates by rotating about the normal of tangent plane at observer
    azimuth_direction_coordinates = rotate_point_about_arbitrary_axis_in_3d(
        position_vector_of_tail_of_rotation_axis=position_vector_of_tail_of_rotation_axis,
        position_vector_of_tip_of_rotation_axis=position_vector_of_tip_of_rotation_axis,
        coordinates_to_rotate=coordinates_of_local_tangent_pointing_north,
        rotation_angle_in_degrees=-azimuth)
    # Rotate coordinates of azimuth direction about surface normal at observer by an additional 90 degrees

    coordinates_of_90_degree_away_from_azimuth = rotate_point_about_arbitrary_axis_in_3d(
        position_vector_of_tail_of_rotation_axis=position_vector_of_tail_of_rotation_axis,
        position_vector_of_tip_of_rotation_axis=position_vector_of_tip_of_rotation_axis,
        coordinates_to_rotate=azimuth_direction_coordinates,
        rotation_angle_in_degrees=-90)

    # Rotate azimuth_direction_coordinates by elevation angle about the ninety_degree_away_vector axis from_azimuth_vector
    substellar_point_coordinates = rotate_point_about_arbitrary_axis_in_3d(
        position_vector_of_tail_of_rotation_axis=position_vector_of_tail_of_rotation_axis,
        position_vector_of_tip_of_rotation_axis=coordinates_of_90_degree_away_from_azimuth,
        coordinates_to_rotate=azimuth_direction_coordinates,
        rotation_angle_in_degrees=altitude)
    substellar_point_vector = substellar_point_coordinates - position_vector_of_tail_of_rotation_axis

    unit_substellar_point_vector = substellar_point_vector / np.linalg.norm(substellar_point_vector)

    DEC = math.asin(unit_substellar_point_vector[2])

    # Find longitude of substellar point
    sin_lon_ss = unit_substellar_point_vector[1] / math.cos(DEC)
    lon_ss = math.asin(sin_lon_ss)
    lon_ss = math.degrees(lon_ss)
    one_eighty_opposite_lon_obs = new_longitude(longitude_of_observer,180)

    # If azimuth is between 0 and 180 but lon_ss lies west of observer's longitude
    if (azimuth > 0 and azimuth < 180) and ((lon_ss < longitude_of_observer and lon_ss >= 0) or
                                          (lon_ss > one_eighty_opposite_lon_obs and lon_ss <= 0)):

        lon_ss = new_longitude(-lon_ss,180)
    # If azimuth is between 180 and 360 but lon_ss lies east of observer's longitude
    elif (azimuth > 180 and azimuth < 360) and ((lon_ss > longitude_of_observer and lon_ss <=180) or
                                                (lon_ss <=one_eighty_opposite_lon_obs and lon_ss <=-180)) :
        lon_ss = new_longitude(-lon_ss, 180)


    sidereal_time_at_observer_longitude = time_functions.convert_time_to_decimal(sidereal_time_at_observer_longitude)
    RA = sidereal_time_at_observer_longitude - (longitude_of_observer - lon_ss) / 15
    if RA < 0:
        RA = RA + 24
    elif RA > 24:
        RA = RA - 24
    DEC = math.degrees(DEC)

    return round(RA,5), round(DEC,5)

# Calculates new longitude from current longitude based on delta longitude
def new_longitude(longitude_in_degrees,
                  delta_longitude_in_degrees):
    delta_longitude_int = int(np.abs(delta_longitude_in_degrees) / 180)
    delta_longitude_mod = np.abs(delta_longitude_in_degrees) % 180

    if delta_longitude_int % 2 == 0:
        longitude_in_degrees = longitude_in_degrees
    else:
        if longitude_in_degrees >= 0:
            longitude_in_degrees = -(180 - longitude_in_degrees)
        else:
            longitude_in_degrees = 180 - np.abs(longitude_in_degrees)
    if longitude_in_degrees >= 0:
        if delta_longitude_in_degrees >= 0:
            lon_ss = longitude_in_degrees + delta_longitude_mod
            if lon_ss > 180:
                lon_ss = -(360 - lon_ss)
        else:
            lon_ss = longitude_in_degrees - delta_longitude_mod

    elif longitude_in_degrees < 0:
        if delta_longitude_in_degrees >= 0:
            lon_ss = longitude_in_degrees + delta_longitude_mod
        else:
            lon_ss = longitude_in_degrees - delta_longitude_mod
            if lon_ss < -180:
                lon_ss = 180 - (-180 - lon_ss)
    return lon_ss

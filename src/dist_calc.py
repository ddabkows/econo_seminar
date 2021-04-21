"""
Author: Dominik Dabkowski
Date:   26th march 2021
Code:   Adding float variable to the bygid data to know the distance to the biggest gdp grid
y: latitude
x: longitude
"""


import math


def dist_calc(src_long, src_lat, dst_long, dst_lat):
    to_meters: float = 6371e3

    src_rho = src_lat * math.pi / 180
    dst_rho = dst_lat * math.pi / 180

    delta_rho = (src_lat - dst_lat) * math.pi / 180
    delta_lambda = (src_long - dst_long) * math.pi / 180

    a = math.sin(delta_rho / 2) * math.sin(delta_rho / 2) + math.cos(src_rho) * \
        math.cos(dst_rho) * math.sin(delta_lambda / 2) * math.sin(delta_lambda / 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    d = to_meters * c

    return d

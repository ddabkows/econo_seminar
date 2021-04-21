"""
Author: Dominik Dabkowski
Date:   26th march 2021
Code:   Adding float variable to the bygid data to know the distance to the closest resourcesfull grid
y: latitude
x: longitude
"""

import pandas
import math
import dist_calc
pandas.options.mode.chained_assignment = None


def main():
    with open("../data/oreandfuel.csv") as dataset:
        database = pandas.read_csv(dataset)
        size: int = len(database["gid"])
        database["distance_to_ore"] = math.inf
        database["distance_to_petrol"] = math.inf
        for row_starting_points in range(0, size):
            src_iso: str = database["isocode"][row_starting_points]
            src_long = database["xcoord"][row_starting_points]
            src_lat = database["ycoord"][row_starting_points]
            for row_destination_points in range(0, size):
                dst_iso: str = database["isocode"][row_destination_points]
                if src_iso == dst_iso:
                    if database["diamsec_s"][row_destination_points] == 1 \
                            or database["diamprim_s"][row_destination_points] == 1 \
                            or database["gem_s"][row_destination_points] == 1 \
                            or database["goldplacer_s"][row_destination_points] == 1 \
                            or database["goldvein_s"][row_destination_points] == 1 \
                            or database["goldsurface_s"][row_destination_points] == 1 \
                            or database["petroleum_s"][row_destination_points] == 1:
                        dst_long = database["xcoord"][row_destination_points]
                        dst_lat = database["ycoord"][row_destination_points]
                        distance: float = dist_calc.dist_calc(src_long, src_lat, dst_long, dst_lat)
                        if distance < database["distance_to_ore"][row_starting_points]:
                            database["distance_to_ore"][row_starting_points] = distance
                    if database["petroleum_s"][row_destination_points] == 1:
                        dst_long = database["xcoord"][row_destination_points]
                        dst_lat = database["ycoord"][row_destination_points]
                        distance: float = dist_calc.dist_calc(src_long, src_lat, dst_long, dst_lat)
                        if distance < database["distance_to_petrol"][row_starting_points]:
                            database["distance_to_petrol"][row_starting_points] = distance
            print(str(round(float(row_starting_points/size)*100, 2)) + " % done.")
        database.to_csv("/home/dominik/Documents/seminar_econo/econo_seminar/oreandfuel_distances.csv")


if __name__ == "__main__":
    main()

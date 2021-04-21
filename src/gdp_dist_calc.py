"""
Author: Dominik Dabkowski
Date:   26th march 2021
Code:   Adding float variable to the bygid data to know the distance to the biggest gdp grid
y: latitude
x: longitude
"""


import pandas
import dist_calc
pandas.options.mode.chained_assignment = None


def main():
    with open("../data/gdp per cell (ppp and pc).csv") as dataset:
        database = pandas.read_csv(dataset)
        size: int = len(database["gid"])
        database["dist_avg_gcp_ppp"] = 0
        database["dist_avg_gcp_ppc"] = 0
        for row_to_check in range(0, size):
            src_iso: str = database["isocode"][row_to_check]
            src_long: float = database["xcoord"][row_to_check]
            src_lat: float = database["ycoord"][row_to_check]
            biggest_ppp: float = database["avg_gcp_ppp"][row_to_check]
            biggest_ppc: float = database["avg_gcpppc"][row_to_check]

            for row_to_compare in range(0, size):
                dst_iso: str = database["isocode"][row_to_compare]

                if src_iso == dst_iso:
                    if database["avg_gcp_ppp"][row_to_compare] > biggest_ppp:
                        biggest_ppp = database["dist_avg_gcp_ppp"][row_to_compare]
                        dst_long: float = database["xcoord"][row_to_compare]
                        dst_lat: float = database["ycoord"][row_to_compare]
                        distance: float = dist_calc.dist_calc(src_long, src_lat, dst_long, dst_lat)
                        database["dist_avg_gcp_ppp"][row_to_check] = distance
                    if database["dist_avg_gcp_ppc"][row_to_compare] > biggest_ppc:
                        biggest_ppc = database["dist_avg_gcp_ppc"][row_to_compare]
                        dst_long: float = database["xcoord"][row_to_compare]
                        dst_lat: float = database["ycoord"][row_to_compare]
                        distance: float = dist_calc.dist_calc(src_long, src_lat, dst_long, dst_lat)
                        database["dist_avg_gcp_ppc"][row_to_check] = distance

            print(str(round(float(row_to_check/size)*100, 2)) + " % done.")
        database.to_csv("/home/dominik/Documents/seminar_econo/econo_seminar/dist_to_biggest_gdps.csv")


if __name__ == "__main__":
    main()

"""
Author: Dominik Dabkowski
Date:   26th march 2021
Code:   Adding last regime change year variable to the workingfile data to know
        if a regime changed occured 5 years ago or less, exactly 6 years ago and more than 6 years ago
"""

import pandas
import time

FIRST_ITERATION: int = 6


def main():
    with open("../data/regime_change_5_years.csv") as dataset:
        database = pandas.read_csv(dataset,
                                   usecols=["id", "gid", "isocode", "year", "ConfIntra", "transition",
                                            "logcapdist", "avg_polity2", "logbdist2", "degtemper", "prec"],
                                   sep=',')
        print(database.head())
        size: int = len(database["year"])
        database["transition6"] = 0
        for row_starting_points in range(FIRST_ITERATION, size):
            regime_change_5_years: int = 0
            for row_check in range(row_starting_points - FIRST_ITERATION, row_starting_points):
                if database["gid"][row_starting_points] == database["gid"][row_check]:
                    if database["year"][row_starting_points] - database["year"][row_check] == 6:
                        if database["transition"][row_check] == 1:
                            regime_change_5_years = 2
                    if database["year"][row_starting_points] - database["year"][row_check] <= 5:
                        if database["transition"][row_check] == 1:
                            regime_change_5_years = 1
            print("Recording " + str(regime_change_5_years) + " to " + str(database["gid"][row_starting_points]) +
                  ", " + str(database["isocode"][row_starting_points]) + " in " +
                  str(database["year"][row_starting_points]) + ".")
            database["transition6"][row_starting_points] = regime_change_5_years
            if (row_starting_points / size * 100) % 2 == 0:
                print(" " * 10 + str(round(row_starting_points / size * 100, 2)) + " % of the data covered.")
                time.sleep(1)
        database.to_csv("/home/dominik/Documents/seminar_econo/econo_seminar/data/regime_change_5_years.csv")


if __name__ == "__main__":
    main()

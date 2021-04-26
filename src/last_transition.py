"""
Author: Dominik Dabkowski
Date:   26th march 2021
Code:   Adding last regime change year variable to the workingfile data to know
        takes the last regime change
"""


import pandas
import time
import numpy


FIRST_YEAR: int = 1946


def main():
    with open("../data/regime_change_5_years.csv") as dataset:
        database = pandas.read_csv(dataset,
                                   usecols=["id", "gid", "isocode", "year", "ConfIntra", "transition",
                                            "logcapdist", "avg_polity2", "logbdist2", "degtemper", "prec"],
                                   sep=',')
        print(database.head())
        size: int = len(database["year"])
        database["last transition"] = numpy.nan
        for row_starting_points in range(0, size):
            last_transition: int = numpy.nan
            for row_check in range(row_starting_points - int(database["year"][row_starting_points] - FIRST_YEAR),
                                   row_starting_points):
                if database["gid"][row_check] == database["gid"][row_starting_points]:
                    if database["transition"][row_check] == 1:
                        last_transition = database["year"][row_starting_points] - database["year"][row_check]
            print("Recording " + str(last_transition) + " to " + str(database["gid"][row_starting_points]) +
                  ", " + str(database["isocode"][row_starting_points]) + " in " +
                  str(database["year"][row_starting_points]) + ".")
            database["last transition"][row_starting_points] = last_transition
            if (row_starting_points / size * 100) % 2 == 0:
                print(" " * 10 + str(round(row_starting_points / size * 100, 2)) + " % of the data covered.")
                time.sleep(1)
        database.to_csv("/home/dominik/Documents/seminar_econo/econo_seminar/data/last_transition.csv")


if __name__ == "__main__":
    main()

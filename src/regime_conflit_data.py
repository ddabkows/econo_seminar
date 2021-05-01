"""
Author: Dominik Dabkowski
Date:   26th march 2021
Code:   Adding last regime change year variable to the workingfile data to know
        if a regime changed occured 5 years ago or less, exactly 6 years ago and more than 6 years ago
"""


import pandas
import numpy
import time

FIRST_ITERATION: int = 6
FIRST_DATE: int = 1946
LAST_DATE: int = 2005


def main():
    with open("../data/regime_change_5_years.csv") as dataset:
        database = pandas.read_csv(dataset,
                                   usecols=["id", "gid", "isocode", "year", "ConfIntra", "transition",
                                            "logcapdist", "avg_polity2", "logbdist2", "degtemper", "prec"],
                                   sep=',')
        print(database.head())
        size: int = len(database["year"])
        database["last_transition"] = numpy.nan
        database["next_transition"] = numpy.nan
        database["pre_transition"] = numpy.nan
        for row_starting_points in range(0, size):
            last_transition: float = numpy.nan
            next_transition: float = numpy.nan
            for row_check in range(row_starting_points-1, -1, -1):
                if database["gid"][row_starting_points] == database["gid"][row_check]:
                    if database["transition"][row_check] == 1:
                        last_transition = database["year"][row_starting_points] - database["year"][row_check]
                        break
                elif database["gid"][row_starting_points] != database["gid"][row_check]:
                    break
            for row_check in range(row_starting_points+1, size):
                if database["gid"][row_starting_points] == database["gid"][row_check]:
                    if database["transition"][row_check] == 1:
                        next_transition = database["year"][row_check] - database["year"][row_starting_points]
                        break
                elif database["gid"][row_starting_points] != database["gid"][row_check]:
                    break
            if (next_transition < last_transition) and (next_transition <= 5):
                database["pre_transition"][row_starting_points] = 1
            elif (last_transition < next_transition) and (last_transition <= 5):
                database["pre_transition"][row_starting_points] = 0
            database["last_transition"][row_starting_points] = last_transition
            database["next_transition"][row_starting_points] = next_transition

            if (row_starting_points / size * 100) % 2 == 0:
                print(" " * 10 + str(round(row_starting_points / size * 100, 2)) + " % of the data covered.")
                time.sleep(1)
        database.to_csv("/home/dominik/Documents/seminar_econo/econo_seminar/data/regime_change_5_years.csv")


if __name__ == "__main__":
    main()

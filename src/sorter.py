"""
Author: Dominik Dabkowski
Date:   26th march 2021
Code:   Sorting the data
"""


import pandas


def main():
    with open("../data/workingfile2_extracted_data.csv") as dataset:
        database = pandas.read_csv(dataset,
                                   usecols=["id", "gid", "isocode", "year", "ConfIntra", "transition",
                                            "logcapdist", "avg_polity2", "logbdist2", "degtemper", "prec"],
                                   sep=',')
        dataframe = database.sort_values(by=["gid", "year"])
        dataframe.to_csv("/home/dominik/Documents/seminar_econo/econo_seminar/data/regime_change_5_years.csv")


if __name__ == "__main__":
    main()

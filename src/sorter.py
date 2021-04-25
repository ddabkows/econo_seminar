"""
Author: Dominik Dabkowski
Date:   26th march 2021
Code:   Sorting the data
"""


import pandas


def main():
    with open("../data/workingfile2_extracted_data.csv") as dataset:
        database = pandas.read_csv(dataset,
                                   usecols=["id", "gid", "year", "conflict", "regime change", "logdistcap",
                                            "loggcppc", "logpop", "imr", "logttime", "logcellarea",
                                            "logdist_LNC", "mountain2000", "ycoord", "degtemper",
                                            "prec"],
                                   sep=',')
        dataframe = database.sort_values(by=["gid", "year"])
        dataframe.to_csv("/home/dominik/Documents/seminar_econo/econo_seminar/data/regime_change_5_years.csv")


if __name__ == "__main__":
    main()

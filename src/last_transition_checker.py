"""
Author: Dominik Dabkowski
Date:   26th march 2021
Code:   Analysing the data
"""


import pandas


def main():
    with open("../data/last_transition.csv") as dataset:
        database = pandas.read_csv(dataset,
                                   usecols=["id", "gid", "isocode", "year", "ConfIntra", "transition",
                                            "logcapdist", "avg_polity2", "logbdist2", "degtemper", "prec",
                                            "last transition"],
                                   sep=',')
        size: int = len(database["ConfIntra"])
        no_data: int = 0
        data: int = 0
        for row in range(0, size):
            if database["last transition"][row] >= 0:
                data += 1
            else:
                no_data += 1
        print("Sample size: " + str(size))
        print("\n Number of no data entries: " + str(no_data))
        print("\n Proportion of no data entries: " + str(no_data/size))
        print("\n Number of entries with data: " + str(data))
        print("\n Proportion of entries with data: " + str(data/size))


if __name__ == "__main__":
    main()

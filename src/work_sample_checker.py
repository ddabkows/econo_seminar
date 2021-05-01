"""
Author: Dominik Dabkowski
Date:   26th march 2021
Code:   Analysing the data
"""


import pandas


def main():
    with open("../data/regime_change_5_years.csv") as dataset:
        database = pandas.read_csv(dataset,
                                   usecols=["id", "gid", "isocode", "year", "ConfIntra", "transition",
                                            "logcapdist", "avg_polity2", "logbdist2", "degtemper", "prec",
                                            "pre_transition"],
                                   sep=',')
        size: int = len(database["ConfIntra"])
        pre_transition: int = 0
        post_transition: int = 0
        for row in range(0, size):
            if database["pre_transition"][row] == 0:
                post_transition += 1
            elif database["pre_transition"][row] == 1:
                pre_transition += 1
        print("Sample size: " + str(size))
        print("\n Number of pre-transition entries: " + str(pre_transition))
        print("Proportion of the pre-transition group (to the sample size): " + str(pre_transition/size))
        print("\n Number of post-transition entries: " + str(post_transition))
        print("Proportion of the post-transition group (to the sample size): " + str(post_transition/size))


if __name__ == "__main__":
    main()

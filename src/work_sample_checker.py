"""
Author: Dominik Dabkowski
Date:   26th march 2021
Code:   Analysing the data
"""


import pandas


def main():
    with open("../data/regime_change_5_years.csv") as dataset:
        database = pandas.read_csv(dataset,
                                   usecols=["id", "gid", "year", "conflict", "regime change",
                                            "regime change within 5 years"],
                                   sep=',')
        size: int = len(database["regime change within 5 years"])
        no_regime_change: int = 0
        iteration_6_years: int = 0
        iteration_less_6_years: int = 0
        for row in range(0, size):
            if database["regime change within 5 years"][row] == 0:
                no_regime_change += 1
            elif database["regime change within 5 years"][row] == 1:
                iteration_less_6_years += 1
            elif database["regime change within 5 years"][row] == 2:
                iteration_6_years += 1
        print("Sample size: " + str(size))
        print("\n Number of non-elligible entries: " + str(no_regime_change))
        print("\n Number of non-elligible control group entries: " + str(iteration_6_years))
        print("Proportion of the control group (to the sample size): " + str(iteration_6_years/size))
        print("\n Number of elligible treatment group entries: " + str(iteration_less_6_years))
        print("Proportion of the treatment group (to the sample size): " + str(iteration_less_6_years/size))


if __name__ == "__main__":
    main()

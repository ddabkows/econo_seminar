"""
Author: Dominik Dabkowski
Date:   26th march 2021
Code:   Extracting data for the regime/conflict RDD
"""


import pandas


data = pandas.io.stata.read_stata("../data/workingfile2_onset.dta")

data_to_extract = pandas.DataFrame(zip(data.gid, data.year, data.ConfIntra, data.transition, data.logcapdist))
data_to_extract.to_csv("../data/workingfile2_extracted_data.csv")

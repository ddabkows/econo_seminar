# Author : Dominik Dabkowski
# Date:    21.04.2021
# Code:    RDD according to the behaviour depending on how far was the last
#          regime change


setwd("/home/dominik/Documents/seminar_econo/econo_seminar/")
# Table Reading
EXP_PATH = "img/"
IMP_PATH = "data/"
DAT_PATH = "regime_change_5_years.csv"


dataframe = read.csv(paste(IMP_PATH,
                           DAT_PATH,
                           sep=""),
                     stringsAsFactors=T,
                     sep=",")

control_group = subset(dataframe$conflict, 
                       dataframe$regime.change.within.5.years == 2)
control_group_years = subset(dataframe$year,
                             dataframe$regime.change.within.5.years == 2)

treatment_group = subset(dataframe$conflict,
                         dataframe$regime.change.within.5.years == 1)
treatment_group_years = subset(dataframe$year,
                             dataframe$regime.change.within.5.years == 1)

plot(treatment_group_years, treatment_group,
     type="n")

# Author : Dominik Dabkowski
# Date:    21.04.2021
# Code:    RDD according to the behaviour depending on how far was the last
#          regime change


library(aod)
library(rr2)




setwd("/home/dominik/Documents/seminar_econo/econo_seminar/")
EXP_PATH = "img/"
IMP_PATH = "data/"
DAT_PATH = "regime_change_5_years.csv"


dataframe = read.csv(paste(IMP_PATH,
                           DAT_PATH,
                           sep=""),
                     stringsAsFactors=T,
                     sep=",")

# Control group subset 
control_group = subset(dataframe$conflict, 
                       dataframe$regime.change.within.5.years == 2)
control_group_logdistcap = subset(dataframe$logdistcap,
                             dataframe$regime.change.within.5.years == 2)


control_proportion = length(control_group) / length(dataframe$conflict) * 100

# Treatment group subset
treatment_group = subset(dataframe$conflict,
                         dataframe$regime.change.within.5.years == 1)
treatment_group_logdistcap = subset(dataframe$logdistcap,
                             dataframe$regime.change.within.5.years == 1)

treatment_proportion = length(treatment_group) / length(dataframe$conflict)* 100

# No elligible group subset
noneli_group = subset(dataframe$conflict,
                      dataframe$regime.change.within.5.years == 0 & 
                              dataframe$regime.change == 0)
noneli_group_logdistcap = subset(dataframe$logdistcap,
                            dataframe$regime.change.within.5.years == 0 & 
                                    dataframe$regime.change == 0)

noneli_proportion = length(noneli_group) / length(dataframe$conflict) * 100

treatment_reg = glm(treatment_group ~ treatment_group_logdistcap, 
                    family="binomial")
treatment_pred = predict(treatment_reg)
summary(treatment_reg)

control_reg = glm(control_group ~ control_group_logdistcap, 
                  family="binomial")
control_pred = predict(control_reg)
summary(control_reg)

noneli_reg = glm(noneli_group ~ noneli_group_logdistcap,
                 family="binomial")
noneli_pred = predict(noneli_reg)
summary(noneli_reg)


plot(dataframe$logdistcap, dataframe$conflict)
lmreg = glm(conflict ~ logdistcap, data=dataframe, family="binomial")
summary(lmreg)

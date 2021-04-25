# Author : Dominik Dabkowski
# Date:    21.04.2021
# Code:    RDD according to the behaviour depending on how far was the last
#          regime change


library(plm)
library(aod)
library(bife)
install.packages('bife')
install.packages('RcppArmadillo')


setwd("/home/dominik/Documents/seminar_econo/econo_seminar/")
EXP_PATH = "img/"
IMP_PATH = "data/"
DAT_PATH = "regime_change_5_years.csv"


dataframe = read.csv(paste(IMP_PATH,
                           DAT_PATH,
                           sep=""),
                     stringsAsFactors=T,
                     sep=",")
dataframe = pdata.frame(dataframe, index=c("year"))
regression = conflict ~ logdistcap + loggcppc + logpop + imr +
                        logttime + logcellarea + logdist_LNC + 
                        mountain2000 + ycoord + degtemper + prec

# Control group subset 
control_group = subset(dataframe, 
                       dataframe$regime.change.within.5.years == 2)
control_proportion = length(control_group$conflict) / 
                     length(dataframe$conflict) * 100

# Treatment group subset
treatment_group = subset(dataframe,
                         dataframe$regime.change.within.5.years == 1)
treatment_proportion = length(treatment_group$conflict) / 
                       length(dataframe$conflict)* 100

# No elligible group subset
noneli_group = subset(dataframe,
                      dataframe$regime.change.within.5.years == 0 & 
                              dataframe$regime.change == 0)
noneli_proportion = length(noneli_group$conflict) / 
                    length(dataframe$conflict) * 100


treatment_reg = plm(regression,
                    data = treatment_group,
                    model="within")
treatment_pred = predict(treatment_reg)
summary(treatment_reg)

control_reg = plm(regression,
                  data=control_group,
                  model="within")
control_pred = predict(control_reg)
summary(control_reg)

noneli_reg = plm(regression,
                 data=noneli_group,
                 model="within")
noneli_pred = predict(noneli_reg)
summary(noneli_reg)

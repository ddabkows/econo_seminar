# Author : Dominik Dabkowski
# Date:    21.04.2021
# Code:    RDD according to the behaviour depending on how far was the last
#          regime change


library(plm)
library(aod)
library(bife)


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
regression = ConfIntra ~ logcapdist + logbdist2 + 
             degtemper + prec | year 
trans_regression = ConfIntra ~ transition6 + logcapdist + logbdist2 + 
  degtemper + prec | year 

# Control group subset 
control_group = subset(dataframe, 
                       dataframe$transition6 == 2)
control_proportion = length(control_group$ConfIntra) / 
                     length(dataframe$ConfIntra) * 100
plot(control_group$logcapdist, control_group$ConfIntra)

# Treatment group subset
treatment_group = subset(dataframe,
                         dataframe$transition6 == 1)
treatment_proportion = length(treatment_group$ConfIntra) / 
                       length(dataframe$ConfIntra)* 100
plot(treatment_group$logcapdist, treatment_group$ConfIntra)

# No elligible group subset
noneli_group = subset(dataframe,
                      dataframe$transition6 == 0)
noneli_proportion = length(noneli_group$ConfIntra) / 
                    length(dataframe$ConfIntra) * 100
plot(noneli_group$logcapdist, noneli_group$ConfIntra)


treatment_reg = bife(regression,
                    data = treatment_group,
                    model='logit')
treatment_pred = predict(treatment_reg)
summary(treatment_reg)

control_reg = bife(regression,
                  data=control_group,
                  model="logit")
control_pred = predict(control_reg)
summary(control_reg)

noneli_reg = bife(regression,
                 data=noneli_group,
                 model="logit")
noneli_pred = predict(noneli_reg)
summary(noneli_reg)

trans6_reg = bife(trans_regression, 
                  data = dataframe,
                  model='logit')
trans6_pred = predict(trans6_reg)
summary(trans6_reg)

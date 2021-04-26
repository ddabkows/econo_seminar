# Author : Dominik Dabkowski
# Date:    21.04.2021
# Code:    Regression of the conflict depending on the last regime change


library(plm)
library(aod)
library(bife)


setwd("/home/dominik/Documents/seminar_econo/econo_seminar/")
EXP_PATH = "img/"
IMP_PATH = "data/"
DAT_PATH = "last_transition.csv"


dataframe = read.csv(paste(IMP_PATH,
                           DAT_PATH,
                           sep=""),
                     stringsAsFactors=T,
                     sep=",")

dataframe = pdata.frame(dataframe, index=c("year"))
formula = ConfIntra ~ logcapdist + logbdist2 + degtemper + prec +
             last.transition | year 

regression = 	bife(formula, 
                   data=dataframe,
                   model="logit")		
predictions = predict(regression)
summary(regression)

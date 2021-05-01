# Author : Dominik Dabkowski
# Date:    21.04.2021
# Code:    RDD according to the behaviour depending on how far was the last
#          regime change


library(plm)
library(aod)
library(pglm)
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

# Control group subset 
pre_test_group = subset(dataframe,
                        dataframe$pre_transition == 1)
pre_test_prop  = length(pre_test_group$ConfIntra) /
                 length(dataframe$ConfIntra) * 100

post_test_group = subset(dataframe,
                        dataframe$pre_transition == 0)
post_test_prop  = length(post_test_group$ConfIntra) /
  length(dataframe$ConfIntra) * 100


pre_test_reg = bife(regression,
                    data = pre_test_group,
                    model="logit")
pre_test_pred = predict(pre_test_reg)
summary(pre_test_reg)

post_test_reg = bife(regression,
                     data = post_test_group,
                     model="logit")
post_test_pred = predict(post_test_reg)
summary(post_test_reg)



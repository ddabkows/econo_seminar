Authors:  Bozet Baptiste
	  Dabkowski Dominik
	  Kivrak Selin
	  Petitjean Flavio

This README file contains all the information needed to compute the scripts present in the folder. 

{dist_calc.py} 
This program is a function that calculates the distance between two points on the globe knowing their
lattitudes and longitudes. 
Do not run this script, it will bring no results.

{gdp_dist_calc.py}
This script computes and adds the distances to the cell with the biggest average gdp per capita.

{ore_dist_calc.py}
This script computes and adds the distances to the closest cell with natural resources.

{workingfile_to_csv.py}
This script transforms the dta file workingfile2 to a csv file with only the columns needed for 
the RDD.

{sorter.py}
This script sorts the csv file for the RDD in order to make the next algorithm faster.

{regime_conflict_data.py}
This script is responsible for verifying when occured the last and the next regime transition and to 
verify which one was closer.

{work_sample_checker.py}
Optional script that verifies how many observations remain with values for the RDD.

{RDD_regime_change.r}
File that regresses the RDD.


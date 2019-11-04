
# install.packages("ggplot2")
library(ggplot2)
# install.packages("data.table")
library(timelineR)
require(data.table)


# Getting Cities
setwd("/Users/raiquepereira/Documents/Projects/BeijingAirPollutionPrediction")

Gucheng <- read.csv("/Users/raiquepereira/Documents/Projects/BeijingAirPollutionPrediction/data/raw_data/PRSA_Data_Gucheng_20130301-20170228.csv", stringsAsFactors = FALSE)

Huairou <- read.csv("data/raw_data/PRSA_Data_Huairou_20130301-20170228.csv", stringsAsFactors = FALSE)

Tiantan <- read.csv("data/raw_data/PRSA_Data_Tiantan_20130301-20170228.csv", stringsAsFactors = FALSE)

Changping <- read.csv("data/raw_data/PRSA_Data_Changping_20130301-20170228.csv", stringsAsFactors = FALSE)

Guanyuan <- read.csv("data/raw_data/PRSA_Data_Guanyuan_20130301-20170228.csv", stringsAsFactors = FALSE)

Nongzhanguan <- read.csv("data/raw_data/PRSA_Data_Nongzhanguan_20130301-20170228.csv", stringsAsFactors = FALSE)

Wanliu <- read.csv("data/raw_data/PRSA_Data_Wanliu_20130301-20170228.csv", stringsAsFactors = FALSE)

Dongsi <- read.csv("data/raw_data/PRSA_Data_Dongsi_20130301-20170228.csv", stringsAsFactors = FALSE)

Wanshouxigong <- read.csv("data/raw_data/PRSA_Data_Wanshouxigong_20130301-20170228.csv", stringsAsFactors = FALSE)

Aotizhongxin <- read.csv("data/raw_data/PRSA_Data_Aotizhongxin_20130301-20170228.csv", stringsAsFactors = FALSE)

Dingling <- read.csv("data/raw_data/PRSA_Data_Dingling_20130301-20170228.csv", stringsAsFactors = FALSE)

Shunyi <- read.csv("data/raw_data/PRSA_Data_Shunyi_20130301-20170228.csv", stringsAsFactors = FALSE)

#Dropping Unneeded ID column and merging
Shunyi = subset(Shunyi, select = -c(No) )
Dingling = subset(Dingling, select = -c(No))
Aotizhongxin = subset(Aotizhongxin, select = -c(No))
Wanshouxigong = subset(Wanshouxigong, select = -c(No) )
Wanliu = subset(Wanliu, select = -c(No))
Nongzhanguan = subset(Nongzhanguan, select = -c(No) )
Guanyuan = subset(Guanyuan,  select = -c(No))
Changping = subset(Changping, select = -c(No))
Tiantan = subset(Tiantan, select = -c(No))
Huairou = subset(Huairou, select = -c(No))
Gucheng = subset(Gucheng, select = -c(No))

cities = rbind(Shunyi, Dingling, Aotizhongxin, Wanshouxigong,
               Wanliu, Nongzhanguan, Guanyuan, Changping, Tiantan, Huairou, Gucheng)

# Creating Time Series + Clean Up
#"%Y-%m-%d %H:%M:%OS",
cities$time = paste(cities$year, '-', cities$month, '-', cities$day, ' ', cities$hour)
cities$time = as.POSIXct(cities$time, format= "%Y - %m - %d   %H")
cities = subset(cities, select=-c(year, month, day, hour))

#Setting Columns as Factors to ensure they are categorial
cities$station <- as.factor(cities$station)
cities$wd <- as.factor(cities$wd)


# Pollutants are: SO2, NO2, CO, O3
plot_grob <- plot_timeline(cities)





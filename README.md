# Beijing Air Pollution Prediction

While Beijing is a massive city, which section of the city is the most populated city with 21.54 million residents and 6490 square miles compared to Boston of a mere 90 square miles. However, Beijing has longed struggles with air pollution. We would build a predictive model that uses prior air quality data in different areas in Beijing so that the city would know which area is most affected to its citizens. Our goal is to build models to forecast each pollutant in our dataset.

Source of Data: Beijing Multi Site Air Quality Data							   Link -  http://archive.ics.uci.edu/ml/datasets/Beijing+Multi-Site+Air-Quality+Data

Data Selection: 
We’ll be importing 12 datasets corresponding to the sites on which air quality were measured hourly from March 2013 to February 2017. The data includes 16 attributes such as :
No: row number						        year: year of data in this row
month: month of data in this row					day: day of data in this row
hour: hour of data in this row			    PM2.5: PM2.5 concentration (ug/m^3)
PM10: PM10 concentration (ug/m^3)		          SO2: SO2 concentration (ug/m^3)
NO2: NO2 concentration (ug/m^3)                		   CO: CO concentration (ug/m^3)	O3: O3 concentration (ug/m^3)			     TEMP: temperature (degree Celsius)
PRES: pressure (hPa)		          DEWP: dew point temperature (degree Celsius)
RAIN: precipitation (mm)					      		   wd: wind direction
WSPM: wind speed (m/s)			  station: name of the air-quality monitoring site

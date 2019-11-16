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


### Goal 

Are ultimate goal is forecast the Six pollutants provided to us - PM2.5, PM10, 
NO2, SO2, CO, and O3. 

### Approach:

We noticed that SO2, CO, and O3 forecasting was possible since the data
suggested a trend. For NO2 and PM, this was not present and it seemed 
independent of time. So at a high-level we implemented the following algorithm:

<pre>
1. Combine all the Cities and Create two K-NN models for NO2 and PM. 
2. Take advantage that SO2, CO, and O3 are a time series and create a 
recurrent neural network of each. 
3. Retrieve Predicted SO2, CO, O3. 
4. Use Predicted values as inputs into K-NN to predict NO2 and PM.
</pre>

### Other Ideas:
1. Use LSTM RNN for multivariate predictions.
2. Use K-Means to cluster data, save to an index,
and Run approximate nearest neighbors: 
    - K-NN scalablity issue: Too many dimensions that cannot be reduced.
    - K-NN scalability to many data points.
    
### TODO
- Build Following Models:
    - RNN CO
    - RNN O3
    - Build PM2.5
- Resolve K-NN scalability issue.
- Changing frequency from hourly to daily, weekly, etc. and observing 
if trend exists. 
- Building a visualization map using google-maps-api
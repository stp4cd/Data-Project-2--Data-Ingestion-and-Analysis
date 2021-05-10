# Data Project 2: Data Ingestion and Analysis

The goal of this project is to write and deploy a process that retrieves data from a remote API (https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi), writes the values to a database every minute for 60 minutes, and finds trends and patterns between the various values retrieved. 

To do this, I created a python file that calls the given API and fetches the data values every minute. In addition, this file connects to a MongoDB database session and creates a new collection to which the data values are inserted. After compiling the values of the various data fields, the documents are retrieved from the collection and converted into a dataframe so that easy analysis can be conducted to better understand the patterns and trends found between the data fields. To conduct this analysis, three plots are created (factor and pi, pi and time, and factor and time) to visualize trends. 

The first plot that is produced plots how the pi value changes based on the factor value. By looking at the plot produced (output1.png can be found amongst the files) one can easily see that as factor increases, the pi value converges to a value of approximately 3.14. This is because ____. 




everyminute1.png
everyminute2.png 



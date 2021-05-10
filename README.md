# Data Project 2: Data Ingestion and Analysis

The goal of this project is to write and deploy a process that retrieves data from a remote API (https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi), writes the values to a database every minute for 60 minutes, and finds trends and patterns between the various values retrieved. 

To do this, I created a python file that calls the given API and fetches the data values every minute. In addition, this file connects to a MongoDB database session and creates a new collection to which the data values are inserted. After compiling the values of the various data fields, the documents are retrieved from the collection and converted into a pandas dataframe so that easy analysis can be conducted to better understand the patterns and trends found between the data fields. To conduct this analysis, three plots are created (factor vs. pi, pi vs. time, and factor vs. time) to visualize trends. 

The first plot that is produced plots how the pi value changes based on the factor value. By looking at the plot produced (output1.png can be found amongst the files) one can easily see that as factor increases, the pi value converges from around 4 to a value of approximately 3.14. The factor value seems to increase exponentially so it is plotted on a log scale. 

The second plot (output2.png) produced is a scatter plot that indicates how the factor value changes over time. The value seems to be repetitive in nature where after it reaches a certain value, it drops down to it's initial value and starts increasing exponentially again. Lastly, the third plot reemphasizes the converging nature of the pi value by plotting the pi value against time. We see a very similar pattern to the first plot, and we can also see that when the factor value hits its final value and drops to its initial to start over, this is reflected in the pi value over time. When the factor value drops, we see the pi value stray greatly (goes back to around 4) from the value it converges to (~3.14). 


# Files

1. proj2b.py : This file contains the python script. Please see comments within the file for a better understanding of the steps taken to execute the process.
2. project2_textoutput.txt : Alongside the data fields being fetched from the API every minute, a print statement is used to check the progress over the hour. This text file are of the printed data values, and the time data field indicates that the process occurs every minute exactly for 60 minutes. The MongoDB collection is also printed within this text file. Note that the values within this text file may not line up exactly with the graphic outputs as they were pulled from separate runs. 
3. output1.png : When running the python file, this is one of the figures that is printed. It is the scatterplot that visualizes the relationship between the data fields factor and pi. 
4. output2.png : When running the python file, this is one of the figures that is printed. It is the scatterplot that visualizes the relationship between the data fields factor and time. 
5. output3.png : When running the python file, this is one of the figures that is printed. It is the scatterplot that visualizes the relationship between the data fields pi and time. 
 




import threading
import datetime
import requests
import time
from pymongo import MongoClient
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt

# Choose the appropriate client
client = MongoClient()

# Connect to the test db 
db=client.test

#if pival collection already exists, remove it
db.pival.drop()

# create a new collection "pival"
pival = db.pival

# the following function performs operations repeatedly every "interval" seconds
# while making use of thread timers
def do_every (interval, worker_func, iterations = 0):
  #print('iterations = ', iterations)
  if iterations != 1:
    thr = threading.Timer (
      interval,
      do_every, [interval, worker_func, 0 if iterations == 0 else iterations-1]
    )
    thr.start()	
  worker_func()

def my_func ():
    #print("I am executed at {}".format(datetime.datetime.now()))
    response = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi")
    print(response.text)
	# insert into MogoDB database collection
    result = pival.insert_one(response.json())
	
def main():
    # call my_func periodically
    between_interval = 60 # interval set to 60 sec
    total_iterations = 60  # iterate 60 times
    do_every(between_interval, my_func, total_iterations)
	
	# sleep until all the periodic calls are completed
    time.sleep(between_interval*total_iterations)

	# print the MongoDB contents
    print("\nMongoDB Collection contents are shown below:\n")
    ret = pival.find({})
    for document in ret:
        pprint(document)
	
	# put the contents in the Pandas dataframe for analysis
    cursor = pival.find()
    entries = list(cursor)
    df = pd.DataFrame(entries)
    #print("\nPandas DataFrame contents are:")
    #print(df.head(total_iterations))
	
	#plot factor vs pi while using logarithmic scale for factor
    df.plot(x='factor', y='pi', style='.', logx=True)
    #df.plot(x='factor', y='pi', logx=True)
    plt.savefig('output1.png')
    
    #plot factor against time
    df.plot(x='time', y='factor',style='.')
    plt.savefig('output2.png')
    
    #plot pi against time 
    df.plot(x='time',y='pi',style='.')
    plt.savefig('output3.png')

if __name__ == '__main__':
    main()
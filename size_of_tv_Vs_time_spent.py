import plotly.express as px
import csv
import numpy as np

#this is the function definition to create a scatter plot graph for the given data set
def plotFigure(data_path):
    #opens the file to access what is in it
    with open(data_path) as csv_file:
        #using csv.Dicreader to read the data frame of the file
        df = csv.DictReader(csv_file)
        #we use fig as the variable & create a scatter grapph on the given data for the x & y
        fig = px.scatter(df,x="Size of TV", y="\tAverage time spent watching TV in a week (hours)")
        #display the graph
        fig.show()

#function definiton to extract the information of size of tv & average time spent as seperate list from the given data file
def getDataSource(data_path):
    size_of_tv = []
    Average_time_spent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            Average_time_spent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return {"x" : size_of_tv, "y": Average_time_spent}

#function definition to get the correlation & print it with a message & showing the result
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Size of Tv and Average time spent watching Tv in a week :-  \n--->",correlation[0,1])
    
#function defenition to execute a set of functions
def setup():
    #setting the data path so that we can connect it to the file
    data_path  = "./data/size_of_tv_Vs_time_spent.csv"
    #setting the value of data source by calling getDataSource
    #function call to extract the information of size of tv & average time spent as seperate list from the given data file
    datasource = getDataSource(data_path)
    #function call to get the correlation & print it with a message & showing the result
    findCorrelation(datasource)
    #function call to create a scatter plot graph for the given data set
    plotFigure(data_path)
    
#function call to execute the set of functions
setup()


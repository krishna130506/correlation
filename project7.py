import numpy as np
import plotly_express as px
import csv
import pandas as pd

def getDataSource(data_path):
    Coffee = []
    Sleep = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee.append(float(row["Coffee"]))
            Sleep.append(float(row["sleep"]))

    return{"x":Coffee,"y":Sleep}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])      
    print("correlation between coffee(in ml) and sleep(in hours):",correlation[0,1])

def plotFigure(data_path):
    with open(data_path)as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x = "Coffee",y = "sleep")
        fig.show()

def setup():
    data_path = "coffee.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()
        


         
import csv
import sys
import pandas as pd

def check_name(name):
    #read csv, and split on "," the line
    df = pd.read_csv('values.csv')
    row_list = df[df["Name"]==name].values.flatten().tolist()
    points = 0
    if row_list:
        points = row_list[1]
    
    return points

def write_csv(name, value):
    df = pd.read_csv('values.csv')
    if(len(df[df["Name"]==name])>0):
        df.loc[df['Name'] == name, 'Value'] = value
    else:
        df.loc[len(df.index)] = [name, value] 

    df.to_csv('values.csv', index=False)

'''
Here we have taken some  of the parameters for now. These parameters will be taken by the user via GUI in future.
These parameters are:
    ->  delimited file path
    ->  delimiter
    ->  desired file name
    ->  destination path of the file
'''
import pandas as pd
import openpyxl
import transform_path

delimiter = ';'
original_path = "D:/Required_Data/TessyFunctionReport.csv"
destination_filePath ="D:/Required_Data/TessyFunctionReport.xlsx"
def toexcel(delimiter, original_path,destination_filePath):
    data = pd.read_csv(original_path, sep= delimiter)
    data.to_excel(destination_filePath, index= False, header= True)
#toexcel(delimiter, original_path, destination_filePath)
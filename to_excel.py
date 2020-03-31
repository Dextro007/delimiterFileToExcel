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

delimiter = ';'
original_path = "D:/Required_Data/TessyResult.csv"
destination_filePath = r"D:\Required_Data\TessyResults.xlsx"
data = pd.read_csv(original_path, sep= delimiter)
data.to_excel(destination_filePath, index= False, header= True)

import xlrd
import pandas as pd

#path = r"D:\Tessy Reports\FCA_332_BEV\NVM_1.30"
#print(path.replace('\\', '/'))

def transformPath(path_str):
    path = list(path_str)
    for i in range(0, len(path)):
        if(path[i] == '\\'):
            path[i] = '/'
    path_str = "".join(path)
    return path_str
def takePath():
    s = input("Enter the string :  ")
    path = r"{}".format(s)
    transformPath(path)

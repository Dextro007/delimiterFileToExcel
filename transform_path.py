import xlrd
import pandas as pd

#path = r"D:\Tessy Reports\FCA_332_BEV\NVM_1.30"
#print(path.replace('\\', '/'))

def transformPath(s):
    path = r"{}".format(s)
    path = list(path)
    for i in range(0, len(path)):
        if(path[i] == '\\'):
            path[i] = '/'
    path_str = "".join(path)
    return path_str

 

import numpy as np
import pandas as pd
import os

cwd = os.getcwd()
parent =  os.path.abspath(os.path.join(cwd,os.pardir))

df= pd.read_table(parent+"/output/latex.txt",delimiter=" ",header=None,skiprows=0,skipinitialspace=True)
df.to_excel(parent+"/output/latex.xlsx")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as mplcm
import matplotlib.colors as colors
import os
import models

cwd = os.getcwd()
parent =  os.path.abspath(os.path.join(cwd,os.pardir))

plt.rcParams.update({'font.size': 13})
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

df_data = pd.read_table(parent+"/data/covid.txt",delimiter=" ",header=None,skiprows=0,skipinitialspace=True)
df_data = pd.read_table(parent+"/data/covid.txt",delimiter=" ",header=None,skiprows=0,skipinitialspace=True)
df_sol = pd.read_table(parent+"/output/solution_covid.txt",delimiter=" ",header=None,skiprows=0,skipinitialspace=True)

n_train = int(df_data[0].values[0])
n_test = int(df_data[0].values[1])

y = df_data[0].values[2:len(df_data)]

days = [i for i in range(1,n_train+n_test+1)]
x = df_sol[:].values[0]

t = np.linspace(days[0],days[-1],1000)

with open(parent+"/output/outliers.txt") as f:
    lines = f.readlines()
    xdata = [line.split()[0] for line in lines]

noutliers = int(xdata[0])
outliers = np.empty(noutliers,dtype=int)
cubic_outliers = np.empty((2,noutliers))

for i in range(noutliers):
    outliers[i] = int(xdata[i+1])

for i in range(noutliers):
    cubic_outliers[0,i] = days[outliers[i]-1]
    cubic_outliers[1,i] = df_data.values[outliers[i]+1]


plt.plot(t,models.cubic(x[0],x[1],x[2],t,y[len(y)-n_test-1],days[len(y)-n_test-1]),lw=2)

plt.plot(cubic_outliers[0],cubic_outliers[1],'ro',mfc='none',ms=10)

l1 = plt.plot(days[:n_train],y[:n_train],"ok")
plt.setp(l1, 'markersize')

l2 = plt.plot(days[n_train:],y[n_train:],"ok",mfc='none',ms=6,marker="s")
plt.setp(l2, 'markersize')

# plt.xticks(range(-1, 4, 1))
# plt.yticks(range(-4, 5, 2))
# plt.show()

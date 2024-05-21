import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

cwd = os.getcwd()
parent =  os.path.abspath(os.path.join(cwd,os.pardir))

plt.rcParams['figure.figsize'] = 0.6 * [6.4, 4.8]
plt.rc('text', usetex=True)

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 11,
        }

countries = {
    "ar" : "ar.xlsx",
    "br" : "br.xlsx",
    "co" : "co.xlsx",
    "es" : "es.xlsx",
    "it" : "it.xlsx",
    "pa" : "pa.xlsx",
    "uk" : "uk.xlsx",
    "us" : "us.xlsx"
}

country = countries["it"]

# ind_excel = 475
ind_excel = 218

df = pd.read_excel(parent+"/data/"+country)

initial_date = ind_excel - 2
n_train = 27
n_test = 3
total_days = n_train + n_test  
data = np.zeros(n_train)

with open(parent+"/data/covid.txt","w") as f:
    f.write("%i\n" % n_train)
    f.write("%i\n" % n_test)
    j = 0

    for i in range(initial_date,initial_date + total_days):
        x = df["new_deaths_smoothed_per_million"][i]

        if pd.isna(x) == True:
            f.write("%f\n" % 0.0)
        else:
            f.write("%f\n" % x)

        if j <= n_train - 1:
            data[j] = x
    
        j += 1


plt.plot(np.linspace(1,n_train,n_train),data,":o",color="darkgreen")
plt.xlabel("Days",fontdict=font)
plt.ylabel("Deaths per million",fontdict=font)
plt.savefig(parent+"/images/image.pdf",bbox_inches="tight")
# plt.show()

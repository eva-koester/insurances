#Projekt: Scatterplot mit Beschwerden und Versicherten (um Korrelation zu erkennen)

import pandas as pd
import matplotlib.pyplot as plt
df_beschwerden = pd.read_csv('beschwerden_all.csv')
print(df_beschwerden)

#zwei Listen x uns y aus den Columns "Versichterte" (x) und "Beschwerden" (y):
x = list(df_beschwerden['Versicherte'])
y = list(df_beschwerden['Beschwerden'])
print(x)
print(y)
assert len(x) == len(y)

#Scatterplot (x auf x-Achse, y aauf y-Achse)
r_besch_vers = plt.scatter(x,y)
plt.show()
#plt.close()

#df_beschwerden.plot.scatter(x = 'Versicherte', y = 'Beschwerden', c = 'Name')
#plt.show()
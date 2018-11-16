#Projekt: Plot mit Scatterplot mit Beschwerden und Versicherten (um Korrelation zu erkennen)

import pandas as pd
import matplotlib.pyplot as plt
df_beschwerden = pd.read_csv('beschwerden_all.csv')
print(df_beschwerden)
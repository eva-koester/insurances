# Project: create a scatterplot of "Versicherte" and "Beschwerden"
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# preparation //I used the pd.read function
df = pd.read_csv('beschwerden_all.csv')
#print(df)

# remove duplicates of year 2007 from the dataframe: create a new df that only includes year 2007, drop the duplicates,
# remove all entries with year 2007 from the normal df, coerce the two df's
df_year_2007 = df[df['Jahr'] == 2007]
df_year_2007 = df_year_2007.drop_duplicates("Nummer", keep="first")
df = df[df['Jahr'] != 2007]
df = pd.concat([df, df_year_2007])
print(len(df))
# scatterplot: relationship between "Versicherte" and "Beschwerden"
# sns.set()
sns.relplot(x='Versicherte', y='Beschwerden', hue="Name", data=df)
#plt.show()
plt.close()
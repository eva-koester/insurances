# Project: How does sum of complaints develop, how does sum of insured persons develop? //absolute and relative
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('beschwerden_all.csv')
sns.set(context="talk", style="ticks")
#sns.set_style("dark")

# remove duplicates of year 2007 from the dataframe: create a new df that only includes year 2007, drop the duplicates,
# remove all entries with year 2007 from the normal df, coerce the two df's
df_year_2007 = df[df['Jahr'] == 2007]
df_year_2007 = df_year_2007.drop_duplicates("Nummer", keep="first")
df = df[df['Jahr'] != 2007]
df = pd.concat([df, df_year_2007])

# plot the sum of complaints and insured persons from 2002 to 2017 (not considered: no. of insurances)
# change new index "Jahr" into according column
df_sum = df.groupby('Jahr').agg('sum')
df_sum['Jahr'] = df_sum.index
print(df_sum)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax2.set_ylabel('exp', color='red')
ax2.tick_params('y', colors='red')
f=sns.lineplot(x='Jahr', y='Versicherte', data=df_sum, ax=ax1)
g=sns.lineplot(x='Jahr', y='Beschwerden', data=df_sum, ax=ax2, color='red')
sns.despine(right=False)
#plt.xticks(rotation=45)
#g.set_xticklabels(rotation=30)
#g.set_xticklabels([2008, 2009, 2010], rotation=30)
#print(g.get_xticklabels())
#print(f.get_xticklabels())
#plt.tight_layout()
plt.show()

# Project: How does sum of complaints develop, how does sum of insured persons develop? //absolute and relative
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cleaning

df = cleaning.load_clean_data()
sns.set(context="talk", style="ticks")
#sns.set_style("dark")

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

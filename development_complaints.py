# Project: How does sum of complaints develop, how does sum of insured persons develop? //absolute and relative
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cleaning

df = cleaning.load_clean_data()
sns.set(style="ticks", rc={'font.family':'sans-serif','font.sans-serif': ['Cambria'],'axes.labelsize':18,'axes.titlesize':20})
#sns.set_style("dark")

# adjust the scaling of insured persons
df_sum = df.groupby('Jahr').agg('sum')
df_sum['Jahr'] = df_sum.index
print(df_sum)
df_sum['Versicherte'] = df_sum['Versicherte']/1000000

# plot the sum of complaints and insured persons from 2002 to 2017 (not considered: no. of insurances)
# change new index "Jahr" into according column
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

f=sns.lineplot(x='Jahr', y='Versicherte', data=df_sum, ax=ax1, color='darkgreen')
g=sns.lineplot(x='Jahr', y='Beschwerden', data=df_sum, ax=ax2, color='crimson')
sns.despine(right=False)
ax1.set_ylabel('Insured Persons (Mio)', color='darkgreen')
ax2.set_ylabel('Complaints', color='crimson')
ax1.tick_params('y', colors='darkgreen')
ax2.tick_params('y', colors='crimson')
#sns.axes_style(axes.facecolor='darkgreen')
#plt.xticks(rotation=45)
#g.set_xticklabels(rotation=30)
#g.set_xticklabels([2008, 2009, 2010], rotation=30)
#print(g.get_xticklabels())
#print(f.get_xticklabels())
plt.tight_layout()
plt.show()

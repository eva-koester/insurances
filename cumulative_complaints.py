# Project: scatterplot with average complaints and average insured persons, controlled for number of years
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('beschwerden_all.csv')
sns.set(style='dark', rc={'font.family':'sans-serif','font.sans-serif': ['Cambria'],'axes.labelsize':18,'axes.titlesize':20})

# data cleaning:
# remove duplicates of year 2007 from the dataframe: create a new df that only includes year 2007, drop the duplicate
# remove all entries with year 2007 from the normal df, coerce the two df's
# make sure that all insurances with the same number have the same name
df_year_2007 = df[df['Jahr'] == 2007]
df_year_2007 = df_year_2007.drop_duplicates("Nummer", keep="first")
df = df[df['Jahr'] != 2007]
df = pd.concat([df, df_year_2007])
grouped = df.groupby('Nummer')
for nummer, group in grouped:
    name = group['Name'].iloc[0]
    df.loc[df['Nummer'] == nummer, 'Name'] = name

# add number of years as a new column and assign value 1 to it, then summarize complaints, insured persons
# and number of years per insurance
df['no_years'] = 1
df = df.groupby('Name').agg('sum')
df['Name'] = df.index

# calculate the relative number of insured persons and complaints
df['rel_Versicherte'] = df['Versicherte'] / df['no_years']
df['rel_Beschwerden'] = df['Beschwerden']/df['no_years']

# calculate the correlation between relative number of insured persons and relative number of complaints
rel_insured = list(df['rel_Versicherte'])
rel_complaints = list(df['rel_Beschwerden'])
print(rel_insured)
print(rel_complaints)
correlation = np.corrcoef(rel_insured, rel_complaints)
print(correlation)

# adjust the scaling for rel_Versicherte
df['rel_Versicherte'] = df['rel_Versicherte']/1000000

# find out how many steps the variable "no_years" contains
minimum = 10000
range_no_years = []
for entry in df['no_years']:
    if entry in range_no_years:
        pass
    else:
        range_no_years.append(entry)
print(range_no_years)
# the range from 1 to 15 seems ok. It reflects the range from 2002 to 2017.

# scatterplot: complaints vs. insured persons (dot size reflects the number of years)
cmap = sns.cubehelix_palette(8, start=.5, rot=-.75, as_cmap=True)
g = sns.scatterplot(x='rel_Beschwerden', y='rel_Versicherte', size='no_years', hue='no_years', sizes=(100, 400),
                    legend = 'full', data=df, palette=cmap, alpha=0.8)
g.set(xlabel='Beschwerden', ylabel='Versicherte (Mio)', title='Zusammenhang zwischen Beschwerden und Anzahl Versicherter')

for index, row in df.iterrows():
    if row['Name'] in ['AXA KRANKEN', 'HANSEMERKUR S.KRANKEN', 'DEBEKA KRANKEN', 'SIGNAL KRANKEN', 'CENTRAL KRANKEN',
                'ALLIANZ PRIV.KV AG', 'DT. KRANKENVERS.']:
        print(row['Name'])
        if row['rel_Beschwerden'] >= 150:
            alignment='right'
        else:
            alignment='left'
        g.text(row['rel_Beschwerden'], row['rel_Versicherte']+0.125, row['Name'],
               horizontalalignment=alignment, verticalalignment='baseline', size='medium', color='black', weight='semibold')
g.set_xticks(range(0, 250, 25))
g.set_yticks(np.linspace(0,4,17))
plt.text(-10, -0.75, r'Notes: x=average number complaints, y=average number of insured persons, r = .66')
plt.tight_layout()
plt.show()
# Project: plot the market share of the insurances in 2002 and 2017
# Output: two bargraphs (2002, 2017)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('beschwerden_all.csv')
sns.set(style='darkgrid', rc={'font.family':'sans-serif','font.sans-serif': ['Cambria'],'axes.labelsize':18,'axes.titlesize':20})
print(df)

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

# extract dataframe limited to year 2002, order it in descending order of number of insured persons,
# store this new ordering in new column
df_2002 = df[df['Jahr'] == 2002]
df_2002 = df_2002.sort_values("Versicherte", ascending=False)
df_2002['order_insured'] = df_2002.groupby('Jahr').cumcount()
print(df_2002)


# plot the market share in 2002 in descending order
#df_2002 = df[df['Jahr'] == 2002]
#df_2002 = df_2002.sort_values("Versicherte", ascending=False)
g = sns.barplot(x="Versicherte", y="Name", data=df_2002)
g.set(xlabel='Insured Persons', ylabel='Insurance Name', title='Market Share in 2002')
#plt.title('market share in 2002')
#plt.show()
#plt.close()
#print("We've got data from " + str(len(df_2002)) + " insurances in 2002.")

# plot market share in 2017 in the same order as market share in 2002
df_2017 = df[df['Jahr'] == 2017]

#df_full=merge(df_2002, df_2017, by = intersect("Name"))

#df_2017 = df_2017.sort_values("Versicherte", ascending=False)
#s#ns.barplot(x="Versicherte", y="Name", data=df_2017)
#plt.title('market share in 2017')



# plot market share in 2017 in descending order
#df_2017 = df[df['Jahr'] == 2017]
#df_2017 = df_2017.sort_values("Versicherte", ascending=False)
#sns.barplot(x="Versicherte", y="Name", data=df_2017)
#plt.title('market share in 2017')
#plt.show()
#plt.close()
#print("We've got data from " + str(len(df_2017)) + " insurances in 2017.")





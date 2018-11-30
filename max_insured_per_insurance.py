# Projekt: barplot with one bar per insurance, showing the max number of insured persons (regardless of the year)
import cleaning
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = cleaning.load_clean_data()
sns.set(style='darkgrid', rc={'font.family':'sans-serif','font.sans-serif': ['Cambria'],'axes.labelsize':18,
                              'axes.titlesize':20})

# extract max insured persons for each insurance
df = df.groupby('Name')
df = df.Versicherte.max()

# drop the rows with NaN, change the pandas series back into a dataframe again and make sure that the index 'Name' is
# also a column
df = df.dropna(how='any')
df = pd.DataFrame(df,columns = ['Versicherte'])
df['Name'] = df.index

# adjust scaling (insured persons in Mio)
df['Versicherte'] = df['Versicherte']/1000000

# plot the max number of insured persons in a barplot, descending order
df = df.sort_values("Versicherte", ascending=False)
g = sns.barplot(x="Versicherte", y="Name", data=df)
g.set(xlabel='Insured Persons (Mio)', ylabel='Insurance Name')
plt.title('Record Year: Max Number of Insured Persons Per Insurance')
plt.show()

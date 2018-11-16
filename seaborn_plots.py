import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# preparation //I used the pd.read function (the other tips = sns.load_dataset("tips") did not work)
df = pd.read_csv('beschwerden_all.csv')
print(df)

# remove duplicates from the dataframe (some entries in "Jahr" are the same)

#sns.set()
sns.relplot(x='Versicherte', y='Beschwerden', hue="Name", data=df)
plt.show()
#plt.close()

# plot market share in 2002:
df_2002 = df[df['Jahr'] == 2002]
#print(df_2002)

# Print how many datapoints we have in 2002
#print(len(df_2002))
print("We've got data from " + str(len(df_2002)) + " insurances in 2002.")

# bargraph: that shows market share in 2002 in descending order
sorted_versicherte_2002 = df_2002.sort_values("Versicherte", ascending=False)
#print(sorted_versicherte_2002)
sns.barplot(x="Versicherte", y="Name", data=sorted_versicherte_2002)
plt.title('market share in 2002')
plt.show()
#plt.close()

# plot market share in 2017:
df_2017 = df[df['Jahr'] == 2017]
print(df_2017)
print("We've got data from " + str(len(df_2017)) + " insurances in 2017.")

# bargraph: that shows market share in 2017 in descending order
sorted_versicherte_2017 = df_2017.sort_values("Versicherte", ascending=False)
sns.barplot(x="Versicherte", y="Name", data=sorted_versicherte_2017)
plt.title('market share in 2017')
plt.show()
#plt.close()

# Wie entwickeln sich die Gesamtzahl der Beschwerden und die Gesamtzahl der Versicherten über die Zeit?
# Hansemerkur S. KRANKEN (number 4122)
df_hansem = df[df['Nummer'] == 4122]
print(df_hansem)

# in 2007, hansemerkur seems to have many duplicates. Drop them:
df_hansem = df_hansem.drop_duplicates("Jahr",keep="first")
print(df_hansem)

# lineplot
sns.scatterplot(x="Jahr", y="Versicherte", data=df_hansem)
plt.show()
#plt.close()

# checking whether number 4001 also has duplicates in 2007 --> it does
df_4001 = df[df['Nummer'] == 4001]
print(df_4001)

# df with all values for Jahr 2007
df_Jahr_2007 = df[df['Jahr'] == 2007]
print(df_Jahr_2007)
print(len(df_Jahr_2007))

# drop duplicates
df_Jahr_2007= df_Jahr_2007.drop_duplicates("Nummer",keep="first")
print(df_Jahr_2007)
print(len(df_Jahr_2007))

# remove entries with Jahr 2007 from normal df
print(len(df))
df = df[df['Jahr'] != 2007]
print(len(df))

# summarize, it's right.
df = pd.concat([df, df_Jahr_2007])
print(len(df))
print(df)

# check whether Jahr 2006 has duplicates as well
df_Jahr_2006 = df[df['Jahr'] == 2006]
df_Jahr_2006 = df_Jahr_2006.sort_values('Nummer')
#print(df_Jahr_2006)

# # check whether Jahr 2008 has duplicates as well
df_Jahr_2008 = df[df['Jahr'] == 2008]
df_Jahr_2008 = df_Jahr_2008.sort_values('Nummer')
#print(df_Jahr_2008)

# check whether Jahr 2009 has duplicates as well
df_Jahr_2009 = df[df['Jahr'] == 2009]
df_Jahr_2009 = df_Jahr_2009.sort_values('Nummer')
#print(df_Jahr_2009)

#print(len(df['Jahr']==2007))
#print(len(df['Jahr']== 2008))
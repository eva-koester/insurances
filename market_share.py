# Project: plot the market share of insurances that existed in 2002, both in 2002 and 2017
# Output: two bargraphs (2002, 2017)

import matplotlib.pyplot as plt
import seaborn as sns
import cleaning

df = cleaning.load_clean_data()
sns.set(style='darkgrid', rc={'font.family':'sans-serif','font.sans-serif': ['Cambria'],'axes.labelsize':18,'axes.titlesize':20})

# extract a copy of the dataframe limited to year 2002, order it in descending order of number of insured persons,
# store this new ordering in a new column
# use .copy, because: to prevent chaining indexing (copy means that the slice of df will be unique df)
df_2002 = df[df['Jahr'] == 2002].copy()
df_2002 = df_2002.sort_values("Versicherte", ascending=False)
df_2002['order'] = df_2002.groupby('Jahr').cumcount()
#print(df_2002)

# extract a copy of a dataframe limited to year 2017
df_2017 = df[df['Jahr'] == 2017].copy()

# compare column "Nummer" of df_2002 and df_2017 with each other, if equal: entry in "order" of df 2002 into
# "order" of df_2017 (which I previously created):
df_2017['order'] = 100
for entry in df_2017['Nummer']:
    #print('Working on entry', entry)
    #print(" - current order in 2017:", df_2017.loc[df_2017["Nummer"] == entry, 'order'].iloc[0])
    if entry in df_2002['Nummer'].values:
        #print(" - entry", entry, "is in 2002!")
        var = df_2002.loc[df_2002['Nummer']== entry, 'order']
        #print('var', var)
        old_order = var.iloc[0]
        #print(" - in 2002, entry", entry, "had order #", old_order)
        df_2017.loc[df_2017['Nummer']== entry, 'order'] = old_order
        #print(" - added old order", old_order, "to 2017:", df_2017.loc[df_2017["Nummer"]==entry, 'order'].iloc[0])
    #else:
        #print(" - entry", entry, "is not in 2002!")

## iterate through df_2002: if entry in "order" not in df_2017, add a new row to df_2017 with insurance and complaint set
# to 0
for index, row in df_2002.iterrows():
    if row["Nummer"] in df_2017["Nummer"].values:
        pass
    else:
        #print('snabb')
        row["Versicherte"] = 0
        row["Beschwerden"] = 0
        if row["Nummer"] in df_2002 != 4018:
            df_2017 = df_2017.append(row, ignore_index=True)

# change order number of Hansemerkur (replace order number for it in 2017 by order number 2017)
# number of Hansemerkur in 2002: 4018, order_number: 15
# number of Hansemerkur in 2017: 4144
old_order_number = df_2002.loc[df_2002["Nummer"] == 4018, "order"]

#remove index from this number (otherwise, there will be NaN when you try to replace it)
new_order_number = old_order_number.iloc[0]
print(new_order_number)
df_2017.loc[df_2017["Nummer"] == 4144, "order"] = new_order_number

# order the entries in df_2017 according to 'order'
df_2017 = df_2017.sort_values('order')
print(df_2017)
# if order = 100: this insurance did not exist in 2002, but it existed in 2017

# adjust the scaling of both dataframes (insured persons in Mio)
df_2002["Versicherte"] = df_2002["Versicherte"]/1000000
df_2017["Versicherte"] = df_2017["Versicherte"]/1000000

# plot the market share in 2002 in descending order
#df_2002 = df[df['Jahr'] == 2002]
#df_2002 = df_2002.sort_values("Versicherte", ascending=False)
g = sns.barplot(x="Versicherte", y="Name", data=df_2002)
g.set(xlabel='Insured Persons (Mio)', ylabel='Insurance Name')
plt.title('Market Share in 2002')
plt.show()
#plt.close()
#print("We've got data from " + str(len(df_2002)) + " insurances in 2002.")

# plot market share in 2017 in the same order as market share in 2002
f = sns.barplot(x="Versicherte", y="Name", data=df_2017)
g.set(xlabel='Insured Persons (Mio)', ylabel='Insurance Name')
plt.title('Market Share in 2017')
plt.show()
#plt.close()

#df_full=merge(df_2002, df_2017, by = intersect("Name"))



#print("We've got data from " + str(len(df_2017)) + " insurances in 2017.")


## Probleme:
# for entry, row in df_2017.iterrows():
#   print(row['Nummer'])
#  #print(entry)
#  for number in df_2017['Nummer']:
#     if number in df_2002['Nummer']:
#        print('schnabbel')

# for entry, row in df_2017.iterrows():
# if row['Nummer']
#  if df_2017['Nummer'] == 4034 in df_2002['Nummer']:
#   print('babbel')
# if df_2017.loc[entry, 'Nummer'] in df_2002['Nummer']:
# print('schnabbel')

## das habe ich versucht:
#for entry in df_2017['Nummer']:
 #   if entry in df_2002['Nummer']:
  #      df_2017['order'] = df_2002['order']
#print(df_2017['order'])
       # df_2017['order'] == df_2002['order']
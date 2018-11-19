# Project: clean the dataset: only one name for each number, drop year-duplicates (2007)
import pandas as pd
df = pd.read_csv('beschwerden_all.csv')
print(len(df))

# remove duplicates of year 2007 from the dataframe: create a new df that only includes year 2007, drop the duplicates,
# remove all entries with year 2007 from the normal df, coerce the two df's
df_year_2007 = df[df['Jahr'] == 2007]
df_year_2007 = df_year_2007.drop_duplicates("Nummer", keep="first")
df = df[df['Jahr'] != 2007]
df = pd.concat([df, df_year_2007])
print(len(df))

# Krankenkassen mit derselben Nummer haben denselben Namen
grouped = df.groupby('Nummer') ##--> Nummer wird zu name
for nummer, group in grouped:
    name = group['Name'].iloc[0]
    #print(nummer, name)
    #print(group)
    df.loc[df['Nummer'] == nummer, 'Name'] = name

#print(df)
print(df.sort_values('Nummer'))


#print(df)

#for name, group in grouped:
 #   if name == 4001:
        #entry = grouped['Name']
        #print(entry)
   # else:
   #     print('babbel')

#for name, group in grouped:
    #print(name)
    #print(group)

 #   for entry in
#   group['Name'] = group.iloc[0, 1]
 #
   #print(len(group))
#grouped.get_group(4143)
#print(grouped)


# Project: for each letter in the alphabet, count the number of banks that start with that letter
# output: as dataframe and histogram

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('beschwerden_all.csv')

# only consider the name column
df_name_only = df[["Name"]]
#print(df_name_only)

# extract the initial of the name column into a dictionary
all_letters = {}
for entry in df_name_only['Name']:
    first_letter = (entry[0])
    #print(entry)
    if first_letter in all_letters:
        all_letters[first_letter] += 1
    else:
        all_letters[first_letter] = 1

#print(all_letters)
#print(len(all_letters))

# create a dataframe out of the dictionary
df_all_letters = pd.DataFrame({'letter':list(all_letters.keys()), 'number':list(all_letters.values())})

# sort dataframe according to column 'letter'
df_all_letters = df_all_letters.sort_values('letter')
print(df_all_letters)

# preparation for plotting: put the 2 dataframe columns into 2 lists
x = list(df_all_letters['letter'])
y = list(df_all_letters['number'])
#print(x)
#print(y)
assert len(x) == len(y)

# create a histogramm out of lists x and y:
plt.bar(range(len(y)), y, align='center')
plt.xticks(range(len(y)), x, size='small')
plt.xlabel('letter')
plt.ylabel('number')
plt.title('First Letter of the bank')
plt.show()
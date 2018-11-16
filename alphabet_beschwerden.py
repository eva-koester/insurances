#Project: alphabet (hackathon) --> for each letter in the alphabet, count the number of Name that start with that letter

import pandas as pd
import matplotlib.pyplot as plt

df_beschwerden = pd.read_csv('beschwerden_all.csv')

#dataframe erstellen, der nur den Tunnelnamen enthält:
df_name_only = df_beschwerden[["Name"]]
print(df_name_only)

#aus diesem dataframe den ersten index (0) des strings extrahieren: in ein dictionary (all_letters)
all_letters = {}

for entry in df_name_only['Name']:
    first_letter = (entry[0])
    print(entry)
    if first_letter in all_letters:
        all_letters[first_letter] += 1
    else:
        all_letters[first_letter] = 1

print(all_letters)
print(len(all_letters))

#dictionary in ein dataframe (um zu sortieren):
df_all_letters = pd.DataFrame({'letter':list(all_letters.keys()), 'number':list(all_letters.values())})

#dataframe nach column 'letter' sortieren:
df_all_letters = df_all_letters.sort_values('letter')
print(df_all_letters)

#dataframe mit 2 Columns in zwei Listen x und y (x für letter, y für number):
x = list(df_all_letters['letter'])
y = list(df_all_letters['number'])
print(x)
print(y)
assert len(x) == len(y)

#Histogramm aus den Listen x und y:
plt.bar(range(len(y)), y, align='center')
plt.xticks(range(len(y)), x, size='small')
plt.xlabel('letter')
plt.ylabel('number')
plt.title('First Letter of the bank')
plt.show()
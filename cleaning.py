# Project: clean the dataset: only one name for each number, drop year-duplicates (2007)
import pandas as pd


def load_clean_data():
    df = pd.read_csv('beschwerden_all.csv')
    # remove duplicates of year 2007 from the dataframe: create a new df that only includes year 2007, drop the duplicates,
    # remove all entries with year 2007 from the normal df, coerce the two df's
    df_year_2007 = df[df['Jahr'] == 2007]
    df_year_2007 = df_year_2007.drop_duplicates("Nummer", keep="first")
    df = df[df['Jahr'] != 2007]
    df = pd.concat([df, df_year_2007])
    # print(len(df))

    # Krankenkassen mit derselben Nummer haben denselben Namen
    grouped = df.groupby('Nummer')  ##--> Nummer wird zu name
    for nummer, group in grouped:
        name = group['Name'].iloc[0]
        df.loc[df['Nummer'] == nummer, 'Name'] = name
    #print(df.sort_values('Nummer'))
    return df

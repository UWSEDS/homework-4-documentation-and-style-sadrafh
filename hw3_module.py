"""
This Module helps to check the three amin requested crteria asked in teh assignments

"""

import pandas as pd


#Importing Data
DF_HW = pd.read_csv(
    'https://data.seattle.gov/api/views/65db-xm6k/rows.csv')

#Defining the function
def test_create_dataframe(df_initials, list_col): #the functions checks the criteria
    for k in list_col:
        if k not in list(df_initials.columns):
            raise ValueError("check the column names")
    df_1 = df_initials[list_col]
    for j in list(df_1.columns):
        if len(list(df_1[j])) > 0:
            result = all(type(df_1[j][i]) == type(df_1[j][0]) for i in range(len(df_1[j])))
    if not result:
        raise TypeError("Values in each columns have diffrenet types")
    df_2 = df_1
    if len(df_2) < 10:
        raise ValueError("it should be at least 10 rows")
    df_3 = df_2
    return df_3

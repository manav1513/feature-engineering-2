import seaborn as sns
import numpy as np
import pandas as pd

def By_deleting_rows(df):
    df = df.dropna()  
    return df
def imputation_technique(df):
    df['Age_mean'] = df.fillna(df['age'].mean())
    df['age_median']=df['age'].fillna(df['age'].median())

    return df


df = sns.load_dataset("titanic")

#print(df.shape)
#print(By_deleting_rows(df).shape)
#df1 = imputation_technique(df)
#print(df1)





import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE

def frame(x,y):
    df1=pd.DataFrame(x,columns=['f1','f2'])
    df2=pd.DataFrame(y,columns=['target'])
    final_df=pd.concat([df1,df2],axis=1)
    return final_df
def smort(df):
    oversample=SMOTE()
    x,y=oversample.fit_resample(df[['f1','f2']],df['target'])
    return frame(x,y)

x,y=make_classification(n_samples=1000,n_redundant=0,n_features=2,n_clusters_per_class=1,
                   weights=[0.90],random_state=12)

#y is  the feature and x is the target variable
df = frame(x,y)
#print(df.value_counts())
#print(plt.scatter(df['f1'],df['f2'],c=df['target']))
df = smort(df)
# print(df)
print(df.value_counts())
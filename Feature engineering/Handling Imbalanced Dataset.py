import numpy as np
import pandas as pd
from sklearn.utils import resample

def up(df):
    df_minority=df[df['target']==1]
    df_majority=df[df['target']==0]
    df_minority_upsampled=resample(df_minority,replace=True,n_samples=len(df_majority),random_state=42)
    df_upsampled=pd.concat([df_majority,df_minority_upsampled])
    return df_upsampled

def  down(data):
    df_minority=df[df['target']==1]
    df_majority=df[df['target']==0]
    df_majority_downsampled=resample(df_majority,replace=False,samples=len(df_minority),random_state=42)
    df_downsampled=pd.concat([df_minority,df_majority_downsampled])
    return df_downsampled

def class_A(a):
    class_0 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=a),
    'feature_2': np.random.normal(loc=0, scale=1, size=a),
    'target': [0] * a})
    return class_0

def class_B(b):
    class_1 = pd.DataFrame({
    'feature_1': np.random.normal(loc=2, scale=1, size=b),
    'feature_2': np.random.normal(loc=2, scale=1, size=b),
    'target': [1] * b })
    return class_1


np.random.seed(123)
samples = 1000
ratio = 0.9
a_class = int(samples * ratio)
b_class = samples - a_class

class_0 = class_A(a_class)
class_1 = class_B(b_class)
df=pd.concat([class_0,class_1])
ss = up(df)
print(ss['target'].value_counts())

## Minimum,MAximum,Median,Q1,Q3,IQR

import numpy  as np
lst=[45,32,56,75,89,54,32,89,90,87,67,54,45,98,99,67,74]
minimum,Q1,median,Q3,maximum=np.quantile(lst,[0,0.25,0.50,0.75,1.0])
IQR=Q3-Q1
lower_fence=Q1-1.5*(IQR)
higher_fence=Q3+1.5*(IQR)

outliers = []
for i in lst:
    if i>=0.75 and i<=142.75:
        print("not outlies")
    else:
        outliers.append(i)

print(outliers)
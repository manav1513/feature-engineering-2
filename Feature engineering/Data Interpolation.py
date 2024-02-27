import numpy as np
from scipy.interpolate import interp1d

def linear(x,y):
    x_new=np.linspace(1,5,10) 
    y_interp=np.interp(x_new,x,y)
    return x_new , y_interp
def Cubic(x,y):
    f=interp1d(x,y,kind='cubic')
    x_new = np.linspace(1, 5, 10)
    y_interp=f(x_new)
    return  x_new, y_interp
def polynomial(x,y):
    p=np.polyfit(x,y,2)
    x_new = np.linspace(1, 5, 10) 
    y_interp = np.polyval(p, x_new)
    return  x_new, y_interp


x=np.array([1,2,3,4,5])
y=np.array([2,4,6,8,10])

print(linear(x,y))
print("------------------------------")
print(Cubic(x,y))
print("------------------------------")
print(polynomial(x,y))
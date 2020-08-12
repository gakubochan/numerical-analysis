#二分法
import math
import numpy as np
def f(x):
    return math.cos(x)-x

a=0
b=1
n=0
while n<=10:
    c=(a+b)/2
    if np.sign(f(c))==np.sign(f(a)):
        a=c
    else: b=c
    n=n+1
print(c)




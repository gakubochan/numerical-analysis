#代入法
import math
import numpy as np
def g(a):
    return math.cos(a)

x=0.5
n=0
while n<12:
    x=g(x)
    n=n+1
print(x)
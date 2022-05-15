import math
import numpy as np
def func(t,x,m):
    return math.cos(m*t-x*math.sin(t))
def Im(x,N):
    h = math.pi / 2 ** N
    interval = [0, math.pi]
    I1=0
    I_1=0
    I__1=0
    I2=0
    I_2=0
    I__2=0
    t=0
    for i in range(1,int((2**N)/2)):
        I1+=2*func(t+2*i*h,x,1)
        I_1+=2*func(t+2*i*h,x+h,0)
        I__1+=2*func(t+2*i*h,x,0)
    for i in range(1,int((2**N/2)+1)):
        I2+=4*func(t+(2*i-1)*h,x,1)
        I__2+= 4 * func(t+(2*i-1)*h, x, 0)
        I_2+=4*func(t+(2*i-1)*h,x+h,0)
    return ((I1+I2+func(interval[0],x,1)+func(interval[1],x,1))*h+(I_1+I_2+func(interval[0],x+h,0)+func(interval[1],x+h,0)-I__1-I__2-func(interval[0],x,0)-func(interval[0],x,0)))/3
print(Im(float(input()),int(input())))


import numpy as np
import matplotlib.pyplot as plt
import math
def func_1(x,y,a,b):
    return a*x-b*x*y
def func_2(x,y,c,d):
    return c*x*y-d*y
def solution(func_1,func_2,N,interval_of_time,a,b,c,d,x0,y0):
    deltat=(interval_of_time[1]-interval_of_time[0])/2**N
    T=[(interval_of_time[0]+deltat*i) for i in range(0,2**N+1)]
    x=[]
    y=[]
    x.append(x0)
    y.append(y0)
    for i in range(0,2**N):
        x.append(x[i]+deltat*func_1(x[i],y[i]+(deltat/2)*func_1(x[i],y[i],a,b),a,b))
        y.append(y[i]+deltat*func_2(x[i],y[i] + (deltat/2) * func_2(x[i],y[i],c,d),c,d))
    fig,((ax1,ax2))=plt.subplots(nrows=1,ncols=2,figsize=(10,10))
    ax1.plot(T,x,color='green',label='Victims')
    ax1.plot(T,y,color='red',label='Predators')
    ax1.set_ylabel('Population',color='black')
    ax1.set_xlabel('Time',color='black')
    ax1.grid(True)
    ax1.legend()
    ax1.set_title('Solution')
    ax2.plot(x, y, color='black')
    ax2.set_ylabel('Predators', color='black')
    ax2.set_xlabel('Victims', color='black')
    ax2.grid(True)
    ax2.set_title('Phase trajectory')
    plt.show()
solution(func_1,func_2,int(input()),[0,6],10,2,2,10,1,1)
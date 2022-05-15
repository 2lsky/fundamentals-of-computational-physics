import math
import matplotlib.pyplot as plt
import numpy as np
def li(i,x,xi,n):
    li=1
    for j in range(0,n+1):
        if j!=i:
            li*=(x-xi[j])/(xi[i]-xi[j])
    return li
def L(n,x,xi,yi):
    L=0
    for i in range(0,n+1):
        L+=li(i,x,xi,n)*yi[i]
    return L
def interpolation(n):
    xk=[1+k/n for k in range(0,n+1)]
    yk=[math.log(x) for x in xk]
    x=np.linspace(xk[0],xk[len(xk)-1],1001)
    ln = [math.log(x) for x in x]
    y = [L(n, x, xk, yk) for x in x]
    delta=[(y[i]-ln[i]) for i in range(0,len(y))]
    fig,((ax1,ax2))=plt.subplots(nrows=1, ncols=2,figsize=(10,5))
    ax1.set_xlabel('x',color='black')
    ax1.set_ylabel('y', color='black')
    ax1.set_title('Pn(x)', color='black')
    ax1.grid(True)
    ax2.set_xlabel('x', color='black')
    ax2.set_ylabel('y', color='black')
    ax2.set_title('Pn(x)-ln(x)', color='black')
    ax2.grid(True)
    ax1.plot(x,y,color='black')
    ax2.plot(x,delta,color='black')
    plt.show()
print(interpolation(int(input())))
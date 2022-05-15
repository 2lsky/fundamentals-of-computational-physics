import numpy as np
import matplotlib.pyplot as plt
import math
def func(y):
    return -y
def solution(func,y0,interval,N):
    h=(interval[1]-interval[0])/2**N
    y=y0
    y1=y0
    y2=y0
    x=interval[0]
    yi=[]
    xi=[]
    yi1=[]
    yi2=[]
    yi.append(y)
    xi.append(x)
    yi1.append(y1)
    yi2.append(y2)
    xn=np.linspace(interval[0],interval[1],1001)
    yn=[math.exp(-i) for i in xn]
    for i in range(1,2**N+1):
        y+=h*func(y)
        y1+=h*func(y1+(h/2)*func(y1))
        y2+=h*(func(y2)+2*(func(y2+h*func(y2)/2))+2*(func(y2+h*func(y2+h*func(y2)/2)/2))+func(y2+h*func(y2+h*func(y2+h*func(y2)/2)/2)))/6
        x+=h
        yi.append(y)
        yi1.append(y1)
        yi2.append(y2)
        xi.append(x)
    y_2 = [math.exp(-i) for i in xi]
    delta = [math.fabs((y_2[i] - yi[i])) for i in range(0, len(yi))]
    delta1=[math.fabs((y_2[i] - yi1[i])) for i in range(0, len(yi1))]
    delta2=[math.fabs((y_2[i] - yi2[i])) for i in range(0, len(yi2))]
    fig,((ax1,ax2),(ax3,ax4),(ax5,ax6))=plt.subplots(nrows=3,ncols=2,figsize=(14,14))
    plt.subplots_adjust(wspace=0.3, hspace=0.4)
    ax1.plot(xi,yi,color='black',label='Eiler solution',marker='o',markersize='3')
    ax1.plot(xn,yn,color='green',label='exp(-x)')
    ax1.set_xlabel('x',color='black')
    ax1.set_ylabel('y',color='black')
    ax1.set_title('Solution dy/dx=-y')
    ax1.grid(True)
    ax1.legend()
    ax2.plot(xi,delta,color='black')
    ax2.set_xlabel('x', color='black')
    ax2.set_ylabel('Modulus of Error', color='black')
    ax2.set_title('Accurancy of Eiler')
    ax2.grid(True)
    ax3.plot(xi, yi1, color='black', label='Runge 2 solution',marker='o',markersize='3')
    ax3.plot(xn, yn, color='green', label='exp(-x)')
    ax3.set_xlabel('x', color='black')
    ax3.set_ylabel('y', color='black')
    ax3.set_title('Solution dy/dx=-y')
    ax3.grid(True)
    ax3.legend()
    ax4.plot(xi, delta1, color='black')
    ax4.set_xlabel('x', color='black')
    ax4.set_ylabel('Modulus of Error', color='black')
    ax4.set_title('Accurancy of Runge 2')
    ax4.grid(True)
    ax5.plot(xi, yi2, color='black', label='Runge 4 solution', marker='o', markersize='3')
    ax5.plot(xn, yn, color='green', label='exp(-x)')
    ax5.set_xlabel('x', color='black')
    ax5.set_ylabel('y', color='black')
    ax5.set_title('Solution dy/dx=-y')
    ax5.grid(True)
    ax5.legend()
    ax6.plot(xi, delta2, color='black')
    ax6.set_xlabel('x', color='black')
    ax6.set_ylabel('Modulus of Error', color='black')
    ax6.set_title('Accurancy of Runge 4')
    ax6.grid(True)
    plt.show()
solution(func,1,[0,3],int(input()))
import math
import matplotlib.pyplot as plt
import numpy as np
def p(x):
    return 0
def q(x):
    return 0
def f(x):
    return math.sin(x)
def f1(x,p,f,h):
    return f(x)/(1+p(x)*h/2)
def m(x,p,q,h):
    return -(2-q(x)*h**2)/(1+p(x)*h/2)
def n(x,p,h):
    return (1-p(x)*h)/(1+p(x)*h/2)
def progonka(x0,x1,N,a0,a1,b0,b1,f1,m,n,A,B):
    h=(x1-x0)/2**N
    x=[x0+i*(x1-x0)/2**N for i in range(0,2**N+1)]
    if a1!=0:
        c0=a1/(a0*h-a1)
        d0=A*h/a1
        c=[]
        d=[]
        c.append(c0)
        d.append(d0)
        for i in range(1,2**N):
            c.append(1/(m(x[i],p,q,h)-n(x[i],p,h)*c[i-1]))
            d.append(f1(x[i],p,f,h)*h**2-n(x[i],p,h)*c[i-1]*d[i-1])
        y=[]
        yn=(B*h+b1*c[2**N-1]*d[2**N-1])/(b0*h+b1*(c[2**N-1]+1))
        y.append(yn)
        for i in range(1,2**N+1):
            y.append(c[2**N-i]*(d[2**N-i]-y[i-1]))
        fig,(ax1,ax2)=plt.subplots(nrows=1,ncols=2,figsize=(10,10))
        ax1.plot(x,y[::-1],color='green',label='approximental solution')
        ax1.plot()
        ax1.grid()
        ax1.legend()
        ax1.set_xlim(x0,x1)
        M = np.array([[a0 * x0 + a1, a0], [x1 * b0 + b1, b0]])
        V = np.array([A + a0 * math.sin(x0) + a1 * math.cos(x0), B + b0 * math.sin(x1) + b1 * math.cos(x1)]).reshape((2,1))
        C = np.linalg.solve(M, V)
        y1 = [-math.sin(x) + C[0] * x + C[1] for x in x]
        accurancy = [(y[::-1][i] - y1[i]) for i in range(0, len(y))]
        ax2.plot(x,accurancy, label='accurancy')
        ax2.grid(True)
        ax2.legend()
        ax2.set_xlim(x0, x1)
    else:
        c = []
        c0=0
        c.append(c0)
        d=[]
        d1 = f1(x[1], p, f, h) * h ** 2 - n(x[1], p, h) * A
        d.append(d1)
        for i in range(1,2**N):
            c.append(1 / (m(x[i], p, q, h) - n(x[i], p, h) * c[i - 1]))
        for i in range(2,2**N):
            d.append(f1(x[i], p, f, h) * h ** 2 - n(x[i], p, h) * c[i - 1] * d[i-2])
        y=[]
        yn=(B*h+b1*c[2**N-1]*d[2**N-2])/(b0*h+b1*(c[2**N-1]+1))
        y.append(yn)
        for i in range(1,2**N):
            y.append(c[2**N-i]*(d[2**N-i-1]-y[i-1]))
        y.append((A*h-a1*y[2**N-1])/(a0*h-a1))
        fig,(ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))
        ax1.plot(x, y[::-1], color='green', label='approximental solution')
        ax1.grid()
        ax1.legend()
        ax1.set_xlim(x0, x1)
        M=np.array([[a0*x0+a1,a0],[x1*b0+b1,b0]])
        V=np.array([A+a0*math.sin(x0)+a1*math.cos(x0),B+b0*math.sin(x1)+b1*math.cos(x1)]).reshape((2,1))
        C=np.linalg.solve(M,V)
        y1=[-math.sin(x)+C[0]*x+C[1] for x in x]
        accurancy=[(y[::-1][i]-y1[i]) for i in range(0,len(y))]
        ax2.plot(x,accurancy,label='accurancy')
        ax2.grid(True)
        ax2.legend()
        ax2.set_xlim(x0,x1)
    plt.show()

print(progonka(0,math.pi,7,1,0,1,0,f1,m,n,5,5.5))



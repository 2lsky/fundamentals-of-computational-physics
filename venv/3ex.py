import math
import matplotlib.pyplot as plt
import numpy as np
def func_1(x):
    return 1/(1+x**2)
def func_2(x):
    return (x**(1/3))*math.exp(math.sin(x))
def integration(func,interval,N):
    h=(interval[1]-interval[0])/(2**N)
    x=interval[0]
    X=[]
    I1=0
    S1=0
    S2=0
    while (x<interval[1]):
        X.append(x)
        x=x+h
    X.append(interval[1])
    #трапеция
    for i in range(0,len(X)-1):
        I1+=(func(X[i])+func(X[i+1]))*h/2
    #симпсон
    for i in range(1,int((2**N)/2)):
        S1+=2*func(X[2*i])
    for i in range(1,int((2**N/2)+1)):
        S2+=4*func(X[2*i-1])
    I2=(S1+S2+func(interval[0])+func(interval[1]))*h/3
    return [I1,I2]
def integration_error_for_func_1(integral,interval):
    N=[2**i for i in range(0,5)]
    N1=np.linspace(0,N[len(N)-1],1001)
    error_of_trapezoid_integration=[math.fabs((-integral(func_1,interval,N[i])[0]+math.pi/2)) for i in range(0,len(N))]
    error_of_simpson_integration=[math.fabs((-integral(func_1, interval, N[i])[1] + math.pi / 2)) for i in range(0, len(N))]
    plt.figure(figsize=(8, 6))
    plt.xlabel('N', color='black')
    plt.ylabel('Error', color='black')
    plt.grid(True)
    plt.axis([0, N[len(N)-1], 0, 3*max(error_of_trapezoid_integration)/2])
    plt.semilogy(N,error_of_trapezoid_integration,'b^',label='Trapezoid')
    plt.semilogy(N, error_of_simpson_integration,'ro',markersize=3,label='Simpson')
    #plt.semilogy(N1,0.07/N1**2,'g-',label='~a/N^2')
    #plt.semilogy(N1,0.07/N1**4,'y-',label='~a/N^4')
    plt.ylim(0,100)
    plt.xlim(0,20)
    plt.legend()
    plt.show()
def graph_of_tpapezoid_method(func,N,interval):
    x=np.linspace(interval[0],interval[1],1001)
    x1=np.linspace(interval[0],interval[1],2**N+1)
    y=[func(x) for x in x]
    y1=[func(x) for x in x1]
    fig=plt.figure(figsize=(10,10))
    axes = fig.subplots(1,1)
    axes.set_xlabel('x', color='black')
    axes.set_ylabel('y', color='black')
    axes.set_xlim([interval[0],interval[1]])
    axes.set_ylim([0,max(y)+1])
    axes.set_title('Method of trapezoid')
    axes.plot(x,y,'black')
    points_1=[[x1[i],y1[i]] for i in range(0,len(x1))]
    points_2 = [[x1[len(x1)-i], 0] for i in range(1, len(x1)+1)]
    polygon = plt.Polygon(points_1+points_2,facecolor='deepskyblue', edgecolor='b',linewidth=2,linestyle='-')
    axes.vlines(x1,0,y1,'b')
    axes.add_patch(polygon)
    axes.text((interval[1]+interval[0])/2,max(y)*1.5,f'N={2**N}',color='black',size=50)
    axes.plot(x1,y1,'o',color='black')
    axes.plot(x1,[0]*len(x1),'o',color='black')
    plt.show()
graph_of_tpapezoid_method(func_1,int(input()),[-1,1])
integration_error_for_func_1(integration,[-1,1])
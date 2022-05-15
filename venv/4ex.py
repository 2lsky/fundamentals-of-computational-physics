import math
import matplotlib.pyplot as plt
def dI0(t,x):
    return -math.sin(t)*math.sin(math.sin(t)*(x))
def I1(t,x):
    return math.cos(t-x*math.sin(t))
def value(x,N):
    h=math.pi/10**N
    S1=0
    for i in range(1,int((10**N)/2)):
        S1+=2*(I1(2*i*h,x)+dI0(2*i*h,x))+4*(I1((2 * i - 1) * h, x) + dI0((2 * i - 1) * h, x))
    return (S1+4*(I1(((10**N) - 1) * h, x) + dI0(((10**N) - 1) * h, x))+I1(0,x)+I1(math.pi,x)+dI0(0,x)+dI0(math.pi,x))*h/3
def comparison(N,func,interval):
    bool=True
    h=(interval[1]-interval[0])/10**N
    x0=interval[0]
    for i in range(0,int(10**N)+1):
        if math.fabs(func(x0+i*h,N))>(10**(-10)):
            bool = False
            break
    return bool
def graph(func,interval,N):
    h = (interval[1] - interval[0]) / 10 ** N
    x=[interval[0]+h*i for i in range(0,10**N+1)]
    y=[func(x,N) for x in x]
    plt.subplots()
    plt.grid(True)
    plt.xlabel('x', color='black')
    plt.ylabel('dI0(x)/dx+I1(x)', color='black')
    xmin=float('{:.4f}'.format(interval[0]))
    xmax=float('{:.4f}'.format(interval[1]))
    plt.text((interval[1]-interval[0])/2,5*max(y),f'x: from {xmin} to {xmax}...')
    plt.axis([interval[0], interval[1], min(y)*10, max(y)*10])
    plt.plot(x, y,'black')
    plt.show()
graph(value,[0,2*math.pi],int(input()))


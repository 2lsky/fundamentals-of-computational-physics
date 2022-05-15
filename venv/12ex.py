import math
import cmath
import matplotlib.pyplot as plt
def signal(t,a0,a1,w1,w2):
    return a0*math.sin(w1*t)+a1*math.sin(w2*t)
def window_hanna(size,t):
    return (1-math.cos(2*math.pi*t/(size-1)))/2
def fouier(signal,t0,t1,N,type_of_window,a0,a1,w1,w2):
    window=(t1-t0)
    deltat=window/N
    t=[i*deltat for i in range(0,N+1)]
    f1=[]
    f2=[]
    for k in range(0,len(t)):
        sum1=0
        sum2=0
        for i in range(0,len(t)):
            sum1+=signal(t[i],a0,a1,w1,w2)*cmath.exp((-2*math.pi*k*i*(1j))/N)
            sum2+=signal(t[i],a0,a1,w1,w2)*cmath.exp((-2*math.pi*k*i*(1j))/N)*type_of_window(len(t),i)
        f1.append(abs(sum1))
        f2.append(abs(sum2))
    fig=plt.figure(figsize=(10,10))
    ax1=fig.add_subplot(111)
    ax1.plot([2*math.pi*k/(window) for k in range(0,int(len(t)/2)+1)],f1[:int(len(t)/2)+1],label='square_window')
    ax1.plot([2*k*math.pi/(window) for k in range(0,int(len(t)/2)+1)],f2[:int(len(t)/2)+1],label='hanna_window')
    ax1.legend()
    ax1.grid(True)
    plt.show()
fouier(signal,2,4,1000,window_hanna,10,20,30,30.5)



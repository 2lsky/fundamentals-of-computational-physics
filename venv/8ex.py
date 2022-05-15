import matplotlib.pyplot as plt
import math
import numpy as np
def func_1(u,v):
    return 998*u+1998*v
def func_2(u,v):
    return -999*u-1999*v
def eiler1(N,func_1,func_2,interval_of_time,u0,v0):
    deltat = (interval_of_time[1] - interval_of_time[0]) / 2 ** N
    T = [(interval_of_time[0] + deltat * i) for i in range(0, 2 ** N + 1)]
    u = []
    v = []
    u.append(u0)
    v.append(v0)
    for i in range(0, 2 ** N):
        v.append(v[i]+deltat*func_2(u[i],v[i]))
        u.append(u[i] + deltat * func_1(u[i], v[i]))
    fig, ((ax1, ax2,ax3,ax4)) = plt.subplots(nrows=1, ncols=4, figsize=(20, 20))
    ax1.plot(T, u, color='green', label='u(t)')
    ax1.plot(T, v, color='red', label='v(t)')
    ax1.set_ylabel('f(t)', color='black')
    ax1.set_xlabel('t', color='black')
    ax1.grid(True)
    ax1.legend()
    ax1.set_title('Solution')
    ax2.plot(u, v, color='black')
    ax2.set_ylabel('v', color='black')
    ax2.set_xlabel('u', color='black')
    ax2.grid(True)
    ax2.set_title('Phase trajectory')
    c1=2*v0+u0
    c2=-u0-v0
    delta1=[math.fabs(u[i]-(-c1*math.exp(-1000*T[i])-2*c2*math.exp(-T[i]))) for i in range(0,len(T))]
    delta2 = [math.fabs(v[i] - (c1 * math.exp(-1000 * T[i]) + c2 * math.exp(-T[i]))) for i in range(0, len(T))]
    ax3.plot(T,delta1)
    ax3.set_title('Error of u(t)')
    ax3.grid(True)
    ax4.plot(T,delta2)
    ax4.set_title('Error of v(t)')
    ax4.grid(True)
    plt.show()
def eiler2(N,interval_of_time,u0,v0):
    deltat = (interval_of_time[1] - interval_of_time[0]) / 2 ** N
    T = [(interval_of_time[0] + deltat * i) for i in range(0, 2 ** N + 1)]
    u = [u0]
    v = [v0]
    for i in range(0, 2 ** N):
        u.append((1999 * deltat * u[i] + u[i] +1998 * deltat * v[i]) / (1000 * deltat**2 + 1001 * deltat + 1))
        v.append((-999 * deltat * u[i] - 998 * deltat * v[i] +v[i]) / (1000 * deltat**2 + 1001 * deltat + 1))
    fig, ((ax1, ax2, ax3, ax4)) = plt.subplots(nrows=1, ncols=4, figsize=(20, 20))
    ax1.plot(T, u, color='green', label='u(t)')
    ax1.plot(T, v, color='red', label='v(t)')
    ax1.set_ylabel('f(t)', color='black')
    ax1.set_xlabel('t', color='black')
    ax1.grid(True)
    ax1.legend()
    ax1.set_title('Solution')
    ax2.plot(u, v, color='black')
    ax2.set_ylabel('v', color='black')
    ax2.set_xlabel('u', color='black')
    ax2.grid(True)
    ax2.set_title('Phase trajectory')
    c1 = 2 * v0 + u0
    c2 = -u0 - v0
    delta1 = [math.fabs(u[i] - (-c1 * math.exp(-1000 * T[i]) - 2 * c2 * math.exp(-T[i]))) for i in range(0, len(T))]
    delta2 = [math.fabs(v[i] - (c1 * math.exp(-1000 * T[i]) + c2 * math.exp(-T[i]))) for i in range(0, len(T))]
    ax3.plot(T, delta1)
    ax3.set_title('Error of u(t)')
    ax3.grid(True)
    ax4.plot(T, delta2)
    ax4.set_title('Error of v(t)')
    ax4.grid(True)
    plt.show()
eiler1(int(input()),func_1,func_2,[0,1],1,2)
eiler2(int(input()),[0,1],1,2)
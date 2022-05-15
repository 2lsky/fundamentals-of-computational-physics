
import numpy as np
import matplotlib.pyplot as plt
def func(x):
    return x*(1-x)**2
def cranck_nick(N1,N2,t0,t1,x0,x1):
    deltat=(t1-t0)/N1
    deltax=(x1-x0)/N2
    x=[x0+i*deltax for i in range(0,N2+1)]
    t=[t0+i*deltat for i in range(0,N1+1)]
    A=np.array(np.random.randint(0,1,(N2+1)**2).reshape(N2+1,N2+1))
    q = deltat / (deltax ** 2)
    A[0][0], A[A.shape[0] - 1][A.shape[0] - 1] = 1, 1
    for i in range(1, N2):
        A[i][i] = 1 + q
        A[i][i-1]=-q/2
        A[i][i+1]=-q/2
    U0=np.array([func(x) for x in x]).reshape(N2+1,1)
    U=U0
    T=[]
    T.append(max(U0)[0])
    fig = plt.figure(figsize=(20, 20))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.grid(True)
    for i in range(0,len(t)-1):
        B=np.array([0])
        B=np.append(B,[U[i]+((deltat)*(U[i-1]-2*U[i]+U[i+1]))/(2*deltax**2) for i in range(1,len(U)-1)])
        B=np.append(B,[0])
        B1=B.reshape(N2+1,1)
        U = np.linalg.solve(A, B1)
        ax1.plot(x,U)
        T.append(max(U)[0])
    ax2.plot(t, T)
    ax2.grid(True)
    plt.show()
print(cranck_nick(1000,100,0,2,0,1))
import numpy as np
import matplotlib.pyplot as plt
import math
def E(N,m):
    E=np.array([0]*N**2).reshape(N,N)
    for i in range(0,N):
        E[i][i]=1
    return m*E
def lambd(V0,V1):
    sum=0
    for i in range(0,V0.shape[0]):
        sum+=(V0[i])/(V1[i])
    return sum/(V0.shape[0])
def func(x):
    return x**2/2
def sh(N,x0,x1):
    deltax=(x1-x0)/N
    x=[x0+i*deltax for i in range(0,N+1)]
    A=np.zeros((N+1,N+1))
    U = np.array([func(x) for x in x])
    for i in range(0, N+1):
        A[i][i] = -2-2*U[i]*(deltax**2)
    for i in range(0,N):
        A[i][i+1]=+1
    for i in range(1,N+1):
        A[i][i-1]=+1
    v0=np.array(np.random.randint(1,2,N+1))
    V0=v0.reshape(N+1,1)
    V=V0/math.sqrt(N+1)
    lamb=[]
    lamb.append(lambd(V, np.linalg.solve(A, V)))
    V=np.linalg.solve(A, V)/np.linalg.norm(np.linalg.solve(A, V))
    i=0
    while i<50:
        lamb.append(lambd(V,np.linalg.solve(A, V)))
        V=np.linalg.solve(A, V)/np.linalg.norm(np.linalg.solve(A, V))
        i+=1
    psi=[math.fabs(x[0]) for x in V]
    fig,ax1=plt.subplots(ncols=1,nrows=1)
    ax1.plot(x,psi)
    ax1.grid(True)
    plt.show()
    return lamb[len(lamb)-1]/(-2*deltax**2)
def sh_1(N,x0,x1):
    delta_lambd_res=[]
    delta_max_component=[]
    fig, ax1 = plt.subplots(ncols=1, nrows=1)
    for n in N:
        deltax=(x1-x0)/n
        x=[x0+i*deltax for i in range(0,n+1)]
        A=np.zeros((n+1,n+1))
        U = np.array([func(x) for x in x])
        for i in range(0, n+1):
            A[i][i] = -2-2*U[i]*(deltax**2)
        for i in range(0,n):
            A[i][i+1]=+1
        for i in range(1,n+1):
            A[i][i-1]=+1
        v0=np.array(np.random.randint(1,2,n+1))
        V0=v0.reshape(n+1,1)
        V=V0/math.sqrt(n+1)
        lamb=[]
        lamb.append(lambd(V, np.linalg.solve(A, V)))
        V=np.linalg.solve(A, V)/np.linalg.norm(np.linalg.solve(A, V))
        i=0
        while i<50:
            lamb.append(lambd(V,np.linalg.solve(A, V)))
            V=np.linalg.solve(A, V)/np.linalg.norm(np.linalg.solve(A, V))
            i+=1
        psi=[math.fabs(x[0]) for x in V]
        #fig,(ax1,ax2)=plt.subplots(ncols=1,nrows=1)
        #ax1.plot(x,psi)
        #ax1.grid(True)
        #plt.show()
        #delta_mod_vector.append(1-np.linalg.norm(V))
        delta_lambd_res.append(0.5-lamb[len(lamb)-1]/(-2*deltax**2))
        delta_max_component.append(-max(psi)+0.1)
        #print(delta_max_component)
        #print(delta_max_component)
        ax1.plot(x,psi)
        ax1.grid(True)
    #ax2.grid(True)
    #ax2.plot(N,delta_mod_vector)
    plt.show()
    print([math.log2(x) for x in [delta_lambd_res[i]/delta_lambd_res[i+1] for i in range(0,len(delta_lambd_res)-1)]])
    print([math.log2(x) for x in [delta_max_component[i]/delta_max_component[i+1] for i in range(0,len(delta_max_component)-1)]])
sh_1([16,32,64,128,256,512],-5,5)
#print(sh(10,-5,5))
import math
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import keyboard
def deltamass(A,B):
    return [A[i]-B[i] for i in range(0,len(B))]
def func0(x):
    return math.exp(-x**2/2)
def solution_hoph(t0,t1,N1,x0,x1,N2,func0):
    deltat=(t1-t0)/N1
    deltax=(x1-x0)/N2
    x=[x0+i*deltax for i in range(0,N2+1)]
    t=[t0+i*deltat for i in range(0,N1+1)]
    U0=[func0(x) for x in x]
    Ureal=[]
    for j in t:
        Urealt=[]
        for i in x:
            Urealt.append(fsolve(lambda y:y-math.exp(-(i-y*j)**2/2),0))
        Ureal.append(Urealt)
    Umass1=[]
    Umass2=[]
    Umass1.append(U0)
    Umass2.append(U0)
    for j in range(0,N1):
        Unext1=[]
        Unext2=[]
        Unext1.append(Umass1[j][0])
        Unext2.append(Umass2[j][0])
        for i in range(1,len(Umass1[j])-1):
            Unext1.append((Umass1[j][i+1]+Umass1[j][i-1])/2-((deltat)/(2*deltax))*(((Umass1[j][i+1])**2)/2-((Umass1[j][i-1])**2)/2))
            if Umass2[j][i]>=0:
                Unext2.append(Umass2[j][i]-(deltat / deltax) * (((Umass2[j][i]) ** 2) / 2 - ((Umass2[j][i-1]) ** 2) / 2))
            else:
                Unext2.append(Umass2[j][i] - (deltat / deltax) * (((Umass2[j][i+1]) ** 2) / 2 - ((Umass2[j][i]) ** 2) / 2))
        Unext1.append(Umass1[j][-1])
        Unext2.append(Umass2[j][-1])
        Umass1.append(Unext1)
        Umass2.append(Unext2)
    return Ureal,Umass1,Umass2,x,t
def draw(data):
    fig=plt.figure(figsize=(10,10))
    plt.subplots_adjust(hspace=0.5,wspace=0.5)
    ax1=fig.add_subplot((321))
    ax1.set_title('Scheme of Laks ((deltat/deltax)*max(U(x,t))<=1)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('U(x)')
    ax1.grid(True)
    ax2=fig.add_subplot((322))
    ax2.set_title('Scheme of Curant-Rice ((deltat/deltax)*max(U(x,t))<=1)')
    ax2.set_xlabel('x')
    ax2.set_ylabel('U(x)')
    ax2.grid(True)
    ax3 = fig.add_subplot((323))
    ax3.set_title('Error of Laks')
    ax3.set_xlabel('x')
    ax3.set_ylabel('deltaU(x)')
    ax3.grid(True)
    ax4 = fig.add_subplot((324))
    ax4.set_title('Error of Curant-Rice')
    ax4.set_xlabel('x')
    ax4.set_ylabel('deltaU(x)')
    ax4.grid(True)
    ax5 = fig.add_subplot((313))
    ax5.set_title('Comparison of errors')
    ax5.set_xlabel('t')
    ax5.set_ylabel('maxdeltaU(x)')
    ax5.grid(True)
    ax5.plot(data[4],[max(deltamass(data[0][i],data[1][i])) for i in range(0,len(data[0]))],color='red',label='Laks')
    ax5.plot(data[4], [max(deltamass(data[0][i], data[2][i])) for i in range(0, len(data[0]))],color='green',label='C-R')
    ax5.legend()
    i=0
    while True:
        if i>=len(data[0]):
            i=len(data[0])-1
        elif i<0:
            i=0
        line1,=ax1.plot(data[3],data[1][i],color='black')
        line2,=ax2.plot(data[3],data[2][i],color='black')
        line3,=ax3.plot(data[3],deltamass(data[0][i],data[1][i]),color='black')
        line4,=ax4.plot(data[3],deltamass(data[0][i],data[2][i]),color='black')
        plt.waitforbuttonpress()
        if keyboard.is_pressed('Right'): 
            i+=1
        elif keyboard.is_pressed('Left'):
            i-=1
        line1.remove()
        line2.remove()
        line3.remove()
        line4.remove()
    plt.show()
data=solution_hoph(0,10,10,-5,10,150,func0)
draw(data)

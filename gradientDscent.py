import numpy as np
import matplotlib.pyplot as plt

c=np.array([0.15*np.pi])
def f(x):
    return np.sin(x*c)*x

def f_grad(x):
    return np.sin(x*c)+np.cos(x*c)*x*c

x=np.array([87])
learnRate=0.01
epochs=1000
result=[]

def gradient_descent(x):
    result.append(x)
    for i in range(epochs):
        x=x-learnRate*f_grad(x)
        print(f"Epoch: {i+1}, x: {x}")
        result.append(x)

def show_trace(results):
    n = max(abs(min(results)), abs(max(results)))
    f_line=np.arange(80,n+5,0.001)
    y=f(f_line)
    plt.plot(f_line,y)
    plt.plot(results,f(result),color='red')
    plt.show()

gradient_descent(x)
show_trace(result)





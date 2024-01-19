import math

import numpy as np

def myLog(p):
    n=len(p)
    lnp=np.zeros(n)
    for i in range(n):
        if p[i]==0:
            lnp[i]=0
        else:
            lnp[i]=np.log(p[i])
    return lnp

X=np.array([[9,0,0,0],[8,3,0.9,0.5],[6,7,0.2,1]]) # 正向化之后的矩阵

Z=X/np.sqrt(np.sum(X*X,axis=0)) # 对X进行标准化
print(Z)

n,m=Z.shape
D=np.zeros(m)

for  i in range(m):
    x=Z[:,i]
    p=x/np.sum(x)
    e= -np.sum(p*myLog(p))/np.log(n)
    D[i]=1-e

W=D/np.sum(D)
print(f"Entropy Weight is {W}")


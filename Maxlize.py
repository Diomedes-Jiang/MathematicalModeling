import numpy as np

def minToMax(max, x):
    x=list(x)
    ans=[[(max-e)]for e in x]
    return np.array(ans)

def midToMax(best, x):
    x=list(x)
    h=[abs(e-best) for e in x]
    M=max(h)
    if M==0:
        return np.array(x)
    ans=[[(1-e/M)]for e in h]
    return np.array(ans)

def regToMax(low,high, x):
    x=list(x)
    M=max(low-min(x),max(x)-high)
    if M==0:
        return np.array(x)
    ans=[]
    for i in range(len(x)):
        if x[i]<low:
            ans.append([(1-(low-x[i])/M)])
        elif x[i]>high:
            ans.append([(1-(x[i]-high)/M)])
        else:
            ans.append([1])
    return np.array(ans)
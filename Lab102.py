import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    s=1/(1+np.exp(-x))
    ds=s*(1-s)
    return s,ds

X=np.linspace(-10, 10, 100)
Y1,Y2=sigmoid(X)

plt.plot(X,Y1,X,Y2)
plt.xlabel("x")
plt.ylabel("Sigmoid(X), Sigmoid'(X)")
plt.show()
import numpy as np
y=np.array([1,1,2,2,4])
ypred=np.array([0.7,1.34,1.89,2.53,3.2])
mse=(np.square(ypred-y)).mean()
print(mse)
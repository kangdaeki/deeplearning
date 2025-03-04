import matplotlib.pyplot as plt
import numpy as np

numbers=np.random.normal(size=10_000)
plt.hist(numbers)
plt.xlabel("Value")
plt.ylabel("Freq.")
plt.show()
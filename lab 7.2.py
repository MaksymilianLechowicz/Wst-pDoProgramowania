import numpy as np
a= np.random.randint(low=0, high=75, size=(5,5))
print(a)
print(a.max())
print(a.min())
print(a.max(axis=1))
print((a.max(axis=1)).min())
print(a.max(axis=0))

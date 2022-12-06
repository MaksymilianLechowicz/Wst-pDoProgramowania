import numpy as np
b = np.random.randint(low=-0, high=1, size=(3,3))
c = np.zeros((3,3))
print(b)
b[:2, [0,2]] = 1
print(b)
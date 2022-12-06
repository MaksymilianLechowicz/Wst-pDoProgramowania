import numpy as np
tab = [2**i for i in range(0,8)]
print(tab)
tab.reverse()
wagi = np.array(tab)
print(wagi)
liczba_bin= np.random.randint(low=0, high=2, size=8)
print(liczba_bin)
tab2=liczba_bin*wagi
print(tab2)
print(tab2.sum())
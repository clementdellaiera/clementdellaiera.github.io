from random import randint
from numpy import exp, matmul,array, zeros
from numpy.random import uniform, binomial
from matplotlib import pyplot as plt
from matplotlib.pyplot import pcolor

T=100 # nombre de jours
n=100 # nombre de lampadaires

L=zeros((n,T)) #L[x,t]

for t in range(T):
    L[0,t]=1

print(L)

for t in range(T-1):
    for x in range(n-1):
        if (L[x,t]==1):
            L[x+1,t+1] = 1-L[x+1,t]
        else:
            L[x+1,t+1] = L[x+1,t]

print(L)

plt.figure()
plt.pcolor(L)
plt.show()

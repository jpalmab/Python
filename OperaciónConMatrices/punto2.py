import matplotlib.pyplot as plt
from numpy import arange, tanh

plt.figure()  
x = arange(-2,2)   
y = tanh(x)
plt.plot(x,y)
plt.grid(True)
plt.ylabel(' Y ')
plt.xlabel(' X ')
plt.savefig("grafica.png")
plt.show()


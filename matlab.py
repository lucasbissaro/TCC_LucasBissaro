import matplotlib.pyplot as plt
import math

valores=[x for x in range(0,10000,1)]
coluna0 = [x for x in valores]
coluna1 = [math.cos((x*0.003))+1 for x in valores]


#plota o grafico
plt.plot(coluna0, coluna1)
plt.fill_between(coluna0, 0, coluna1)
plt.show()
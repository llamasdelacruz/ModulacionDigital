import numpy as np
import matplotlib.pyplot as plt

x = [i for i in range(7)]
y = []

x2 = "0101001"
for bit in x2:
    if(bit == "1"):
        y.append(20)
    else:
        y.append(0)

plt.step(x, y, where='post', label='post')
plt.plot(x, y, 'o--', color='grey', alpha=0.3)

plt.grid(axis='x', color='0.95')
plt.legend(title='Parameter where:')
plt.title('plt.step(where=...)')
plt.show() 
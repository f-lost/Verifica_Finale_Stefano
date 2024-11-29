import numpy as np
import matplotlib.pyplot as plt


data = np.random.rand(50).round(decimals=2)

data = data.reshape(10, 5)

for i, riga in enumerate(data):

    riga_unici= set(riga)

    while len(riga_unici) < 5:
        riga_unici.add(np.random.rand())
    
    data[i] = np.array(list(riga_unici))



normalized_data = (data * 100).astype(int)

print(normalized_data)


plt.figure(figsize=(10, 6))
for i in range(data.shape[0]):
    plt.scatter([i]*5, data[i], label=f"Riga {i}")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.title('ScatterPlot della matrice')
plt.grid(True)
plt.tight_layout()
plt.show()
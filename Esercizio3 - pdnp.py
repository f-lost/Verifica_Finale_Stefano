import numpy as np
import matplotlib.pyplot as plt

#creo 50 numeri casuali e li arrotondo
data = np.random.rand(50).round(decimals=2)

#li formatto in una tabello 10x5
data = data.reshape(10, 5)

#controllo che ogni riga sia composta da valori unici
for i, riga in enumerate(data):

    riga_unici= set(riga) #con il set elimino i duplicati

    while len(riga_unici) < 5: #finchè la lunghezza del set non sarà pari a 5 si aggiungeranno valori randomici al set
        riga_unici.add(np.random.rand())
    
    data[i] = np.array(list(riga_unici)) #converto di nuovo il set in nparray e lo assegno alla riga i


#normalizzo i dati e li converto in interi
normalized_data = (data * 100).astype(int)

print(normalized_data)

#sovrappongo uno scatterplot per riga, dove come x ho il numero di riga e come y i valori all'interno della riga
plt.figure(figsize=(10, 6))
for i in range(data.shape[0]):
    plt.scatter([i]*5, data[i], label=f"Riga {i}")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.title('ScatterPlot della matrice')
plt.grid(True)
plt.tight_layout()
plt.show()
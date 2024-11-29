class Menu:
    def __init__(self):
        self.__elementi = [] 
    
    def aggiungi_elemento(self, elemento):
        #aggiunge un'opzione al menu.
        if isinstance(elemento, Elemento):
            self.__elementi.append(elemento)
        else:
            raise TypeError("L'elemento deve essere un'istanza della classe Elemento")

    def mostra_menu(self):
        #Mostra il menu e gestisce il ciclo while true e l'opzione di uscita.
        while True:
            print("\nMenu:")
            for i, elemento in enumerate(self.__elementi, start=1):
                print(f"{i}. {elemento.get_nome()}")
            print(f"{len(self.__elementi) + 1}. Esci")

            try:
                scelta = int(input("Seleziona il numero dell'opzione: "))
                
                if 1 <= scelta <= len(self.__elementi):
                    self.__elementi[scelta - 1].esegui_azione()
                elif scelta == len(self.__elementi) + 1:
                    print("Uscita dal menu.")
                    break
                else:
                    print("Scelta non valida. Riprova.")
            except ValueError:
                print("Per favore, inserisci un numero valido.")


class Elemento:
    def __init__(self, nome, azione=None):
        self.__nome = nome  
        self.__azione = azione  
    
    def get_nome(self):
        return self.__nome

    def esegui_azione(self):
        """Executes the action associated with this item."""
        if self.__azione:
            self.__azione.esegui()
        else:
            print(f"{self.__nome} non ha alcuna azione associata.")


class Azione:
    def __init__(self, funzione):
        self.__funzione = funzione  
    
    def esegui(self):
        """Executes the function associated with the action."""
        if callable(self.__funzione):
            self.__funzione()
        else:
            raise ValueError("L'azione deve essere una funzione chiamabile")

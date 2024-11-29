
#questa classe menù l'avevo già fatta, l'ho leggermente modificata per l'uso

class Menu:

    def __init__(self):

        self.__elementi = [] 
    
    def __set_elemento(self, elemento):

        self.__elementi.append(elemento)

    def aggiungi_elemento(self, elemento):

        if isinstance(elemento, Elemento):

            self.__set_elemento(elemento)
        else:
            print("L'elemento deve essere un'istanza della classe Elemento.")

    def mostra_menu(self):

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

    def get_azione(self):

        return self.__azione
    
    def esegui_azione(self):

        if self.get_azione():
            self.__azione.esegui()
        else:
            print(f"{self.get_nome} non ha alcuna azione associata.")


class Azione:

    def __init__(self, funzione):

        self.__funzione = funzione  
    
    def esegui(self):

        if callable(self.__funzione):
            self.__funzione()
        else:
            raise ValueError("L'azione deve essere una funzione chiamabile")

#classe libro con attributi nome, autore, anno, quantità che vengono richiesti al momento dell'inizializzazione dell'oggetto
class Libro:

    def __init__(self, nome = '', autore = '', anno = '', quantità = ''):

        if self.nome == '':

            self.nome = input("Inserisci il nome del libro: ")
        
        if self.autore == '':

            self.autore = input("Inserisci il nome dell'autore: ")
        
        if self.anno == '':

            self.anno = int(input("Inserisci l'anno di pubblicazione: "))
        
        if self.anno == '':

            self.quantià = int(input("Quante copie vuoi inserire in biblioteca?: "))

#classe biblioteca con 
class Biblioteca:

    def __init__(self):

        self.biblioteca = {}
    
    def aggiungi_libro(self, libro):

        if isinstance(libro, Libro):

            if libro.nome in self.biblioteca:

                choice = input("Libro già presente, vuoi aggiungerne altre copie? (y/n): ").lower()

                if choice == 'y' or 'yes':

                    numero = int(input("Quante copie vuoi aggiungerne?: "))

                    self.biblioteca[libro.nome].quantità += numero
            
            else:

                self.biblioteca[libro.nome] = libro

        else:

            print("L'elemento deve essere un'istanza della classe Libro.")


    def stampa(self):

        for libro in self.biblioteca:

            print(f'titolo: {libro.nome}\t autore: {libro.autore}\t anno: {libro.anno}\t copie presenti: {libro.quantità}')

    def cerca(self, titolo):

        for libro in self.biblioteca:

            if libro.nome == titolo:

                print("Libro presente.\n")
                print(f'titolo: {libro.nome}\t autore: {libro.autore}\t anno: {libro.anno}\t copie presenti: {libro.quantità}')

            else:

                print("Libro non presente in biblioteca.")

    def modifica(self, titolo):

        for libro in self.biblioteca:

            if libro.nome == titolo:

                scelta_autore = input("Vuoi modificare l'autore? (y/n): ").lower()

                if scelta_autore == "y" or "yes":

                    libro.autore = input("Inserisci un autore:")
                
                scelta_anno = input("Vuoi modificare l'anno? (y/n): ").lower()

                if scelta_anno == "y" or "yes":

                    libro.anno = int(input("Inserisci un anno:"))
                
                scelta_quantità = input("Vuoi modificare la quantità? (y/n): ").lower()

                if scelta_quantità == "y" or "yes":

                    libro.quantità = int(input("Inserisci una quantità:"))

#-------

def aggiungi_libro():

    libro = Libro()
    biblioteca.aggiungi_libro(libro)    

def stampa():

    biblioteca.stampa()   

def cerca():
    
    titolo = input("Inserisci il titolo del libro che vuoi cercare: ")
    biblioteca.cerca(titolo)  

def modifica():

    titolo = input("Inserisci il titolo del libro che vuoi modificare: ")
    biblioteca.modifica(titolo)


menu = Menu()
biblioteca = Biblioteca()


elemento1 = Elemento("Aggiungi un nuovo libro", Azione(aggiungi_libro))
elemento2 = Elemento("Visualizza tutta la biblioteca", Azione(stampa))
elemento3 = Elemento("Cerca un libro per titolo", Azione(cerca))
elemento4 = Elemento("Gestisci un libro per titolo", Azione(modifica))

menu.aggiungi_elemento(elemento1)
menu.aggiungi_elemento(elemento2)
menu.aggiungi_elemento(elemento3)
menu.aggiungi_elemento(elemento4)

# Mostra il menu ripetibile
menu.mostra_menu()
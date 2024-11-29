class Utente:

    def __init__(self, username, password, domanda_segreta):

        self.__username = username
        self.__password = password
        self.__domanda_segreta = domanda_segreta

    def __get_username(self):

        return self.__username
    
    def external__get_username(self):

        return self.__get_username()
    
    def __set_username(self, new_username):

        self.__username = new_username

    def external__set_username(self, new_username):

        self.__set_password(new_username)

    def __get_password(self):

        return self.__password
    
    def external__get_password(self):

        return self.__get_password()
    
    def __set_password(self, new_password):

        self.__password = new_password

    def external__set_password(self, new_password):

        self.__set_password(new_password)
       
    def __get_domanda_segreta(self):

        return self.__domanda_segreta
    
    def external__get_domanda_segreta(self):

        return self.__get_domanda_segreta()
    
    def __set_domanda_segreta(self, new_domanda_segreta):

        self.__domanda_segreta = new_domanda_segreta
    
    def _cambia_username(self):

        new_username = input("Inserisci uno username: ")

        self.__set_username(new_username)

    def _cambia_domanda_segreta(self):

        new_domanda_segreta = input("Qual è il nome delle tue elementari?: ").lower()

        self.__set_domanda_segreta(new_domanda_segreta)



class SistemaLogin:
    def __init__(self):
        # Dictionary to store registered users: key = username, value = Utente object
        self.utenti_registrati = {}

    def controlla_utente(self, username):
        """Checks if a username is already registered."""
        if username in self.utenti_registrati:
            print("L'username esiste già.")
            return True
        print("L'username è disponibile.")
        return False

    def crea_nuovo_utente(self, username, password, domanda_segreta):
        """Creates and registers a new user."""
        nuovo_utente = Utente(username, password, domanda_segreta)
        self.utenti_registrati[username] = nuovo_utente
        print("Registrazione completata con successo!")
        return True

    def effettua_login(self, username, password):
        """Performs login by verifying username existence and password."""
        utente = self.utenti_registrati.get(username)
        
        if not utente:
            print("Errore: Username non trovato.")
            return False
        
        if utente.external__get_password() != password:
            print("Errore: Password errata.")
            return False

        print("Login effettuato con successo!")
        return True

    def cambia_username(self, old_username, new_username):
        """Changes a user's username if the new one is available."""
        utente = self.utenti_registrati.get(old_username)
        
        if not utente:
            print("Errore: Username non trovato.")
            return False
        
        if new_username in self.utenti_registrati:
            print("Errore: Il nuovo username è già in uso.")
            return False
        
        utente.external__set_username(new_username)
        self.utenti_registrati[new_username] = utente
        del self.utenti_registrati[old_username]
        print("Username aggiornato con successo!")
        return True

    def reset_password(self, username):
        """Resets the password using the secret question."""
        utente = self.utenti_registrati.get(username)
        if not utente:
            print("Errore: Username non trovato.")
            return False
        
        risposta = input("Rispondi alla domanda segreta: Qual è il nome delle tue elementari?: ").lower()
        if risposta == utente.external__get_domanda_segreta():
            nuova_password = input("Inserisci la nuova password: ")
            utente.external__set_password(nuova_password)
            print("Password aggiornata con successo!")
            return True
        else:
            print("Risposta alla domanda segreta errata.")
            return False


# sistema = SistemaLogin()

# # Registrazione di un utente
# sistema.registra_utente("utente1", "password123", "scuola_elementare")

# # Login
# sistema.login("utente1", "password123")

# # Reset della password
# sistema.reset_password("utente1")

# # Cambia l'username
# sistema.cambia_username("utente1", "nuovo_utente1")


    


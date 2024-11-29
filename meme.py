class Mirko:

    def __init__(self):

        self.__nome = "Mirko"
        self.__cognome = "Campari"

    def __get_get_name(self):

        return self.__get_name()
    
    def __get_name(self):

        return self.__nome
    
    def __get_get_cognome(self):

        return self.__get_cognome()
    
    def __get_cognome(self):

        return self.__cognome

    def __get_stampa_info(self):

        print(f"nome: {self.__get_get_name()}, cognome: {self.__get_get_cognome()} ")

    def stampa(self):

        self.__get_stampa_info()



#-----------------------#

mirko = Mirko()

mirko.stampa()

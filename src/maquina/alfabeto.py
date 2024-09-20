# alfabeto.py
from sys import argv

class Alfabeto:
    # Métodos especiales
    def __init__(self, letras):
        self.letras = letras

    def __str__(self):
        return self.letras

    def __len__(self):
        return len(self.letras)

    def __getitem__(self, indice):
        return self.letras[indice]

    def __iter__(self):
        return iter(self.letras)

    def __contains__(self, letra):
        return letra in self.letras

    def __add__(self, otro):
        return self.letras + otro

    # Métodos normales
    def indexOf(self, letra):
        return self.letras.index(letra)

    def isValid(self, palabra):
        return all(letra in self.letras for letra in palabra)


def main():
    if __name__ == '__main__':
        if argv[1] == '--test':
            alfabeto = Alfabeto('abc')
            print("Alfabeto:", alfabeto)
            print("Longitud:", len(alfabeto))

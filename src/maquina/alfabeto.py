# alfabeto.py

from sys import argv, exit

class Alfabeto:
    '''
    private letras: str

    Encapsula la cadena del alfabeto, pero
    provee las funciones y accesos esenciales.

    Implementa además los métodos que definen el
    comportamiento que se requiere para el proyecto.
    '''

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
    def index(self, letra):
        return self.letras.index(letra)

    def isValid(self, palabra):
        return all(letra in self.letras for letra in palabra)

def test():
    '''Unit test'''

    alfabeto = Alfabeto('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    assert len(alfabeto) == 26
    assert alfabeto[0] == 'A'
    assert alfabeto[25] == 'Z'
    assert alfabeto.index('A') == 0
    assert alfabeto.index('Z') == 25
    assert 'A' in alfabeto
    assert 'Z' in alfabeto
    assert 'a' not in alfabeto
    assert 'z' not in alfabeto
    assert 'ABC' in alfabeto
    assert 'abc' not in alfabeto
    assert alfabeto + 'ABC' == 'ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
    assert str(alfabeto) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert len(alfabeto) == 26
    assert list(alfabeto) == list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

if __name__ == '__main__':
    argc = len(argv)
    if argc >= 2 and argv[1] == 'test':
        test()
    else:
        exit('Uso: python alfabeto.py [test]')

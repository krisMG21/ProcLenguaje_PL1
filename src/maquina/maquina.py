# maquina.py

from alfabeto import Alfabeto
from matriz import Matriz
from estados import Estados

class Maquina:
    def __init__(self, alfabeto : Alfabeto, matriz : Matriz, estados : list, inicial : int, finales : list):
        self.alfabeto = alfabeto
        self.matriz = matriz
        self.estados = Estados(estados, inicial, finales)
        self.estado = self.estados.get_inicial()

    def next_state(self, char):
        self.state = self.matriz[self.state][self.alfabeto.index(char)]

    def parse(self, texto):
        for char in texto:
            self.next_state(char)
        
        if self.estados.is_final(self.state):
            return True
        else:
            return False






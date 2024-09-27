# matriz.py
import json

from estados import Estados

class Matriz:
    '''
    private matriz: dict
    private estados: Estados

    Dado un archivo de expresiones, crea una matriz
    de estados así como los estados disponibles.

    Encapsula la matriz y provee de las funciones
    y accesos esenciales.
    '''

    def __init__(self, estados: Estados, expr_file: str):
        expr = json.load(open(expr_file))
        self.matriz = expr["matriz"]
        self.estados = estados

    def __getitem__(self, keyi):
        return self.matriz[keyi]

    def items(self):
        return self.matriz.items()


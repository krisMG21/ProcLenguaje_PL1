# matriz.py
import json

from estados import Estados

class Matriz:
    def __init__(self, estados: Estados, expr_file: str):
        expr = json.load(open(expr_file))
        self.matriz = expr["matriz"]
        self.estados = estados

    def __iter__(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                yield self.matriz[i][j]

    def __getitem__(self, key):
        return self.matriz[key]


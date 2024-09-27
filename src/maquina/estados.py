# estados.py

class Estados:
    # Métodos especiales
    def __init__(self, estados : list[int], inicial : int, finales : list[int]):
        self.estados = estados
        self.inicial = inicial
        self.finales = finales

    # Métodos normales
    def get(self):
        return self.estados

    def get_inicial(self):
        return self.inicial

    def is_final(self, estado : int):
        return estado in self.finales


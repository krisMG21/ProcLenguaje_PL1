# estados.py

class Estados:
    # Métodos especiales
    def __init__(self, ultimo_estado : int):
        self.estados = list(range(ultimo_estado))

    def __str__(self):
        return str(self.estados)

    def __len__(self):
        return len(self.estados)

    def __iter__(self):
        return iter(self.estados)

    def __contains__(self, estado):
        return estado in self.estados

    def __add__(self, otro):
        return self.estados.append(otro)

    # Métodos normales
    def get(self):
        return self.estados


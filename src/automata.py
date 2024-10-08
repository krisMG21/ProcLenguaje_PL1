# automata.py

import json

# ESTADOS ===================================================================


class Estados:
    """
    private estados: list[int]
    private inicial: int
    private finales: list[int]

    Dado un archivo de expresiones, crea una matriz
    de estados así como los estados disponibles.

    Encapsula los estados y provee de las funciones
    y accesos esenciales.
    """

    def __init__(self, estados: list[int], inicial: int, finales: list[int]):
        self.estados = estados
        self.inicial = inicial
        self.finales = finales

    def __str__(self):
        """Devuelve los estados como una cadena"""
        return (
            str(self.estados)
            + "\n Inicial: "
            + str(self.inicial)
            + "\n Finales: "
            + str(self.finales)
        )

    def get_inicial(self):
        """Devuelve el estado inicial"""
        return self.inicial

    def is_final(self, estado: int):
        """Devuelve si el estado es final"""
        return estado in self.finales


# MATRIZ ====================================================================


class Matriz:
    """
    private matriz: dict{"estado" : dict{letra : estado}}

    Contiene una matriz de estados y letras, implementada
    en forma de diccionario de diccionarios.

    Encapsula la matriz y provee de las funciones
    y accesos esenciales.
    """

    def __init__(self, matriz: dict):
        self.matriz = matriz
        self.estados = [int(estado) for estado in matriz.keys()]

        # Obtenemos el alfabeto completo desde la matriz
        alfabeto = set()

        for estado in self.matriz.values():
            alfabeto.update(letra for letra in estado.keys())

        self.alfabeto = str.join("", sorted(list(alfabeto)))

    def __getitem__(self, estado):
        """Para acceder de la forma matriz[estado][letra]"""
        return self.matriz[estado]

    def __str__(self):
        """Devuelve la matriz como una cadena tipo:
          a b c ... z
        0 1 3 _ ... _
        1 2 4 4 ... _
        2 _ 3 5 ... _
        . . . . ... .
        9 _ _ _ ... _
        """
        # Fila de letras
        cadena = "  " + " ".join(self.alfabeto) + " \n"

        # Recorremos la matriz
        for estado in self.estados:
            cadena += str(estado) + " "
            for letra in self.alfabeto:
                # Si no existe esa transición, se añade un '_' en su lugar
                try:
                    cadena += str(self.matriz[str(estado)][letra]) + " "
                except KeyError:
                    cadena += "_ "
            cadena += "\n"

        return cadena


class Automata:
    """Representa un autómata de una expresión regular"""

    def __init__(self, expr_json: str):
        """Carga los componentes de la maquina desde un json"""
        config = json.load(open(expr_json))
        self.matriz = Matriz(config["matriz"])
        self.estados = Estados(
            self.matriz.estados, config["inicial"], config["finales"]
        )
        self.expr = config["expresion"]
        self.state = config["inicial"]

    def get_alfabeto(self):
        """Devuelve el alfabeto"""
        return self.matriz.alfabeto

    def get_matriz(self):
        """Devuelve la matriz"""
        return self.matriz

    def get_estados(self):
        """Devuelve los estados de forma legible"""
        return self.estados

    def get_expr(self):
        """Devuelve la expresión"""
        return self.expr

    def get_state(self):
        """Devuelve el estado actual"""
        return self.state

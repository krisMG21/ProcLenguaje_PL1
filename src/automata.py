# automata.py

import json

# ESTADOS ===================================================================

class Estados:
    '''
    private estados: list[int]
    private inicial: int
    private finales: list[int]

    Dado un archivo de expresiones, crea una matriz
    de estados así como los estados disponibles.

    Encapsula la matriz y provee de las funciones
    y accesos esenciales.
    '''

    def __init__(self, estados : int, inicial : int, finales : list[int]):
        self.estados = list(range(estados))
        self.inicial = inicial
        self.finales = finales

    def __str__(self):
        '''Devuelve los estados como una cadena'''
        return str(self.estados) + \
            '\n Inicial: ' + str(self.inicial) + \
            '\n Finales: ' + str(self.finales)

    def get_inicial(self):
        '''Devuelve el estado inicial'''
        return self.inicial

    def is_final(self, estado : int):
        '''Devuelve si el estado es final'''
        return estado in self.finales

# MATRIZ ====================================================================

class Matriz:
    '''
    private matriz: dict{"estado" : dict{letra : estado}}

    Contiene una matriz de estados y letras, que en realidad
    es un diccionario de diccionarios.

    Encapsula la matriz y provee de las funciones
    y accesos esenciales.
    '''

    def __init__(self, alfabeto : str, matriz: dict):
        self.matriz = matriz
        self.estados = matriz.keys()
        self.alfabeto = alfabeto

    def __getitem__(self, i):
        '''Para acceder de la forma matriz[estado][letra]'''
        return self.matriz[i]

    def __str__(self):
        '''Devuelve la matriz como una cadena tipo:
              a b c ... z
            0 1 3 _ ... _
            1 2 4 4 ... _
            2 _ 3 5 ... _
            . . . . ... .
            9 _ _ _ ... _
        '''
        # Fila de letras
        cadena = '  ' + ' '.join(self.alfabeto) + ' \n'

        # Recorremos la matriz
        for estado in self.estados:
            cadena += str(estado) + ' '
            for letra in self.alfabeto:
                # Si no existe esa transición, se añade un '_' en su lugar
                try:
                    cadena += str(self.matriz[estado][letra]) + ' '
                except KeyError:
                    cadena += '_ '
            cadena += '\n'

        return cadena

class Automata:
    ''' Representa un autómata de una expresión regular '''

    def __init__(self, expr_json : str):
        '''Carga los componentes de la maquina desde un json'''
        config = json.load(open(expr_json))
        self.estados = Estados(
            config['estados'],
            config['inicial'],
            config['finales'])
        self.alfabeto = config['alfabeto']
        self.matriz = Matriz(config['alfabeto'], config['matriz'])
        self.expr = config['expresion']

    def get_alfabeto(self):
        '''Devuelve el alfabeto'''
        return self.alfabeto

    def get_matriz(self):
        '''Devuelve la matriz'''
        return self.matriz

    def get_estados(self):
        '''Devuelve los estados de forma legible'''
        return self.estados

    def get_expr(self):
        '''Devuelve la expresión'''
        return self.expr

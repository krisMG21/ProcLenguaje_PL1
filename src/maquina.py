# maquina.py

import json

# ALFABETO ==================================================================
class Alfabeto:
    '''
    private letras: str

    Encapsula la cadena del alfabeto, pero
    provee las funciones y accesos esenciales.

    Implementa además los métodos que definen el
    comportamiento que se requiere para el proyecto.
    '''

    def __init__(self, letras : str):
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

    def index(self, letra):
        return self.letras.index(letra)

    def isValid(self, palabra):
        return all(letra in self.letras for letra in palabra)



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

    def __init__(self, estados : list[int], inicial : int, finales : list[int]):
        self.estados = estados
        self.inicial = inicial
        self.finales = finales

    def get(self):
        '''Devuelve los estados'''
        return self.estados

    def get_inicial(self):
        '''Devuelve el estado inicial'''
        return self.inicial

    def is_estado(self, estado : int):
        '''Devuelve si el estado es válido'''
        return estado in self.estados

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
        self.alfabeto = alfabeto
        self.matriz = matriz
        self.estados = matriz.keys()

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

        # Estado actual + siguientes estados
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

    def transition(self, estado : int, letra : str):
        try:
            return self.matriz[str(estado)][letra]
        except KeyError:
            return None



# MAQUINA ===================================================================

class Maquina:
    '''
    private alfabeto: Alfabeto
    private matriz: Matriz
    private estados: Estados
    private estado: int

    Una vez se crea con acceso a los datos de la expresión,
    permite realizar el parseo de una cadena de texto, evaluando
    el estado de la maquina en cada paso y determinando si la
    cadena de texto es válida o no.
    '''

    def __init__(self, json_file : str):
        '''Constructor de la maquina directamente desde un json'''

        config = json.load(open(json_file))
        self.expr = config["expresion"]
        self.alfabeto = Alfabeto(config["alfabeto"])
        self.estados = Estados(
            list(range(config["estados"])),
            config["inicial"],
            config["finales"])
        self.matriz = Matriz(config["alfabeto"], config["matriz"])
        self.state = self.estados.get_inicial()

    def reset(self):
        self.state = self.estados.get_inicial()

    def get_state(self):
        '''Devuelve el estado actual'''
        return self.state

    def get_matriz(self):
        '''Devuelve la matriz'''
        return self.matriz

    def get_estados(self):
        '''Devuelve los estados'''
        return self.estados.get()

    def get_alfabeto(self):
        '''Devuelve el alfabeto'''
        return str(self.alfabeto)

    def get_expr(self):
        '''Devuelve la expresión'''
        return self.expr

    def next_state(self, char):
        '''Siguiente estado de la maquina, devuelve si la transición es válida o no'''

        try: 
            self.state = self.matriz[str(self.state)][char]
        except KeyError:
            self.state = -1 # Estado de error
            return False

        return True


    def parse(self, texto : str, steps : bool = False):
        '''Devuelve una lista de los estados por los que
        pasa la máquina mientras procesa el texto'''

        if not texto:
            return [] if steps else False

        transitions = []
        for i, char in enumerate(texto):

            if steps:
                next_state = self.matriz.transition(self.state, char)
                transitions.append((self.state, char, next_state))

            if not self.next_state(char):
                break

        parsed_correctly = (i == len(texto) - 1) and self.estados.is_final(self.state)
        self.reset()

        return transitions if steps else parsed_correctly


    def generate(self, n: int, max_len: int):
        '''Genera n cadenas validas para la expresión, de longitud maxima len'''

        def generate_all(cadena=''):
            if len(cadena) <= max_len:
                if self.parse(cadena):
                    yield cadena
                if len(cadena) < max_len:
                    for letra in self.alfabeto:
                        yield from generate_all(cadena + letra)

        count = 0
        for palabra in generate_all():
            if count >= n:
                break
            yield palabra
            count += 1

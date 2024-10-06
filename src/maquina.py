# maquinapy

from automata import Automata

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

    def __init__(self, automata : Automata):
        '''Carga los componentes de la maquina desde un json, e inicializa el estado actual'''
        self.automata = automata
        self.estados = self.automata.get_estados()
        self.matriz = self.automata.get_matriz()
        self.alfabeto = self.automata.get_alfabeto()
        self.state = self.estados.get_inicial()

    def reset(self):
        self.state = self.estados.get_inicial()

    def peek_state(self, state: int, char: str):
        '''Devuelve el estado siguiente, sin cambiar el estado de la maquina'''

        try:
            return self.matriz[str(state)][char]
        except KeyError:
            return -1 # Estado de error

    def next_state(self, char: str):
        '''Avanza al siguiente estado de la maquina, devuelve el nuevo estado'''

        self.state = self.peek_state(self.state, char)

        return self.state

    def get_state(self):
        '''Devuelve el estado actual'''
        return self.state

    def get_matriz(self):
        '''Devuelve la matriz'''
        return self.automata.get_matriz()

    def get_estados(self):
        '''Devuelve los estados de forma legible'''
        return self.automata.get_estados()

    def get_alfabeto(self):
        '''Devuelve el alfabeto'''
        return self.automata.get_alfabeto()

    def get_expr(self):
        '''Devuelve la expresión'''
        return self.automata.get_expr()

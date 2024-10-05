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
        self.state = automata.get_inicial()

    def reset(self):
        self.state = self.automata.get_inicial()


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


    def parse(self, texto : str):
        '''Devuelve una lista de los estados por los que
        pasa la máquina mientras procesa el texto
        '''

        i = 0
        # Iteramos sobre el texto
        for i, char in enumerate(texto):
            if self.next_state(char) == -1:
                break

        # Es válida si ha procesado toda la cadena y ha llegado al estado final
        parsed_correctly = (i == len(texto) - 1) and self.estados.is_final(self.state)
        self.reset()

        return parsed_correctly

    def trace(self, texto : str):
        ''' Devuelve una lista de las transiciones por las que ha pasado la cadena'''

        transitions = []
        for char in texto:
            transitions.append((self.state, char, self.next_state(char)))

        # Proceso parecido a parse, pero sigue la traza aun por estados de error

        self.reset()

        return transitions

    def generate_all(self, max_len: int):
        '''Devuelve un generador de cadenas validas para la expresión, de longitud maxima len'''

        assert max_len > 0, 'La longitud máxima debe ser mayor que 0'

        def generator(cadena='', state=self.estados.get_inicial(), len = 0):
            # Si el estado es final, devuelve la cadena
            if self.estados.is_final(state):
                yield cadena

            # Si no ha alcanzado la longitud máxima, sigue probando letras
            if len < max_len:
                for letra in self.alfabeto:
                    next_state = self.peek_state(state, letra)
                    if next_state != -1:
                        yield from generator(cadena + letra, next_state, len + 1)

        return generator()


    def generate(self, n: int, max_len: int):
        '''Genera n cadenas validas para la expresión, de longitud maxima len'''

        count = 0

        # Iteramos sobre la función de generación
        for palabra in self.generate_all(max_len):
            if count >= n:
                break
            yield palabra
            count += 1

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

    def get_config(self):
        '''Devuelve la configuración de la maquina'''
        return self.automata.get_config()

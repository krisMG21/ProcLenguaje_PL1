# main.py
from sys import argv
from automata import Automata
from maquina import Maquina
from consola import iniciar_consola


def parse(maquina : Maquina, texto : str):
    '''Devuelve una lista de los estados por los que
    pasa la máquina mientras procesa el texto
    '''
    i = 0
    # Iteramos sobre el texto
    for i, char in enumerate(texto):
        if maquina.next_state(char) == -1:
            break
    # Es válida si ha procesado toda la cadena y ha llegado al estado final
    parsed_correctly = (i == len(texto) - 1) and maquina.estados.is_final(maquina.state)
    maquina.reset()

    return parsed_correctly

def trace(maquina : Maquina, texto : str):
    ''' Devuelve una lista de las transiciones por las que ha pasado la cadena'''

    transitions = []
    for char in texto:
        transitions.append((maquina.state, char, maquina.next_state(char)))

    # Proceso parecido a parse, pero sigue la traza aun por estados de error

    maquina.reset()

    return transitions

def generate_all(maquina : Maquina, max_len: int):
    '''Devuelve un generador de cadenas validas para la expresión, de longitud maxima len'''

    assert max_len > 0, 'La longitud máxima debe ser mayor que 0'

    def generator(cadena='', state=maquina.estados.get_inicial(), len = 0):
        # Si el estado es final, devuelve la cadena
        if maquina.estados.is_final(state):
            yield cadena
        # Si no ha alcanzado la longitud máxima, sigue probando letras
        if len < max_len:
            for letra in maquina.alfabeto:
                next_state = maquina.peek_state(state, letra)
                if next_state != -1:
                    yield from generator(cadena + letra, next_state, len + 1)

    return generator()


def generate(maquina : Maquina, n: int, max_len: int):
    '''Genera n cadenas validas para la expresión, de longitud maxima len'''

    count = 0

    # Iteramos sobre la función de generación
    for palabra in generate_all(maquina, max_len):
        if count >= n:
            break
        yield palabra
        count += 1


def main():
    expr_file = argv[1] # Tomamos como argumento el archivo de la expresión
    automata = Automata(expr_file) # Cargamos la expresión
    maquina = Maquina(automata) # Creamos la maquina

    # Se la pasamos a la consola para interactuar con ella
    # así como las funciones de parseo, traza y generación
    iniciar_consola(maquina) 

if __name__ == '__main__':
    main()

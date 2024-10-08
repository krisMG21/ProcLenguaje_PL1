from maquina import Maquina


def maq_parse(maquina: Maquina, texto: str):
    """Devuelve una lista de los estados por los que
    pasa la máquina mientras procesa el texto
    """
    i = 0
    estados = maquina.get_estados()

    # Iteramos sobre el texto
    for i, char in enumerate(texto):
        if maquina.next_state(char) == -1:
            break
    # Es válida si ha procesado toda la cadena y ha llegado al estado final
    parsed_correctly = (i == len(texto) - 1) and estados.is_final(maquina.state)
    maquina.reset()

    return parsed_correctly


def maq_trace(maquina: Maquina, texto: str):
    """Devuelve una lista de las transiciones por las que ha pasado la cadena"""

    transitions = []
    for char in texto:
        transitions.append((maquina.get_state(), char, maquina.next_state(char)))

    # Proceso parecido a parse, pero sigue la traza aun por estados de error

    maquina.reset()

    return transitions


def maq_generate_all(maquina: Maquina, max_len: int):
    """Devuelve un generador de cadenas validas para la expresión, de longitud maxima len"""

    estados = maquina.get_estados()
    alfabeto = maquina.get_alfabeto()

    assert max_len > 0, "La longitud máxima debe ser mayor que 0"

    def generator(cadena="", state=estados.get_inicial(), len=0):
        # Si el estado es final, devuelve la cadena
        if estados.is_final(state):
            yield cadena
        # Si no ha alcanzado la longitud máxima, sigue probando letras
        if len < max_len:
            for letra in alfabeto:
                next_state = maquina.peek_state(state, letra)
                if next_state != -1:
                    yield from generator(cadena + letra, next_state, len + 1)

    return generator()


def maq_generate(maquina: Maquina, n: int, max_len: int):
    """Genera n cadenas validas para la expresión, de longitud maxima len"""

    # Iteramos sobre la función de generación
    for i, palabra in enumerate(maq_generate_all(maquina, max_len)):
        if i >= n:
            break
        yield palabra

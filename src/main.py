# main.py
# import readline
from sys import argv
from maquina import Automata, Maquina
from funciones import maq_parse, maq_trace, maq_generate, maq_generate_all

import readline

readline.set_history_length(100)


def help():
    print("Funciones disponibles:")
    print(
        "-parse(str): Devuelve una lista de los estados por los que pasa la máquina mientras procesa el texto"
    )
    print(
        "-trace(str): Devuelve una lista de las transiciones por las que ha pasado la cadena"
    )
    print(
        "-generate(n, m): Genera n cadenas validas para la expresión, de longitud maxima len"
    )
    print(
        "-generate_all(n): Devuelve un generador de cadenas validas para la expresión, de longitud maxima len"
        + "=" * 50
    )
    print(
        "-next_state(char): Devuelve el siguiente estado de la máquina para el caracter char"
    )
    print(
        "-peek_state(state, char): Devuelve el siguiente estado de la máquina para el caracter char en el estado state"
    )
    print("-get_expr(): Devuelve la expresión de la máquina")
    print("-get_estados(): Devuelve el conjunto de estados de la máquina")
    print("-get_alfabeto(): Devuelve el alfabeto de la máquina")
    print("-get_matriz(): Devuelve la matriz de la máquina")
    print("-get_state(): Devuelve el estado actual de la máquina")
    print("-reset(): Reinicia la máquina")


def execute_and_print(maquina: Maquina, command):
    """
    Dada una maquina y una expresión maquina.funcion()
    ejecuta la función e imprime el resultado, de seguido o por elementos
    """

    # Generan avisos pq no se usan en código, sólo en ejecución
    def parse(texto):
        return maq_parse(maquina, texto)

    def trace(texto):
        return maq_trace(maquina, texto)

    def generate(n, m):
        return maq_generate(maquina, n, m)

    def generate_all(n):
        return maq_generate_all(maquina, n)

    # Probamos a evaluar el comando, si es del main, lo ejecutamos tal cual
    try:
        result = eval(command)
    except Exception:
        result = eval(f"maquina.{command}")

    # Imprime elem a elem si es iterable, a menos que sea str
    if hasattr(result, "__iter__") and not isinstance(result, str):
        for i in result:
            print(i)
    # Si no se imprime tal cual
    elif result is not None:
        print(result)


def iniciar_consola(maquina):
    """
    Inicia la consola interactiva para interactuar con la maquina
    """
    import sys
    import traceback

    # Borramos la pantalla y posicionamos el cursor en la posición 1,1
    print("\033[2J\033[0;0H")
    print("Expresion: " + maquina.get_expr() + "\n")
    print("Matriz:\n" + str(maquina.get_matriz()) + "\n")
    print("Try parse(str), generate(n, m) or next_state(char), or help for more info\n")

    texto = ""
    while texto != "exit":
        try:
            texto = input("> ")
            match texto:
                case "help":
                    help()
                case "clear":
                    # Codigo ANSI para borrar la pantalla y posicionar
                    # el cursor en la posición 1,1
                    print("\033[2J\033[1;1H")
                case "exit":
                    break
                case _:
                    execute_and_print(maquina, texto)
        #
        # except AttributeError:
        #     print('Esa función no existe')

        except KeyboardInterrupt:
            print("\n")

        except Exception as e:
            print(e)


def main():
    expr_file = argv[1]  # Tomamos como argumento el archivo de la expresión
    automata = Automata(expr_file)  # Cargamos la expresión
    maquina = Maquina(automata)  # Creamos la maquina

    # Se la pasamos a la consola para interactuar con ella
    # así como las funciones de parseo, traza y generación
    iniciar_consola(maquina)


if __name__ == "__main__":
    main()

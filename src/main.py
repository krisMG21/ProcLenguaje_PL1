# main.py
import readline
from sys import argv
from automata import Automata
from maquina import Maquina
from funciones import maq_parse, maq_trace, maq_generate, maq_generate_all, help

# Recuperamos el historial (si existe)
histfile = ".myhistory"
try:
    readline.read_history_file(histfile)
except FileNotFoundError:
    pass

readline.set_history_length(100)


def execute_and_print(maquina, command):
    """
    Dada una maquina y una expresión maquina.funcion()
    ejecuta la función e imprime el resultado, de seguido o por elementos
    """

    def parse(texto):
        maq_parse(maquina, texto)

    def trace(texto):
        maq_trace(maquina, texto)

    def generate(n, m):
        maq_generate(maquina, n, m)

    def generate_all(n):
        maq_generate_all(maquina, n)

    # Probamos a evaluar el comando, si es del main, lo ejecutamos tal cual
    try:
        result = eval(command)
    except AttributeError:
        print("Esa función no existe")
        return

    # Imprimimos el resultado en pantalla de forma legible
    if hasattr(result, "__iter__") and not isinstance(result, str):
        for i in result:
            print(i)
    elif result is not None:
        print(result)


def iniciar_consola(maquina):
    """
    Inicia la consola interactiva para interactuar con la maquina
    """

    # Borramos la pantalla y posicionamos el cursor en la posición 1,1
    print("\033[2J\033[0;0H")
    print("Expresion: " + maquina.get_expr() + "\n")
    print("Matriz:\n" + str(maquina.get_matriz()) + "\n")
    print("Try parse(str), generate(n, m) or next_state(char), or help for more info")

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

    readline.write_history_file(histfile)


def main():
    expr_file = argv[1]  # Tomamos como argumento el archivo de la expresión
    automata = Automata(expr_file)  # Cargamos la expresión
    maquina = Maquina(automata)  # Creamos la maquina

    # Se la pasamos a la consola para interactuar con ella
    # así como las funciones de parseo, traza y generación
    iniciar_consola(maquina)


if __name__ == "__main__":
    main()

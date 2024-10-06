import readline


''' ¿Como funciona readline?

Una vez inicializado, se integra con la función input() de python,
intercepta entradas (en nuestro caso interesan flecha de arriba y flecha de abajo)
y se mueve entre los inputs anteriores, mostrándolas en pantalla.

Podemos incluso guardar el historial y recuperarlo la siguiente sesión.
En nuestro caso, guardamos en un archivo llamado .myhistory
'''

# Recuperamos el historial (si existe)
histfile = ".myhistory"
try:
    readline.read_history_file(histfile)
except FileNotFoundError:
    pass

readline.set_history_length(100)



def help():
    print('Funciones disponibles:\n\n' + \
        '·help: Muestra esta ayuda\n\n' + \
        '·clear: Limpia la pantalla\n\n' + \
        '·parse(str): Parsea una cadena para ver si es válida según la expresión\n\n' + \
        '·parse(str, True): Parsea una cadena para ver si es válida según la expresión' + \
        'y devuelve las transiciones realizadas\n\n' + \
        '·generate(n, m): Genera hasta n cadenas de longitud m\n\n' + \
        '·generate_all(m): Genera todas las cadenas posibles de longitud m\n\n' + \
        '·next_state(char): Avanza al siguiente estado dado un caracter\n\n' + \
        '·get_state(): Devuelve el estado actual de la maquina\n\n' + \
        '·get_matriz(): Devuelve la matriz de la maquina\n\n' + \
        '·get_estados(): Devuelve los estados de la maquina\n\n' + \
        '·get_expr(): Devuelve la expresión de la maquina\n\n' + \
        '·get_alfabeto(): Devuelve el alfabeto de la maquina\n\n' + \
        '·reset(): Reinicia el estado de la maquina (no necesario con parse(str) o generate(n, m))\n\n' + \
        '·exit: Salir del programa')

def execute_and_print(maquina, command):
    ''' 
    Dada una maquina y una expresión maquina.funcion()
    ejecuta la función e imprime el resultado, de seguido o por elementos
    '''
    # Probamos a evaluar el comando, si es del main, lo ejecutamos tal cual
    try:
        result = eval(command)
    except AttributeError:
    # Y si no, probamos a evaluar como una función de la maquina
        try: 
            result = eval('maquina.' + command)
        except AttributeError:
            print('Esa función no existe')
            return

    # Imprimimos el resultado en pantalla de forma legible
    if hasattr(result, '__iter__') and not isinstance(result, str):
        for i in result:
            print(i)
    elif result is not None:
        print(result)

def iniciar_consola(maquina):
    '''
    Inicia la consola interactiva para interactuar con la maquina
    '''

    print('\033[2J\033[0;0H') # Borramos la pantalla y posicionamos el cursor en la posición 1,1
    print('Expresion: ' + maquina.get_expr() + '\n')
    print('Matriz:\n' + str(maquina.get_matriz()) + '\n')
    print('Try parse(str), generate(n, m) or next_state(char), or help for more info')

    texto = ''
    while texto != 'exit':
        try:
            texto = input('> ')
            match texto:
                case 'help':
                    help()
                case 'clear':
                    # Codigo ANSI para borrar la pantalla y posicionar
                    # el cursor en la posición 1,1
                    print('\033[2J\033[1;1H')                 
                case 'exit':
                    break
                case _:
                    execute_and_print(maquina, texto)
        #
        # except AttributeError:
        #     print('Esa función no existe')

        except KeyboardInterrupt:
            print('\n')

        except Exception as e:
            print(e)

    readline.write_history_file(histfile)

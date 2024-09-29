# main.py
from sys import argv
from maquina import Maquina

def help():
    print('Funciones disponibles:\n\n' + \
        '·help(): Muestra esta ayuda\n\n' + \

        '·parse(): Parsea una cadena para ver si es válida' + \
        ' según la expresión\n\n' + \

        '·generate(n, m): Genera hasta n cadenas de longitud m\n\n' + \

        '·next_state(char): Avanza al siguiente estado dado un caracter\n\n' + \

        '·get_state(): Devuelve el estado actual de la maquina\n\n' + \

        '·get_matriz(): Devuelve la matriz de la maquina\n\n' + \

        '·get_estados(): Devuelve los estados de la maquina\n\n' + \

        '·get_alfabeto(): Devuelve el alfabeto de la maquina\n\n' + \

        '·reset(): Reinicia el estado de la maquina (no necesario con parse(str)' + \
        'o generate(n, m))\n\n' + \

        '·exit: Salir del programa'
    )

def main():
    # Cargar maquina desde archivo
    expr_file = argv[1]
    maquina = Maquina(expr_file)

    # Visualización de la matriz
    print('Matriz:\n' + str(maquina.get_matriz()))

    # Bucles de usuario
    print('Try parse(str), generate(n, m) or next_state(char), or help() for more info')

    texto = ''
    while texto != 'exit':
        texto = input('> ')
        match input('> ').lower():
            case 'help':
                help()
            case 'exit':
                break
            case _:
                try:
                    exec('maquina.' + texto)
                except AttributeError:
                    print('No existe esa función')
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    main()

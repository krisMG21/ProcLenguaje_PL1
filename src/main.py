# main.py
from sys import argv
from automata import Automata
from maquina import Maquina
from consola import iniciar_consola

def main():
    expr_file = argv[1] # Tomamos como argumento el archivo de la expresión
    automata = Automata(expr_file) # Cargamos la expresión
    maquina = Maquina(automata) # Creamos la maquina
    iniciar_consola(maquina) # Se la pasamos a la consola para interactuar con ella

if __name__ == '__main__':
    main()

# main.py
import json
from sys import argv
from maquina.maquina import Maquina

def main():
    expr_file = argv[1]
    with open(expr_file) as f:
        expr = json.load(f)

    maquina = Maquina(
        expr["alfabeto"],
        expr["matriz"],
        expr["estados"],
        expr["inicial"],
        expr["finales"]
    )

    texto = ''
    while texto != 'exit':
        texto = input('> ')
        if maquina.parse(texto):
            print('Aceptado')
        else:
            print('Rechazado')

if __name__ == '__main__':
    main()

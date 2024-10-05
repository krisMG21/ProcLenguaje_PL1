# main.py
from sys import argv

def main():
    num_estados = int(argv[1])
    inicial = int(argv[2])
    finales = argv[3].split(',')
    alfabeto = argv[4]
    matriz = argv[5]
    expresion = argv[6]

    print(num_estados)
    print(inicial)
    print(finales)
    print(alfabeto)
    print(matriz)
    print(expresion)


if __name__ == '__main__':
    main()

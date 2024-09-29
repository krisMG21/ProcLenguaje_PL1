import json

from maquina import Alfabeto, Estados, Matriz, Maquina

config = json.load(open('test.json'))

def alfabeto_test():
    '''Alfabeto unit testing'''

    alfabeto = Alfabeto('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    alfabeto = Alfabeto('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    assert alfabeto[25] == 'Z'
    assert alfabeto.index('A') == 0
    assert alfabeto.index('Z') == 25
    assert 'A' in alfabeto
    assert 'Z' in alfabeto
    assert 'a' not in alfabeto
    assert 'z' not in alfabeto
    assert 'ABC' in alfabeto
    assert 'abc' not in alfabeto
    assert alfabeto + 'ABC' == 'ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
    assert str(alfabeto) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert len(alfabeto) == 26
    assert list(alfabeto) == list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def estados_test():
    '''Estados unit testing'''

    estados = Estados([0, 1, 2], 0, [2])
    assert estados.get_inicial() == 0
    assert estados.is_estado(1)
    assert not estados.is_estado(3)
    assert estados.is_final(2)
    assert not estados.is_final(1)

def matriz_test():
    '''Matriz unit testing'''
    matriz = Matriz(config["alfabeto"], config["matriz"])

    assert matriz["0"] == {"a" : 1}
    assert matriz["1"] == {"a" : 3, "b" : 2}
    assert matriz["2"] == {"b" : 4, "c" : 5}
    assert matriz["3"] == {"a" : 3, "b" : 2}
    assert matriz["4"] == {"b" : 4, "c" : 5}
    assert matriz["5"] == {"c" : 5}


    print(matriz)

    assert str(matriz) == '  a b c\n0 1 _ _\n1 3 2 _\n2 _ 4 5\n3 3 2 _\n4 _ 4 5\n5 _ _ 5\n'


def maquina_test():
    '''Maquina unit testing'''

    maquina = Maquina('test.json')

    for cadena in maquina.parse('abc', True):
        print(cadena)

    assert maquina.parse('abc')
    assert maquina.parse('aabbc')
    assert not maquina.parse('abca')
    assert not maquina.parse('abcabc')

     # Para cualquier caso, no hay mas de n palabras, con no mas de m caracteres
    n = 100
    m = 10

    for i, cadena in enumerate(maquina.generate(n, m)):
        assert len(cadena) <= m
        assert maquina.parse(cadena)
    assert i <= n


def main():
    '''Main function'''
    try:
        alfabeto_test()
        estados_test()
        matriz_test()
        maquina_test()
    except AssertionError as e:
        raise e
    else:
        print("Tests passed")
        exit(0)

if __name__ == '__main__':
    main()

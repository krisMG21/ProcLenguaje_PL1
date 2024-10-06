import json
import pytest
from automata import Estados, Matriz, Automata
from maquina import Maquina
from main import parse, trace, generate, generate_all

@pytest.fixture
def config():
    return json.load(open('test.json'))

def test_estados():
    estados = Estados([0, 1, 2, 3], 0, [2])
    assert estados.inicial == 0
    assert estados.is_final(2)
    assert not estados.is_final(1)

def test_matriz(config):
    matriz = Matriz(config["matriz"])

    assert matriz["0"] == {"a": 1}
    assert matriz["1"] == {"a": 1, "b": 2}
    assert matriz["2"] == {"b": 2, "c": 3}
    assert matriz["3"] == {}

    assert matriz.alfabeto == 'abc'
    assert matriz.estados == [0, 1, 2, 3]

    expected_str = (
        '  a b c \n'
        '0 1 _ _ \n'
        '1 1 2 _ \n'
        '2 _ 2 3 \n'
        '3 _ _ _ \n'
    )
    assert str(matriz) == expected_str

def test_automata(config):
    automata = Automata('test.json')
    assert automata.estados.estados == [0, 1, 2, 3]
    assert automata.estados.get_inicial() == 0
    assert automata.estados.is_final(3)
    assert not automata.estados.is_final(1)
    assert automata.matriz.matriz == config["matriz"]
    assert automata.expr == 'aa*bb*c'
    assert automata.estados.estados == automata.matriz.estados

def test_maquina():
    automata = Automata('test.json')
    maquina = Maquina(automata)

    assert maquina.next_state('a') == 1
    assert maquina.next_state('b') == 2
    assert maquina.next_state('c') == 3
    assert maquina.next_state('d') == -1

    maquina.reset()
    assert maquina.get_state() == 0

    assert maquina.peek_state(0, 'a') == 1
    assert maquina.peek_state(1, 'a') == 1
    assert maquina.peek_state(1, 'b') == 2
    assert maquina.peek_state(2, 'b') == 2
    assert maquina.peek_state(2, 'c') == 3
    assert maquina.peek_state(3, 'c') == -1
    assert maquina.peek_state(3, 'd') == -1

def test_main():
    maquina = Maquina(Automata('test.json'))
    # Comprobamos que la consola funciona
    assert parse(maquina, 'abc')
    assert parse(maquina, 'aabbc')
    assert not parse(maquina, 'abca')
    assert not parse(maquina, 'abcabc')

    assert trace(maquina, 'abc') == [
        (0, 'a', 1),
        (1, 'b', 2),
        (2, 'c', 3)
    ]
    assert trace(maquina, 'aabbc') == [
        (0, 'a', 1),
        (1, 'a', 1),
        (1, 'b', 2),
        (2, 'b', 2),
        (2, 'c', 3)
    ]
    assert trace(maquina, 'abca') == [
        (0, 'a', 1),
        (1, 'b', 2),
        (2, 'c', 3),
        (3, 'a', -1)
    ]
    assert trace(maquina, 'error') == [
        (0, 'e', -1),
        (-1, 'r', -1),
        (-1, 'r', -1),
        (-1, 'o', -1),
        (-1, 'r', -1)
    ]

    # Para cualquier caso, no hay mas de n palabras, con no mas de m caracteres
    n = 100
    m = 10

    # Comprobamos que todas las cadenas son válidas y no exceden ni n ni m
    generated = list(generate(maquina, n, m))
    assert len(generated) <= n
    for cadena in generated:
        assert len(cadena) <= m
        assert parse(maquina, cadena)

    generated = list(generate_all(maquina, m))
    for cadena in generated:
        assert len(cadena) <= m
        assert parse(maquina, cadena)


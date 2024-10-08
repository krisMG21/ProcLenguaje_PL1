# PL1 - Procesadores del lenguaje

Éste autómata de estados / parser, está implementado de forma compacta y modular:

* main.py: programa principal, contiene el bucle de ejecución y accede únicamente
a la clase Maquina para realizar operaciones

La ejecución del programa se realiza de este modo:

```bash
python3 main.py <archivo_json>
```

Donde `<archivo_json>` es el nombre del archivo .json con los
datos de la expresión.

* automata.py: Define el autómata, así como sus componentes:
  * Matriz: contiene la matriz de transición y el control de acceso a ella
  * Estados: estados disponibles, inicial y finales
  * Automata: contiene toda la información que se pueda requerir de un
    autómata finito

* maquina.py: implementa Maquina y los principales componentes de ella:

  * Maquina: implementa la maquina, que contiene el correspondiente
    autómata, así como el estado actual y la lógica de estados

* test_all.py: Conjunto de tests para todas las clases y todas sus funcionalidades
Para ejecutar los test, no es necesario ningún tipo de argumento:

```bash
pytest
```

* template.py:

## Ejemplo de uso

Para ejecutar el programa, se debe crear un archivo .json con los datos
de la expresión. El formato del archivo debe ser como el del siguiente ejemplo:

```json
{
    "expresion": "ab(c)*...",
    "alfabeto": "abcd...",
    "estados": 6,
    "inicial": 0,
    "finales": [
        1,
        2,
        3
    ],
    "matriz": {
        "0": {"a": 1},
        "1": {"a": 3, "b": 2},
        "2": {"b": 4, "c": 5},
        "3": {"a": 3, "b": 2},
        "4": {"b": 4, "c": 5},
        "5": {"c": 5}
    }
```
* expresion: Expresión regular en formato JFLAPS, haciendo uso solo de (), + y *
* alfabeto --> maquina.Alfabeto
* estados --> Número de estados disponibles
* inicial, finales
* matriz --> Matriz de transiciones, diccionario de la forma {"curr_state" : {"char": next_state}}
  realizados a partir del AFD minimizado.

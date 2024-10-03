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

* maquina.py: implementa Maquina y los principales componentes de ella:

  * Alfabeto: conjunto de caracteres válidos, operaciones de string +
  validación de caracteres

  * Estados: contiene todos los estados, especificando cuál es el inicial y
    cuáles los finales.
    Contiene métodos para contrastar cualquier estado los conjuntos anteriores.

  * Matriz: implementa la matriz de transiciones.
    Contiene acceso por `[estado][letra]` o por la función `self.transition(estado,
    letra)` y método para convertirla a cadena
  
  * Maquina: implementa la maquina, que contiene toda la información necesaria.
  Solo necesita el nombre de un archivo .json con la expresión
  y sus datos con el formato correcto para construirse.

* test.py: Conjunto de tests para todas las clases y todas sus funcionalidades
Para ejecutar los test, no es necesario ningún tipo de argumento:

```bash
python3 test.py
```

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

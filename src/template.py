# template.py

import sys
import json
import re

def generate_template(expression, num_states):
    alphabet = sorted(set(re.findall(r'[a-z]', expression)))
    return {
        "expresion": expression,
        "inicial": 0,
        "finales": list(range(1, num_states)),
        "matriz": {
            str(i): {letter: 0 for letter in alphabet}
            for i in range(num_states)
        }
    }

def main():

    try:
        expression, num_states = sys.argv[1], int(sys.argv[2])
    except ValueError:
        print("Error: Los argumentos deben ser expresiones y números enteros.")
        print("Ejemplo: python template.py aa*bb*c 4")
        sys.exit(1)
    except IndexError:
        print("Error: Numero incorrecto de argumentos.")
        print("Ejemplo: python template.py aa*bb*c 4")
        sys.exit(1)

    template = generate_template(expression, num_states)
    filename = "plantilla.json"

    with open(filename, 'w') as f:
        json.dump(template, f, indent=4)

    print(f"Archivo '{filename}' generado con éxito.")

if __name__ == "__main__":
    main()

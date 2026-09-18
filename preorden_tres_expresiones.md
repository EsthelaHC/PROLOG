# Tres expresiones resueltas en preorden

## Expresiones convertidas

Se respeta la prioridad normal: primero multiplicaciones y divisiones, después sumas.

| Inciso | Expresión normal | Expresión en preorden | Resultado |
|---|---|---|---:|
| a | `2+6*5*2+10/2+6` | `+ + + 2 * * 6 5 2 / 10 2 6` | 73 |
| b | `6*6+9+2+6*3+5` | `+ + + + * 6 6 9 2 * 6 3 5` | 70 |
| c | `10*10+10+6+3+6*3+5` | `+ + + + + * 10 10 10 6 3 * 6 3 5` | 142 |

## Código en Python

```python
def evaluar(elementos):
    if len(elementos) == 0:
        raise ValueError("La expresión está incompleta")

    elemento = elementos.pop(0)

    if elemento in ["+", "-", "*", "/"]:
        a = evaluar(elementos)
        b = evaluar(elementos)

        if elemento == "+":
            return a + b
        if elemento == "-":
            return a - b
        if elemento == "*":
            return a * b
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b

    return float(elemento)


expresiones = [
    "+ + + 2 * * 6 5 2 / 10 2 6",
    "+ + + + * 6 6 9 2 * 6 3 5",
    "+ + + + + * 10 10 10 6 3 * 6 3 5"
]

letras = ["a", "b", "c"]

for i in range(len(expresiones)):
    elementos = expresiones[i].split()
    resultado = evaluar(elementos)
    print(f"{letras[i]}) {expresiones[i]}")
    print(f"   Resultado: {resultado:g}\n")
```

## Explicación

Las tres expresiones se guardan en una lista. El ciclo las toma una por una, las divide en elementos y manda cada lista a la función `evaluar`.

La función reconoce los operadores porque aparecen antes de sus dos valores. Por ejemplo, `* 6 5` significa multiplicar `6` por `5`. Al llamarse a sí misma, la función puede resolver primero las partes internas y después completar toda la operación.

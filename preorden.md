# Evaluación en preorden de una expresión

## Expresión

```text
10 * 10 + 10 + 6 + 3 + 6 + 10
```

Respetando la prioridad de la multiplicación y asociando las sumas de izquierda a derecha, su forma prefija o preorden es:

```text
+ + + + + * 10 10 10 6 3 6 10
```

El operador aparece antes de sus dos operandos. El resultado esperado es `135`.

## Código en Python

```python
def evaluar_preorden(elementos):
    if len(elementos) == 0:
        raise ValueError("La expresión está incompleta")

    elemento = elementos.pop(0)

    if elemento in ["+", "-", "*", "/"]:
        izquierdo = evaluar_preorden(elementos)
        derecho = evaluar_preorden(elementos)

        if elemento == "+":
            return izquierdo + derecho
        if elemento == "-":
            return izquierdo - derecho
        if elemento == "*":
            return izquierdo * derecho
        if derecho == 0:
            raise ValueError("No se puede dividir entre cero")
        return izquierdo / derecho

    return float(elemento)


expresion = "+ + + + + * 10 10 10 6 3 6 10"
elementos = expresion.split()

try:
    resultado = evaluar_preorden(elementos)
    print("Expresión en preorden:", expresion)
    print(f"Resultado: {resultado:g}")
except ValueError as error:
    print("Error:", error)
```

## Explicación

Primero, `split()` separa la expresión y forma una lista de elementos. La función toma el primero con `pop(0)`. Si es un número, lo convierte a `float`; si es un operador, busca de forma recursiva los dos valores que necesita.

En este ejercicio, `* 10 10` produce `100`. Después las llamadas pendientes agregan los demás números hasta llegar al resultado `135`.

## Recorrido resumido

| Operación | Resultado acumulado |
|---|---:|
| `10 * 10` | 100 |
| `100 + 10` | 110 |
| `110 + 6` | 116 |
| `116 + 3` | 119 |
| `119 + 6` | 125 |
| `125 + 10` | 135 |

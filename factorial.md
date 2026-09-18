# Factorial de un número

## Objetivo

Calcular el factorial de un entero no negativo mediante recursividad. El factorial de `n` se obtiene multiplicando todos los enteros desde `n` hasta `1`.

## Código en Python

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


numero = int(input("Número: "))

if numero < 0 or numero > 20:
    print("Escribe un número entre 0 y 20.")
else:
    print(f"{numero}! = {factorial(numero)}")
```

## Explicación

El factorial se forma multiplicando el número por todos sus anteriores hasta llegar a `1`. Por eso, para calcular `5!`, la función deja pendientes las multiplicaciones `5 × 4 × 3 × 2 × 1`.

Cuando `n` vale `0` o `1`, la función devuelve `1` y comienza a regresar los resultados. Se usan valores de `0` a `20` para que la práctica y su salida sean fáciles de revisar.

## Prueba de escritorio para `n = 5`

| Llamada | Operación pendiente | Valor al regresar |
|---|---|---:|
| `factorial(1)` | caso base | 1 |
| `factorial(2)` | `2 × 1` | 2 |
| `factorial(3)` | `3 × 2` | 6 |
| `factorial(4)` | `4 × 6` | 24 |
| `factorial(5)` | `5 × 24` | 120 |

Salida:

```text
Número: 5
5! = 120
```

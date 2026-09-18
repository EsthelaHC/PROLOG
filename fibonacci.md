# Sucesión de Fibonacci

## Objetivo

Calcular un término de Fibonacci de manera recursiva. En esta sucesión, cada término se obtiene sumando los dos anteriores:

```text
0, 1, 1, 2, 3, 5, 8, 13...
```

## Código en Python

```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Posición de Fibonacci: "))

if n < 0 or n > 45:
    print("Escribe una posición entre 0 y 45.")
else:
    print(f"F({n}) = {fibonacci(n)}")
```

## Explicación

La función tiene dos casos en los que ya conoce la respuesta: la posición `0` vale `0` y la posición `1` vale `1`. Estos casos también sirven para detener las llamadas recursivas.

Para cualquier otra posición se suman `fibonacci(n - 1)` y `fibonacci(n - 2)`. El límite de `45` se mantiene porque este método vuelve a calcular varios términos y se hace lento con valores mayores.

## Prueba de escritorio para `n = 5`

| Cálculo | Sustitución | Resultado |
|---|---|---:|
| `F(2)` | `F(1) + F(0)` | 1 |
| `F(3)` | `F(2) + F(1)` | 2 |
| `F(4)` | `F(3) + F(2)` | 3 |
| `F(5)` | `F(4) + F(3)` | 5 |

Salida:

```text
Posición de Fibonacci: 5
F(5) = 5
```

# División mediante restas sucesivas

## Objetivo

Dividir dos enteros positivos sin utilizar los operadores `/` ni `%`. El cociente se obtiene contando cuántas veces se puede restar el divisor al dividendo.

## Código en Python

```python
def dividir(restante, divisor):
    if restante < divisor:
        return 0, restante

    cociente, residuo = dividir(restante - divisor, divisor)
    return cociente + 1, residuo


dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

if dividendo < 0 or divisor <= 0:
    print("Usa un dividendo no negativo y un divisor positivo.")
else:
    cociente, residuo = dividir(dividendo, divisor)
    print("Cociente:", cociente)
    print("Residuo:", residuo)
```

## Explicación

La función quita el divisor una vez en cada llamada. Cuando el valor restante ya es menor, no se puede hacer otra resta completa y ese valor se toma como residuo.

Mientras las llamadas regresan, se suma `1` al cociente por cada resta que sí se realizó. De esta manera se obtiene la división sin utilizar `/` ni `%`.

## Prueba de escritorio: `17 ÷ 5`

| Paso | Restante antes de restar | Cociente |
|---:|---:|---:|
| Inicial | 17 | 0 |
| 1 | 12 | 1 |
| 2 | 7 | 2 |
| 3 | 2 | 3 |

Como `2` es menor que `5`, el algoritmo se detiene. El cociente es `3` y el residuo es `2`.

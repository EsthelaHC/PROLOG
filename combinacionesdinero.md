# Combinaciones de billetes y monedas

## Objetivo

Encontrar todas las maneras de formar una cantidad usando las denominaciones `100`, `50`, `20`, `10`, `5` y `2`. Una denominación se puede utilizar varias veces.

## Código en Python

```python
denominaciones = [100, 50, 20, 10, 5, 2]
total = 0


def buscar_combinaciones(posicion, restante, cantidades):
    global total

    # Si ya se revisaron todas las denominaciones, se comprueba el resultado.
    if posicion == len(denominaciones):
        if restante == 0:
            total += 1
            partes = []

            for i in range(len(denominaciones)):
                if cantidades[i] > 0:
                    partes.append(
                        f"{cantidades[i]} de ${denominaciones[i]}"
                    )

            print(f"{total}) " + "  ".join(partes))
        return

    moneda = denominaciones[posicion]
    maximo = restante // moneda

    # Se prueban todas las cantidades posibles de la moneda actual.
    for cantidad in range(maximo + 1):
        cantidades[posicion] = cantidad
        buscar_combinaciones(
            posicion + 1,
            restante - cantidad * moneda,
            cantidades
        )

    cantidades[posicion] = 0


cantidad_objetivo = int(input("Cantidad que se desea formar: $"))

if cantidad_objetivo < 0:
    print("La cantidad no puede ser negativa.")
else:
    cantidades = [0] * len(denominaciones)
    buscar_combinaciones(0, cantidad_objetivo, cantidades)
    print(f"\nTotal de combinaciones: {total}")
```

## Explicación

La lista `denominaciones` guarda los valores disponibles. La función empieza con los `$100`, prueba desde cero hasta la cantidad máxima posible y luego hace lo mismo con el siguiente valor.

En cada llamada, `restante` indica cuánto dinero falta. Si al terminar vale cero, se encontró una combinación correcta y se muestra en pantalla. Como siempre se sigue el mismo orden de denominaciones, una combinación no se cuenta dos veces.

## Ejemplo de uso

```text
Cantidad que se desea formar: $10
1) 5 de $2
2) 2 de $5
3) 1 de $10

Total de combinaciones: 3
```

## Ejecución

```bash
python programa.py
```

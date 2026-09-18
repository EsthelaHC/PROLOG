# Programa de 10 áreas geométricas

## Figuras incluidas

El programa calcula las áreas de cuadrado, rectángulo, triángulo, círculo, paralelogramo, rombo, trapecio, elipse, polígono regular y corona circular.

## Código en Python

```python
import math


def area_cuadrado(lado):
    return lado * lado


def area_rectangulo(base, altura):
    return base * altura


def area_triangulo(base, altura):
    return base * altura / 2


def area_circulo(radio):
    return math.pi * radio * radio


def area_paralelogramo(base, altura):
    return base * altura


def area_rombo(diagonal_mayor, diagonal_menor):
    return diagonal_mayor * diagonal_menor / 2


def area_trapecio(base_mayor, base_menor, altura):
    return (base_mayor + base_menor) * altura / 2


def area_elipse(semieje_mayor, semieje_menor):
    return math.pi * semieje_mayor * semieje_menor


def area_poligono_regular(lados, longitud, apotema):
    perimetro = lados * longitud
    return perimetro * apotema / 2


def area_corona_circular(radio_mayor, radio_menor):
    return math.pi * (radio_mayor ** 2 - radio_menor ** 2)


print("CALCULADORA DE ÁREAS")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Triángulo")
print("4. Círculo")
print("5. Paralelogramo")
print("6. Rombo")
print("7. Trapecio")
print("8. Elipse")
print("9. Polígono regular")
print("10. Corona circular")

opcion = int(input("Opción: "))
resultado = None

if opcion == 1:
    lado = float(input("Lado: "))
    resultado = area_cuadrado(lado)
elif opcion == 2:
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    resultado = area_rectangulo(base, altura)
elif opcion == 3:
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    resultado = area_triangulo(base, altura)
elif opcion == 4:
    radio = float(input("Radio: "))
    resultado = area_circulo(radio)
elif opcion == 5:
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    resultado = area_paralelogramo(base, altura)
elif opcion == 6:
    diagonal_mayor = float(input("Diagonal mayor: "))
    diagonal_menor = float(input("Diagonal menor: "))
    resultado = area_rombo(diagonal_mayor, diagonal_menor)
elif opcion == 7:
    base_mayor = float(input("Base mayor: "))
    base_menor = float(input("Base menor: "))
    altura = float(input("Altura: "))
    resultado = area_trapecio(base_mayor, base_menor, altura)
elif opcion == 8:
    semieje_mayor = float(input("Semieje mayor: "))
    semieje_menor = float(input("Semieje menor: "))
    resultado = area_elipse(semieje_mayor, semieje_menor)
elif opcion == 9:
    lados = int(input("Número de lados: "))
    longitud = float(input("Longitud de cada lado: "))
    apotema = float(input("Apotema: "))

    if lados < 3:
        print("Se necesitan al menos 3 lados.")
    else:
        resultado = area_poligono_regular(lados, longitud, apotema)
elif opcion == 10:
    radio_mayor = float(input("Radio mayor: "))
    radio_menor = float(input("Radio menor: "))

    if radio_mayor <= radio_menor:
        print("El radio mayor debe ser más grande.")
    else:
        resultado = area_corona_circular(radio_mayor, radio_menor)
else:
    print("Opción no válida.")

if resultado is not None:
    print(f"Área = {resultado:.2f} unidades cuadradas")
```

## Explicación

El programa separa cada fórmula en una función pequeña. Después muestra el menú y utiliza una estructura `if`, `elif` y `else` para saber qué datos debe pedir y qué función debe llamar.

La constante π se obtiene con `math.pi` y `** 2` sirve para elevar un número al cuadrado. Todas las medidas deben usar la misma unidad; si se escriben centímetros, el área final estará en centímetros cuadrados.

## Fórmulas usadas

| Figura | Fórmula |
|---|---|
| Cuadrado | `lado²` |
| Rectángulo | `base × altura` |
| Triángulo | `(base × altura) / 2` |
| Círculo | `π × radio²` |
| Paralelogramo | `base × altura` |
| Rombo | `(diagonal mayor × diagonal menor) / 2` |
| Trapecio | `((base mayor + base menor) × altura) / 2` |
| Elipse | `π × semieje mayor × semieje menor` |
| Polígono regular | `(perímetro × apotema) / 2` |
| Corona circular | `π × (radio mayor² - radio menor²)` |

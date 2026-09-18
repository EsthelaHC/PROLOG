# Programa de 10 volúmenes geométricos

## Cuerpos incluidos

El programa calcula los volúmenes de cubo, prisma rectangular, esfera, cilindro, cono, pirámide, prisma triangular, tetraedro regular, elipsoide y toroide.

## Código en Python

```python
import math


def volumen_cubo(lado):
    return lado ** 3


def volumen_prisma_rectangular(largo, ancho, alto):
    return largo * ancho * alto


def volumen_esfera(radio):
    return 4 * math.pi * radio ** 3 / 3


def volumen_cilindro(radio, altura):
    return math.pi * radio ** 2 * altura


def volumen_cono(radio, altura):
    return math.pi * radio ** 2 * altura / 3


def volumen_piramide(area_base, altura):
    return area_base * altura / 3


def volumen_prisma_triangular(base, altura_triangulo, largo):
    area_triangulo = base * altura_triangulo / 2
    return area_triangulo * largo


def volumen_tetraedro(arista):
    return arista ** 3 / (6 * math.sqrt(2))


def volumen_elipsoide(a, b, c):
    return 4 * math.pi * a * b * c / 3


def volumen_toroide(radio_mayor, radio_tubo):
    return 2 * math.pi ** 2 * radio_mayor * radio_tubo ** 2


print("CALCULADORA DE VOLÚMENES")
print("1. Cubo")
print("2. Prisma rectangular")
print("3. Esfera")
print("4. Cilindro")
print("5. Cono")
print("6. Pirámide")
print("7. Prisma triangular")
print("8. Tetraedro regular")
print("9. Elipsoide")
print("10. Toroide")

opcion = int(input("Opción: "))
resultado = None

if opcion == 1:
    lado = float(input("Lado: "))
    resultado = volumen_cubo(lado)
elif opcion == 2:
    largo = float(input("Largo: "))
    ancho = float(input("Ancho: "))
    alto = float(input("Alto: "))
    resultado = volumen_prisma_rectangular(largo, ancho, alto)
elif opcion == 3:
    radio = float(input("Radio: "))
    resultado = volumen_esfera(radio)
elif opcion == 4:
    radio = float(input("Radio: "))
    altura = float(input("Altura: "))
    resultado = volumen_cilindro(radio, altura)
elif opcion == 5:
    radio = float(input("Radio: "))
    altura = float(input("Altura: "))
    resultado = volumen_cono(radio, altura)
elif opcion == 6:
    area_base = float(input("Área de la base: "))
    altura = float(input("Altura: "))
    resultado = volumen_piramide(area_base, altura)
elif opcion == 7:
    base = float(input("Base del triángulo: "))
    altura_triangulo = float(input("Altura del triángulo: "))
    largo = float(input("Largo del prisma: "))
    resultado = volumen_prisma_triangular(base, altura_triangulo, largo)
elif opcion == 8:
    arista = float(input("Arista: "))
    resultado = volumen_tetraedro(arista)
elif opcion == 9:
    a = float(input("Primer semieje: "))
    b = float(input("Segundo semieje: "))
    c = float(input("Tercer semieje: "))
    resultado = volumen_elipsoide(a, b, c)
elif opcion == 10:
    radio_mayor = float(input("Radio mayor: "))
    radio_tubo = float(input("Radio del tubo: "))

    if radio_mayor <= radio_tubo:
        print("El radio mayor debe superar al del tubo.")
    else:
        resultado = volumen_toroide(radio_mayor, radio_tubo)
else:
    print("Opción no válida.")

if resultado is not None:
    print(f"Volumen = {resultado:.2f} unidades cúbicas")
```

## Explicación

Cada cuerpo geométrico tiene una función con su fórmula. El menú guarda la elección del usuario en `opcion` y los bloques `if` y `elif` solicitan solamente las medidas necesarias para ese cuerpo.

El operador `** 3` calcula un cubo y `math.sqrt(2)` obtiene la raíz cuadrada de `2`. El resultado se muestra con dos decimales y en unidades cúbicas; por ejemplo, al usar centímetros se obtienen centímetros cúbicos.

## Fórmulas usadas

| Cuerpo | Fórmula |
|---|---|
| Cubo | `lado³` |
| Prisma rectangular | `largo × ancho × alto` |
| Esfera | `(4 × π × radio³) / 3` |
| Cilindro | `π × radio² × altura` |
| Cono | `(π × radio² × altura) / 3` |
| Pirámide | `(área de la base × altura) / 3` |
| Prisma triangular | `área del triángulo × largo` |
| Tetraedro regular | `arista³ / (6√2)` |
| Elipsoide | `(4 × π × a × b × c) / 3` |
| Toroide | `2 × π² × radio mayor × radio del tubo²` |

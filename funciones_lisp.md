# Investigación: 25 funciones primitivas de Lisp

Esta consigna trata específicamente sobre Lisp, por eso los ejemplos de este archivo se conservan en **Common Lisp**. Una función primitiva es una operación básica que el lenguaje ya proporciona.

| Núm. | Función | Uso sencillo | Ejemplo | Resultado |
|---:|---|---|---|---|
| 1 | `+` | Suma números | `(+ 4 3)` | `7` |
| 2 | `-` | Resta números | `(- 9 2)` | `7` |
| 3 | `*` | Multiplica números | `(* 4 3)` | `12` |
| 4 | `/` | Divide números | `(/ 10 2)` | `5` |
| 5 | `mod` | Obtiene el residuo | `(mod 10 3)` | `1` |
| 6 | `abs` | Obtiene el valor absoluto | `(abs -8)` | `8` |
| 7 | `sqrt` | Calcula una raíz cuadrada | `(sqrt 25)` | `5` |
| 8 | `expt` | Eleva a una potencia | `(expt 2 3)` | `8` |
| 9 | `max` | Busca el número mayor | `(max 2 9 4)` | `9` |
| 10 | `min` | Busca el número menor | `(min 2 9 4)` | `2` |
| 11 | `=` | Compara números | `(= 5 5)` | `T` |
| 12 | `<` | Comprueba si es menor | `(< 3 8)` | `T` |
| 13 | `>` | Comprueba si es mayor | `(> 3 8)` | `NIL` |
| 14 | `list` | Crea una lista | `(list 1 2 3)` | `(1 2 3)` |
| 15 | `cons` | Agrega un elemento al inicio | `(cons 1 '(2 3))` | `(1 2 3)` |
| 16 | `car` | Obtiene el primer elemento | `(car '(8 9 10))` | `8` |
| 17 | `cdr` | Obtiene la lista sin el primero | `(cdr '(8 9 10))` | `(9 10)` |
| 18 | `first` | Otra forma de obtener el primero | `(first '(a b c))` | `A` |
| 19 | `rest` | Obtiene los elementos restantes | `(rest '(a b c))` | `(B C)` |
| 20 | `append` | Une listas | `(append '(1 2) '(3 4))` | `(1 2 3 4)` |
| 21 | `reverse` | Invierte una lista | `(reverse '(1 2 3))` | `(3 2 1)` |
| 22 | `length` | Cuenta los elementos | `(length '(a b c))` | `3` |
| 23 | `nth` | Obtiene un elemento por posición | `(nth 1 '(a b c))` | `B` |
| 24 | `member` | Busca un elemento | `(member 'b '(a b c))` | `(B C)` |
| 25 | `null` | Comprueba si una lista está vacía | `(null '())` | `T` |

## Programa pequeño de demostración

```lisp
(format t "Suma: ~a~%" (+ 4 3))
(format t "Lista: ~a~%" (list 1 2 3))
(format t "Primer elemento: ~a~%" (car '(8 9 10)))
(format t "Lista invertida: ~a~%" (reverse '(1 2 3)))
(format t "Cantidad de elementos: ~a~%" (length '(a b c)))
```

## Explicación

En Common Lisp se escribe primero la operación y después los datos que va a usar. Todo queda dentro de paréntesis. Por ejemplo, `(+ 4 3)` indica que se deben sumar `4` y `3`.

Las primeras funciones de la tabla sirven para hacer cálculos y comparaciones. Las últimas trabajan principalmente con listas: pueden crearlas, unirlas, invertirlas o consultar sus elementos. Cuando una comparación es verdadera aparece `T`; cuando es falsa aparece `NIL`.

En el programa de demostración, `format` muestra información en pantalla. La letra `t` señala la salida normal, `~a` es el lugar donde se coloca un resultado y `~%` agrega un salto de línea. Así, la primera instrucción realiza la suma y muestra `Suma: 7`.

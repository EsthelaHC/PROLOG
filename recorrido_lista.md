# Ejercicio 12: mostrar una lista mediante recursividad

## Código en Common Lisp

```lisp
(defun mostrar-elementos (elementos)
  (if elementos
      (progn
        (write (car elementos))
        (terpri)
        (mostrar-elementos (cdr elementos)))
      nil))

;; Ejemplo
(mostrar-elementos '(ROJO VERDE AZUL AMARILLO))
```

## Salida

```text
ROJO
VERDE
AZUL
AMARILLO
```

## Explicación

La condición del `if` comprueba si todavía quedan datos en la lista. Cuando hay elementos, `car` toma el primero y `write` lo muestra. Luego la función se llama nuevamente usando `cdr`, que contiene el resto de la lista.

Al llegar a una lista vacía, la condición es falsa, se devuelve `nil` y termina el recorrido.

`progn` únicamente permite realizar varias acciones dentro de la parte verdadera del `if`. La lógica para recorrer la lista sigue dependiendo de `if`, `car`, `cdr` y la llamada recursiva.

## Seguimiento breve

| Llamada | Elemento mostrado | Siguiente lista |
|---|---|---|
| `(ROJO VERDE AZUL AMARILLO)` | `ROJO` | `(VERDE AZUL AMARILLO)` |
| `(VERDE AZUL AMARILLO)` | `VERDE` | `(AZUL AMARILLO)` |
| `(AZUL AMARILLO)` | `AZUL` | `(AMARILLO)` |
| `(AMARILLO)` | `AMARILLO` | `NIL` |

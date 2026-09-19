# Ejercicio 11: acceso a elementos con `car` y `cdr`

En los siguientes ejemplos se recorre cada lista usando `car` para tomar el primer elemento y `cdr` para avanzar al resto. En esta versión no se usan combinaciones abreviadas como `cadr` o `caddr`.

## Inciso A

Lista utilizada:

```lisp
(defparameter *lista-a* '(1 2 3 4 5 6 7 8 9 10))
```

### Elemento 6

```lisp
(car (cdr (cdr (cdr (cdr (cdr *lista-a*))))))
```

### Elemento 8

```lisp
(car (cdr (cdr (cdr (cdr (cdr (cdr (cdr *lista-a*))))))))
```

### Elemento 10

```lisp
(car (cdr (cdr (cdr (cdr (cdr (cdr (cdr (cdr (cdr *lista-a*))))))))))
```

Cada `cdr` elimina el primer elemento. Cuando el número buscado queda al inicio, `car` lo obtiene.

---

## Inciso B

Lista utilizada:

```lisp
(defparameter *lista-b* '(1 2 (3 4) (A B C D)))
```

```lisp
;; Obtener D
(car (cdr (cdr (cdr
  (car (cdr (cdr (cdr *lista-b*))))))))

;; Obtener C
(car (cdr (cdr
  (car (cdr (cdr (cdr *lista-b*)))))))

;; Obtener 4
(car (cdr
  (car (cdr (cdr *lista-b*)))))

;; Obtener 2
(car (cdr *lista-b*))

;; Obtener A
(car
  (car (cdr (cdr (cdr *lista-b*)))))
```

Primero se avanza hasta la sublista necesaria. Después se vuelve a usar `car` o `cdr` dentro de ella para localizar el dato.

---

## Inciso C

Lista utilizada:

```lisp
(defparameter *lista-c* '((A B C) (R (T X) (Z W))))
```

Para que las expresiones sean más claras, se guardan temporalmente las partes de la lista:

```lisp
(let* ((grupo-abc (car *lista-c*))
       (grupo-r   (car (cdr *lista-c*)))
       (grupo-tx  (car (cdr grupo-r)))
       (grupo-zw  (car (cdr (cdr grupo-r)))))

  (format t "W = ~a~%" (car (cdr grupo-zw)))
  (format t "Z = ~a~%" (car grupo-zw))
  (format t "T = ~a~%" (car grupo-tx))
  (format t "R = ~a~%" (car grupo-r))
  (format t "X = ~a~%" (car (cdr grupo-tx)))
  (format t "A = ~a~%" (car grupo-abc)))
```

Resultado:

```text
W = W
Z = Z
T = T
R = R
X = X
A = A
```

---

## Inciso D

Lista utilizada:

```lisp
(defparameter *lista-d* '(((((A B) (C D) (F G))))))
```

La lista de pares está dentro de tres niveles adicionales. Primero se eliminan esas capas y después se obtiene cada letra.

```lisp
(let* ((pares (car (car (car *lista-d*))))
       (par-ab (car pares))
       (par-cd (car (cdr pares)))
       (par-fg (car (cdr (cdr pares)))))

  (format t "A = ~a~%" (car par-ab))
  (format t "B = ~a~%" (car (cdr par-ab)))
  (format t "C = ~a~%" (car par-cd))
  (format t "D = ~a~%" (car (cdr par-cd)))
  (format t "F = ~a~%" (car par-fg))
  (format t "G = ~a~%" (car (cdr par-fg))))
```

## Idea principal

- `car` selecciona el primer elemento.
- `cdr` descarta el primero y permite continuar con los demás.
- Cuando aparece una lista dentro de otra, las mismas operaciones se aplican nuevamente sobre la sublista.


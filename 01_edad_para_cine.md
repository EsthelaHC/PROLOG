# Ejercicio 1: Edad para cine

### Código

```lisp
(defparameter *errores* 0)

(defun reportar-error (mensaje)
  (incf *errores*)
  (format t "[ERROR] ~a~%" mensaje)
  nil)

(defun reportar-ok (mensaje)
  (format t "[OK] ~a~%" mensaje)
  t)

(defun validar-edad-cine (edad)
  (if (integerp edad)
      (if (< edad 0)
          (reportar-error "Edad negativa")
          (if (> edad 120)
              (reportar-error "Edad no realista")
              (if (< edad 13)
                  (reportar-ok "AA (infantil)")
                  (if (< edad 18)
                      (reportar-ok "B (adolescentes)")
                      (reportar-ok "B15/C (adultos)")))))
      (reportar-error "La edad debe ser un entero")))

;; Pruebas:
;; (validar-edad-cine 10)
;; (validar-edad-cine 16)
;; (validar-edad-cine 21)
;; (validar-edad-cine -3)
;; (validar-edad-cine 200)
;; (validar-edad-cine 17.5)
```

### Explicación

La función comprueba que la edad sea un entero entre 0 y 120. Después usa `if` para asignar AA a menores de 13, B a quienes tienen entre 13 y 17, y B15/C a los adultos. Devuelve `T` si el dato es válido y `NIL` si hay un error.

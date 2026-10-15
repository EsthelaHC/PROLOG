# Ejercicio 5: Semáforo de promedio

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

(defun semaforo-promedio (promedio)
  (unless (numberp promedio)
    (return-from semaforo-promedio
      (reportar-error "El promedio debe ser numerico")))

  (unless (and (>= promedio 0)
               (<= promedio 100))
    (return-from semaforo-promedio
      (reportar-error "Promedio fuera de [0, 100]")))

  (cond
    ((< promedio 60)
      (reportar-ok "ROJO - Reprobado"))
    ((< promedio 80)
      (reportar-ok "AMARILLO - Regular"))
    ((< promedio 90)
      (reportar-ok "VERDE - Bien"))
    (t
      (reportar-ok "ORO - Excelencia"))))

;; Pruebas:
;; (semaforo-promedio 45)
;; (semaforo-promedio 75)
;; (semaforo-promedio 88)
;; (semaforo-promedio 97)
;; (semaforo-promedio 110)
;; (semaforo-promedio "nueve")
```

### Explicación

Primero se valida que el promedio esté entre 0 y 100. Luego `cond` asigna rojo si es menor que 60, amarillo de 60 a menos de 80, verde de 80 a menos de 90 y oro de 90 a 100. Un promedio válido devuelve `T`, incluso si es reprobatorio.

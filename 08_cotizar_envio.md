# Ejercicio 8: Cotizar un envío

### Código

```lisp
(defparameter *errores* 0)
(defparameter *avisos* 0)

(defun reportar-error (mensaje)
  (incf *errores*)
  (format t "[ERROR] ~a~%" mensaje)
  nil)

(defun reportar-aviso (mensaje)
  (incf *avisos*)
  (format t "[AVISO] ~a~%" mensaje)
  t)

(defun cotizar-envio (codigo peso zona-riesgo)
  (multiple-value-bind (costo peso-maximo servicio)
      (case codigo
        (est (values 80 20 "Estandar"))
        (exp (values 160 10 "Express"))
        (noc (values 220 5 "Nocturno"))
        (int (values 450 15 "Internacional"))
        (otherwise
          (return-from cotizar-envio
            (reportar-error "Codigo de servicio invalido"))))

    (unless (and (numberp peso) (> peso 0))
      (return-from cotizar-envio
        (reportar-error "El peso debe ser un numero positivo")))

    (unless (<= peso peso-maximo)
      (return-from cotizar-envio
        (reportar-error "Excede peso del servicio")))

    (when zona-riesgo
      (incf costo 40)
      (reportar-aviso "Recargo zona de riesgo +40"))

    (format t "[OK] ~a: costo final $~a~%" servicio costo)
    t))

;; Pruebas:
;; (cotizar-envio 'est 3.0 nil)
;; (cotizar-envio 'exp 12.0 nil)
;; (cotizar-envio 'noc 2.0 t)
;; (cotizar-envio 'xxx 1.0 nil)
```

### Explicación

El `case` selecciona el servicio, su costo y el peso máximo. Después se comprueba que el peso sea positivo y no exceda el límite. Si la zona es de riesgo, `when` agrega $40; al final se muestra el total del envío.

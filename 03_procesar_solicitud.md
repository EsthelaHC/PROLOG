# Ejercicio 3: Procesar una solicitud

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

(defun procesar-solicitud (nombre correo edad acepta-terminos)
  (declare (ignore edad))

  (unless (and (stringp nombre)
               (> (length nombre) 0))
    (return-from procesar-solicitud
      (reportar-error "Falta nombre")))

  (unless (and (stringp correo)
               (search "@" correo))
    (return-from procesar-solicitud
      (reportar-error "Correo invalido")))

  (unless acepta-terminos
    (return-from procesar-solicitud
      (reportar-error "Debe aceptar terminos")))

  (reportar-ok
    (format nil "Solicitud de ~a procesada" nombre)))

;; Pruebas:
;; (procesar-solicitud "" "a@b.com" 20 t)
;; (procesar-solicitud "Ana" "ana.b.com" 20 t)
;; (procesar-solicitud "Ana" "ana@b.com" 20 nil)
;; (procesar-solicitud "Ana" "ana@b.com" 20 t)
```

### Explicación

Con `unless` se revisan el nombre, el correo y la aceptación de términos. Si falta algo, `return-from` detiene la función y devuelve `NIL`; si todo está bien, procesa la solicitud. En este ejercicio la edad se recibe, pero no se valida.

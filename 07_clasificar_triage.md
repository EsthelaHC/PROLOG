# Ejercicio 7: Clasificar triage

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

(defun clasificacion-temperatura (temperatura)
  (cond
    ((< temperatura 35) "HIPOTERMIA")
    ((< temperatura 37.5) "NORMAL")
    ((< temperatura 39) "FIEBRE")
    (t "FIEBRE ALTA")))

(defun clasificar-triage (dato)
  (typecase dato
    (number
      (reportar-ok (clasificacion-temperatura dato)))

    (string
      (cond
        ((string-equal dato "rojo")
          (reportar-ok "ROJO - Atencion inmediata"))
        ((string-equal dato "naranja")
          (reportar-ok "NARANJA - Atencion prioritaria"))
        ((string-equal dato "verde")
          (reportar-ok "VERDE - Atencion no urgente"))
        (t
          (reportar-error "Color de triage no reconocido"))))

    (list
      (if (and (= (length dato) 2)
               (stringp (car dato))
               (numberp (cadr dato)))
          (reportar-ok
            (format nil "~a: ~a"
                    (car dato)
                    (clasificacion-temperatura (cadr dato))))
          (reportar-error "La lista debe contener nombre y temperatura")))

    (t
      (reportar-error "Tipo no soportado"))))

;; Pruebas:
;; (clasificar-triage 36.8)
;; (clasificar-triage 39.5)
;; (clasificar-triage "rojo")
;; (clasificar-triage '("Lia" 38.2))
;; (clasificar-triage 'paciente)
```

### Explicación

Con `typecase` se distingue si el dato es una temperatura, un color o una lista con nombre y temperatura. Las temperaturas se clasifican con `cond` y los colores se comparan sin distinguir mayúsculas. Un formato no admitido muestra un error. Los rangos son parte del ejercicio.

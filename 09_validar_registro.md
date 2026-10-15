# Ejercicio 9: Validar un registro

### Código

```lisp
(defparameter *errores* 0)
(defparameter *avisos* 0)

(defun reportar-error (mensaje)
  (incf *errores*)
  (format t "[ERROR] ~a~%" mensaje)
  nil)

(defun reportar-ok (mensaje)
  (format t "[OK] ~a~%" mensaje)
  t)

(defun reportar-aviso (mensaje)
  (incf *avisos*)
  (format t "[AVISO] ~a~%" mensaje)
  t)

(defun avisar-password (clave)
  (when (< (length clave) 8)
    (reportar-aviso "Clave corta: menos de 8 caracteres"))
  (when (or (string= clave "12345678")
            (string= clave "password"))
    (reportar-aviso "Clave demasiado comun"))
  (when (and (> (length clave) 0)
             (string= clave (string-downcase clave)))
    (reportar-aviso "La clave no contiene mayusculas"))
  t)

(defun validar-registro
    (usuario correo edad rol plan password acepta-terminos)
  (declare (ignore correo))

  ;; [UNLESS] terminos
  (unless acepta-terminos
    (return-from validar-registro
      (reportar-error "Debe aceptar los terminos")))

  ;; [IF] edad / plan
  (if (numberp edad)
      (progn
        (if (< edad 13)
            (return-from validar-registro
              (reportar-error "Edad minima: 13 anos")))
        (if (and (< edad 18)
                 (not (eq plan 'campus)))
            (return-from validar-registro
              (reportar-error
                "Los menores solo pueden usar el plan campus"))))
      (return-from validar-registro
        (reportar-error "La edad debe ser numerica")))

  ;; [CASE] rol
  (let ((prefijo
          (case rol
            (alumno "a/")
            (docente "d/")
            (admin "s/")
            (otherwise
              (return-from validar-registro
                (reportar-error "Rol invalido")))))
        (cuota
          ;; [CASE] plan
          (case plan
            (libre 0)
            (pro 99)
            (campus 0)
            (otherwise
              (return-from validar-registro
                (reportar-error "Plan invalido"))))))

    ;; [WHEN] admin
    (when (eq rol 'admin)
      (reportar-aviso "Admin creado: revisar bitacora de auditoria"))

    ;; [WHEN] password
    (when (stringp password)
      (avisar-password password))

    (when (< edad 18)
      (reportar-aviso "Cuenta tutelada por ser menor de edad"))

    (reportar-ok
      (format nil "Cuenta ~a~a creada. Cuota mensual: $~a"
              prefijo usuario cuota))))

;; Pruebas:
;; (validar-registro "lu" "lu@escuela.mx" 20 'alumno 'pro
;;                   "Clave123" t)
;; (validar-registro "pepe" "pepe@escuela.mx" 15 'alumno 'pro
;;                   "Clave123" t)
;; (validar-registro "nina" "nina@escuela.mx" 16 'alumno 'campus
;;                   "Clave123" t)
;; (validar-registro "root" "root@escuela.mx" 30 'admin 'libre
;;                   "password" t)
;; (validar-registro "x" "x@escuela.mx" 22 'alumno 'pro
;;                   "Clave123" nil)
```

### Explicación

El registro exige aceptar los términos y tener al menos 13 años; los menores de 18 deben usar el plan campus. Con `case` se asignan el prefijo del rol y la cuota del plan. También se muestran avisos para administradores, contraseñas débiles y menores. El correo se recibe, pero no se valida aquí.

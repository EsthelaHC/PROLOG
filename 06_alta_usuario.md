# Ejercicio 6: Alta de usuario

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

(defun alta-usuario (usuario password edad pais bloqueado)
  (if (and (stringp usuario)
           (>= (length usuario) 3)
           (stringp password)
           (>= (length password) 8)
           (numberp edad)
           (>= edad 13)
           (stringp pais)
           (or (string= pais "MX")
               (string= pais "CO")
               (string= pais "AR"))
           (not bloqueado))
      (reportar-ok "Usuario dado de alta")
      (reportar-error "Alta rechazada")))

;; Pruebas:
;; (alta-usuario "ana" "secreto1" 20 "MX" nil)
;; (alta-usuario "ana" "secreto1" 20 "US" nil)
;; (alta-usuario "ana" "secreto1" 20 "MX" t)
;; (alta-usuario "an" "secreto1" 20 "MX" nil)
```

### Explicación

El alta requiere un usuario de al menos 3 caracteres, una contraseña de al menos 8, edad mínima de 13, país MX, CO o AR y una cuenta sin bloqueo. `and`, `or` y `not` reúnen estas condiciones; el `if` final acepta o rechaza el registro.

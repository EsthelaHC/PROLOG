# Ejercicio 2: Avisos de contraseña

### Código

```lisp
(defparameter *avisos* 0)

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

;; Pruebas:
;; (avisar-password "abc")
;; (avisar-password "password")
;; (avisar-password "Secreta99")
```

### Explicación

Los bloques `when` muestran avisos si la contraseña es corta, común o no contiene mayúsculas. Puede aparecer más de un aviso y cada uno aumenta el contador `*avisos*`. La función siempre devuelve `T`, porque solo da recomendaciones.

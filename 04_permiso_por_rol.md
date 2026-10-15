# Ejercicio 4: Permisos por rol

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

(defun permiso-por-rol (rol)
  (case rol
    (admin
      (reportar-ok "Puede crear usuarios y materias"))
    (docente
      (reportar-ok "Puede calificar y pasar lista"))
    (alumno
      (reportar-ok "Puede consultar calificaciones"))
    (padre
      (reportar-ok "Puede ver boleta de sus hijos"))
    (otherwise
      ;; Un string como "admin" no es el simbolo ADMIN y se rechaza.
      (reportar-error "Rol no reconocido"))))

;; Pruebas:
;; (permiso-por-rol 'admin)
;; (permiso-por-rol 'docente)
;; (permiso-por-rol 'invitado)
;; (permiso-por-rol "admin")
```

### Explicación

La instrucción `case` asigna permisos a los roles admin, docente, alumno y padre. Un rol desconocido devuelve `NIL`. Los roles se pasan como símbolos, por ejemplo `'admin`, y no como texto entre comillas.

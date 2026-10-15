# Ejercicio 10: Crédito escolar

### Código

```lisp
(defparameter *errores* 0)

(defun reportar-error (mensaje)
  (incf *errores*)
  (format t "[ERROR] ~a~%" mensaje)
  nil)

(defstruct solicitante
  nombre
  promedio
  materias-reprobadas
  beca
  monto
  historial
  semestre)

(defun validar-solicitante (persona)
  (unless (typep persona 'solicitante)
    (return-from validar-solicitante
      (reportar-error "El dato no es un solicitante")))

  (unless (and (stringp (solicitante-nombre persona))
               (> (length (solicitante-nombre persona)) 0))
    (return-from validar-solicitante
      (reportar-error "Nombre invalido")))

  (unless (and (numberp (solicitante-promedio persona))
               (>= (solicitante-promedio persona) 0)
               (<= (solicitante-promedio persona) 100))
    (return-from validar-solicitante
      (reportar-error "Promedio fuera de [0, 100]")))

  (unless (and (integerp (solicitante-materias-reprobadas persona))
               (>= (solicitante-materias-reprobadas persona) 0))
    (return-from validar-solicitante
      (reportar-error "Materias reprobadas invalidas")))

  (unless (or (eq (solicitante-beca persona) t)
              (null (solicitante-beca persona)))
    (return-from validar-solicitante
      (reportar-error "Beca debe ser T o NIL")))

  (unless (and (numberp (solicitante-monto persona))
               (> (solicitante-monto persona) 0))
    (return-from validar-solicitante
      (reportar-error "El monto debe ser mayor que cero")))

  (unless (symbolp (solicitante-historial persona))
    (return-from validar-solicitante
      (reportar-error "Historial invalido")))

  (unless (and (integerp (solicitante-semestre persona))
               (>= (solicitante-semestre persona) 1)
               (<= (solicitante-semestre persona) 10))
    (return-from validar-solicitante
      (reportar-error "Semestre fuera de [1, 10]")))

  t)

(defun categoria-monto (monto)
  (cond
    ((< monto 2000) 'bajo)
    ((< monto 8000) 'medio)
    (t 'alto)))

(defun penalizacion-historial (historial)
  (case historial
    (limpio 0)
    (atrasos 2)
    (desconocido 1)
    (otherwise 99)))

(defun decidir-credito (persona)
  (unless (validar-solicitante persona)
    (return-from decidir-credito nil))

  (let* ((promedio (solicitante-promedio persona))
         (reprobadas (solicitante-materias-reprobadas persona))
         (historial (solicitante-historial persona))
         (categoria (categoria-monto (solicitante-monto persona)))
         (penalizacion (penalizacion-historial historial))
         (decision
           (if (or (> reprobadas 3)
                   (< promedio 70)
                   (>= penalizacion 99))
               'rechazado
               (cond
                 ((and (>= promedio 85)
                       (eq historial 'limpio)
                       (or (eq categoria 'bajo)
                           (solicitante-beca persona)))
                    'aprobado)
                 (t 'revision)))))

    ;; Un historial desconocido no equivale a limpio, por eso no basta
    ;; tener beca para obtener la aprobacion automatica.
    (when (and (solicitante-beca persona)
               (not (eq decision 'rechazado)))
      (format t "[AVISO] Prioridad: solicitante becado (~a)~%"
              (solicitante-nombre persona)))

    decision))

(defun ronda-credito (solicitantes)
  (dolist (persona solicitantes t)
    (let ((decision (decidir-credito persona)))
      (format t "~a: ~a~%"
              (if (typep persona 'solicitante)
                  (solicitante-nombre persona)
                  "Dato invalido")
              (or decision 'invalido)))))

(defparameter *ronda*
  (list
    (make-solicitante
      :nombre "Ana" :promedio 92 :materias-reprobadas 0
      :beca t :monto 1500 :historial 'limpio :semestre 4)
    (make-solicitante
      :nombre "Beto" :promedio 68 :materias-reprobadas 1
      :beca nil :monto 3000 :historial 'limpio :semestre 3)
    (make-solicitante
      :nombre "Cris" :promedio 80 :materias-reprobadas 0
      :beca nil :monto 9000 :historial 'atrasos :semestre 6)
    (make-solicitante
      :nombre "Dani" :promedio 88 :materias-reprobadas 0
      :beca nil :monto 4000 :historial 'limpio :semestre 2)
    (make-solicitante
      :nombre "Eva" :promedio 90 :materias-reprobadas 0
      :beca t :monto 5000 :historial 'desconocido :semestre 8)))

;; Prueba:
;; (ronda-credito *ronda*)
```

### Explicación

La estructura `solicitante` reúne los datos del alumno y una función los valida. El crédito se rechaza por promedio menor que 70, más de 3 materias reprobadas o historial no reconocido. Se aprueba con promedio mínimo de 85, historial limpio y monto menor que $2,000 o beca; los demás casos pasan a revisión. La ronda de ejemplo produce: Ana aprobada, Beto rechazado y Cris, Dani y Eva en revisión.

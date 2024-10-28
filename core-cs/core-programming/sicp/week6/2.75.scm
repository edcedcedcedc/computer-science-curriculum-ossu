#lang simply-scheme

(define (dot-product row vector)
  (apply + (map * row vector)))

(define (square x)
  (* x x))

(define (magnitude x)
  (sqrt (apply + (map square x))))

;cos -> domain: angles(radians, degrees), range: ratios
(define (acos ratio op)
  (define tolerance 0.0001)
  (define pi 3.141592653589793)
  (define (binary-search low high)
    (let ((mid (abs (/ (+ low high) 2))))
       (cond
         ((< (abs (- ratio (cos mid))) tolerance) mid)
         ((< (cos mid) ratio)(binary-search low mid))
         (else
          (binary-search mid high)))))
  (if (eq? op 'degrees)
      (* (/ 180 pi)(binary-search 0 pi))
      (binary-search 0 pi)))

(define (make-from-mag-ang x y)
  (define (dispatch op)
    (cond
      ((eq? op 'x-component) x)
      ((eq? op 'y-component) y)
      ((eq? op 'angle-radians)
       (acos (/(dot-product x y)
               (*(magnitude x)
                 (magnitude y)))'radians))
      ((eq? op 'angle-degrees)
       (acos (/(dot-product x y)
               (*(magnitude x)
                 (magnitude y)))'degrees))
      (else
       (error "Unknown op: MAKE-FROM-MAG-ANG" op))))
  dispatch)

(define v1 (list 1 2 3))
(define v2 (list 1 4 3))

((make-from-mag-ang v1 v2)'angle-radians)

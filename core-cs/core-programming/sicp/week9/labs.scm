#lang sicp
;3.12

(define (append x y)
  (if (null? x)
      y
      (cons (car x) (append (cdr x) y))))


(define (last-pair x)
  (if (null? (cdr x)) x (last-pair (cdr x))))

(define (append! x y)
  (set-cdr! (last-pair x) y)
  x)

(define x (list 'a 'b))
(define y (list 'c 'd))
(define z (append x '(e h)))

z
(cdr x)
(define w (append! x y))
w
(cdr x)



;ex 2
;A CS 61A student, intending to change the value of x1 to a pair with car equal to 1
;and cdr equal to 2, types the expression (set! (cdr x1) y1) instead of (set-cdr! x1 y1) and gets an error.
;Explain why

(define x1 (cons 1 3))
(define y1 2)

;because set! is a mutator for variables but set-cdr! is a mutator for lists


;ex 3a
(define l1 (list (list 'a) 'b))
(define l2 (list (list 'x) 'y))

;((a x b) b)
(set-cdr! (car l1) (append(car l2)(cdr l1)))
;((x b) y)
(set-cdr! (car l2) (cdr l1))
l2



;3.13

(define (make-cycle x)
  (set-cdr! (last-pair x) x)
  x)

(define z1 (make-cycle (list 'a 'b 'c)))

;inf recursion, the entire list points to itself's last pair



;3.14...
(define (mystery x)
  (define (loop x y)
    (if (null? x)
        y
        (let ((temp (cdr x)))
          (set-cdr! x y)
          (loop temp x))))
  (loop x '()))

;(mystery (list 3))

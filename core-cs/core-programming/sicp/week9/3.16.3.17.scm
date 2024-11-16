#lang simply-scheme

;3.16
;understanding
;ok here are 3 conses
;each of them has unique memory, all the other conses are just references to that memory
;a = 1 cons
;b = 1 cons
;c or d = 1 cons


;eq? compares the identity i.e memory
;equal? compares value 

(define (count-pairs x)
  (if (not (pair? x))
      0
      (+ (count-pairs (car x))
         (count-pairs (cdr x))
         1)))

;(define a (cons 'foo '()))

;(define b (cons a a))

;(define c (cons b '()))

;(define d (cons b b))

;(define a1 (cons 'foo '()))
;(set-car! a1 a1)

;(define infinity a1)




;3.17
;understanding
;use memo to avoid redundant computations on 3.16
;count the actual object in memory by identity but not by value



(define (count-pairs-memo x)
  (let ((cache '()))
    (define (helper x)
      (if (or (not (pair? x)) (memq x cache))
          0
          (begin
            (set! cache (cons x cache))
            (+ (helper (car x))
               (helper (cdr x))
               1))))
    (helper x)))


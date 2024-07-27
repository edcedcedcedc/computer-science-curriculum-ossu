#lang simply-scheme
;define this in terms of lambda by not using define 
(define (sumsq a b)
  (define (square x) (* x x))
  (+ (square a) (square b)))

(sumsq 3 4)

;my version
((lambda (a b)
   (+((lambda(x)(* x x))a)
     ((lambda(x)(* x x))b)))3 4)

;textbook version
((lambda (a b)
   ((lambda (square)
      (+ (square a) (square b)))
    (lambda (x) (* x x))))
 3 4)

;this part unfortunately I don't understand yet

(((lambda (f)
   ((lambda (x) (x x))
    (lambda (x) (f (lambda (v) ((x x) v))))))
 (lambda (fact)
   (lambda (n)
     (if (= n 0)
         1
         (* n (fact (- n 1)))))))3)

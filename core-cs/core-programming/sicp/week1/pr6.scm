#lang simply-scheme
;goal: write a test to check if and or or ar ordinary evaluation or special forms
;strategy:(or (= x 0) (= y 0) (= z 0))

(define (or-test x y z)
  (or(side-effect x)(= y 0)(= z 1)))

(define (or-test-2 x y z)
  (or(if(> x 2)'(x > 2) '(x < 2))(> y 2)(> z 2)))       

(define (side-effect x)
  (print (+ x 1)))

(or-test-2 1 3 3)

(define (and-test x y z)
  (and(side-effect x)(= y 0)(= z 1)))

;(and-test 0 0 0)
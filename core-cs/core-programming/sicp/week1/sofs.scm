#lang simply-scheme
;goal: Define a procedure that takes three numbers
;as arguments and returns the sum of the squares of the two
;larger numbers.
;strategy:abc -> max(bc) -> max(ab)

(define (square x)
  (* x x))

(define (sofs x y z)
  (+ (square(max x y))
     (square(max y z))))




#lang simply-scheme

(define (inc i)(+ i 1))

(define (cube x)
  (* x x x))

(define (sum term a next b)
  (if (> a b)
      0
      (+ (term a)
         (sum term (next a) next b))))

(define (sum-cubes a b)
  (sum cube a inc b))

#(trace sum)
#(sum-cubes 1 10)


(define (identity x) x)

(define (sum-integers a b)
  (sum identity a inc b))

#(trace sum)
#(sum-integers 1 10)

; 1.31a

(define (product term a next b)
  (if (> a b)
      1
      (* (term a)
         (product term (next a) next b))))

(define (factorial b)
  (product identity 1 inc b))

(define (wallis-product n)
  (*(/ (* 2 n)
     (-(* 2 n) 1))
    (/ (* 2 n)
     (+(* 2 n) 1))))
(define (pi-approximation n)
  (product wallis-product 1.0 inc n))

;(trace product)
;(pi-approximation 1000)



;1.32a
;show that sum and product are special cases of accumulation function
;(accumulate combiner null-value term a next b)
;
;accumulate takes as arguments the same term and
;range specifications as sum and product, together with
;a combiner procedure (of two arguments) that specifies how the current term is to be combined with the
;accumulation of the preceding terms and a null-value
;that specifies what base value to use when the terms
;run out. Write accumulate and show how sum and
;product can both be defined as simple calls to accumulate


;(define (product term a next b)
;  (if (> a b)
;      1
;      (* (term a)
;        (product term (next a) next b))))

(define (accumulate combiner null-value term a next b)
  (if (> a b)
      null-value
      (combiner (term a)
                (accumulate combiner null-value term (next a) next b))))


(define (product-accumulate a b)
  (accumulate * 1 identity a inc b))

(product-accumulate 4 5)


#lang simply-scheme
;problem 2
;understanding:
;a perfect number is that whose mod 0 sum not including itself equals itself
;
;strategy:
;using tail recursion
;i - inner loop counter, n - outer loop counter, a - accumulator
;find all i + 1, i + 2 till i = n
;if sum of a = n, then perfect 
;
;write the inner iter loop for i
;write outer iter loop for n



(define (perfect n)
  (define (helper i a)
    (if (= i n)
      a
      (helper (+ i 1)
              (if (= (remainder n i) 0)
                  (+ a i)
                  a))))
  (if (= (helper 1 0) n)
      n
      (perfect (+ n 1))))

;problem 3

;my deduction is that base cases in this function are mutually exclusive
;either the (= amount 0) or (< amount 0), so the base cases cannot interfer with each other
;they represent differnt states
;;code below is from the textbook
(define (count-change amount) (cc amount 5))

(define (cc amount kinds-of-coins)
  (cond ((= amount 0) 1)
        ((or (< amount 0) (= kinds-of-coins 0)) 0)
        (else (+ (cc amount (- kinds-of-coins 1))
                 (cc (- amount(first-denomination kinds-of-coins)) kinds-of-coins)))))

;here I exchanged the base cases, to see what happens
(define (cc2 amount kinds-of-coins)
  (cond ((or (< amount 0) (= kinds-of-coins 0)) 0)
        ((= amount 0) 1)
        (else (+ (cc amount (- kinds-of-coins 1))
                 (cc (- amount(first-denomination kinds-of-coins)) kinds-of-coins)))))

(define (first-denomination kinds-of-coins)
  (cond ((= kinds-of-coins 1) 1)
        ((= kinds-of-coins 2) 5)
        ((= kinds-of-coins 3) 10)
        ((= kinds-of-coins 4) 25)
        ((= kinds-of-coins 5) 50)))
;problem 4
;
;understanding:
;algebraic formulation for expt and expt-iter: b,n,counter, product
;
;strategy:
;
;
;implimentation:
;
;product = b^(n - counter)
;
;evaluation:
;
;
;
;
;

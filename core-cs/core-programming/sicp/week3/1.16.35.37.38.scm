#lang simply-scheme

(define (square x)(* x x))

(define (fast-expt b n)
  (cond ((= n 0) 1)
        ((even? n) (square (fast-expt b (/ n 2))))
        (else (* b (fast-expt b (- n 1))))))

(define (regular-expt b n)
  (if (= n 0)
      1
      (* b (regular-expt b (- n 1)))))
;1.16
(define (iterative-expt b n)
  (define (iter a b n)
    (cond
      ((= n 0) a)
      ((even? n) (iter a (* b b) (/ n 2)))
      (else (iter (* a b) b (- n 1)))))
  (iter 1 b n))


;this is some duplicate from week 2, I needed this code i.e 1.46 part 2
; 1.35
(define tolerance 0.00001)

(define (fixed-point f first-guess)
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2))
       tolerance))
  (define (try guess)
    (let ((next (f guess)))
      (if (close-enough? guess next)
          next
          (try next))))
  (try first-guess))

(define (golden-ratio-formula phi)
  (+ 1 (/ 1 phi)))

(define (golden-ratio guess)
  (fixed-point golden-ratio-formula guess))


; (golden-ratio 10.0)

;1.37
;
;about 11 recursive calls to get to 4 decimal places of the actual golden ratio 
;recursive definition

(define (cont-frac-rec n d k)
  (define (recur-ascend i)
    (if (> i k)
        0
        (/ (n i)(+ (d i) (recur-ascend (+ i 1))))))
  (recur-ascend 1))

(define (cont-frac-iter n d k)
  (define (iter k a)
    (if (= k 0)
        a
        (iter (- k 1) (/ (n k) (+ (d k) a )))))
  (iter k 0))

;1.38
;understanding/goal:
;1 2  1 1 4  1 1 6  1 1 8  1 1 10  1 1 12  1 1 14...
;0 1  2 3 4  5 6 7  8 9 10 - i 
;1 2  3 4 5  6 7 8  8 10 11 - i + 1
;strategy:
;a = 0 
;iter where i starts from 0, 0 1 2 => 1 2 3 i.e i => i - 1
;if i mod 3 = 1 => a + 2
;else a
;
;
(define (euler-d i)
  (define (iter i a)
    (if (= i 0)
        a
        (iter (- i 1)
                 (if (= (remainder i 3) 1)
                     (+ a 2)
                     a))))
  (if (= (remainder (- i 1) 3) 1)
      (iter (- i 1) 0)
      1))

(define (approx-e k)
  (+ (cont-frac-rec (lambda (i) 1.0)
                    euler-d k)2))

(approx-e 10)

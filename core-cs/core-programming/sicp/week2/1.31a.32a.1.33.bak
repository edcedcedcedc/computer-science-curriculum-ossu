#lang simply-scheme

(define (inc i)(+ i 1))

(define (cube x)
  (* x x x))

(define (sum term a next b)
  (if (> a b)
      0
      (+ (term a)
         (sum term (next a) next b))))

(define (square x)
  (* x x))

(define (sum-cubes a b)
  (sum cube a inc b))

;(trace sum)
;(sum-cubes 1 10)


(define (identity x) x)

(define (sum-integers a b)
  (sum identity a inc b))

;(trace sum)
;(sum-integers 1 10)

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

;(product-accumulate 4 5)


;1.33(a,b)

;prime?
;understanding:
;Number is prime if can only be divided by 1 and itself
;
;Fermat primality test including Fermat's little theorem
;a^(p-1) = 1 (mod p) then p is prime
;when p is composite it is known as Fermat liar
;(pseudoprime) to base a
;when pick an a such that
;a^(p-1) != 1 (mod p) 
;a is known as Fermat witness for compositiness of n
;example
;p = 221
;1 < a < p-1
;a = 38
;a^(p-1)=38^220 = 1 (mod 221)
;either 221 is prime or 38 is Fermat liar
;a^(p-1)=24^220 = 81 != 1 (mod 221)
;so 221 is composite

;1.33a.p1

;(define (fermat-little-therem? a p)
;  (if (not (= (remainder (expt a (- p 1)) p) 1))
;      #f
;      #t))

(define (prime? p)
  (define (fermat-little-theorem? next a p)
    (cond
      ((= a (- p 1))#t)
      ((not (= (remainder (expt a (- p 1)) p) 1))#f)
      (else
       (fermat-little-theorem? next (next a) p))))
  (fermat-little-theorem? inc 1 p))

;(trace prime?) 
;(prime? 31)
;(prime? 30)

;1.33a.p2
(define (filtered-accumulate predicate combiner null-value term a next b)
  (if (> a b)
      null-value
      (combiner (if(predicate a)
                    (term a)
                     null-value)
                (filtered-accumulate predicate combiner null-value term (next a) next b))))

(define (sum-prime-squares-filtered b)
  (filtered-accumulate prime? + 0 square 1 inc b))
;(sum-prime-squares-filtered 10)


;1.33b
;goal/understanding:
;gcd euclid algorithm but replaced the difference with modulus                  
;
;strategy:
;a b, if a > b then a if b > a then b, greater remainder of smaller till it's not zero then greater is gcd 
;
;
;
;
(define (gcd a b)
  (cond
    ((= a 0) b)
    ((= b 0) a)
    ((and(> a b)(=(remainder a b)0)(=(remainder b a)b))b)
    ((> a b)(gcd (remainder a b)b))
    ((< a b)(gcd a(remainder b a)))))
        

(gcd 0 5)
        
  


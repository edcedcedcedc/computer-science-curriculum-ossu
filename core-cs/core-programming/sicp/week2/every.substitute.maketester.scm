#lang simply-scheme

(define (square x)
  (* x x))

(define (every fn iterbl)
  (if (empty? iterbl)
      '()
      (se
       (every fn (bl iterbl))(fn (last iterbl)))))

(trace every)
(every square '(1 2 3 4))


(every first '(nowhere man))

(keep even? '(1 2 3 4 5 6))

(every (lambda (letter) (word letter letter)) 'purple)


(define (old-new? current old new)
  (if (equal? current old)
      new
      current))
      
(define (substitute sent old new)
   (if (empty? sent)
       '()
       (se
        (substitute (bl sent) old new)(old-new? (last sent) old new))))

(substitute '(she loves you yeah yeah yeah) 'yeah 'maybe)


;3
;((g)1) - the return type of this function is a function which applies arguments, and g has zero arguments
;because it only applies 1 inside within a lambfa 


;4
;f
(define f 3)
f
;(f1)
(define (f1)
  f1)
(f1)
;(f2 3)
(define (f2 x)
  (+ x))
;(f2 3)
;((f3))
(define (f3)
  ((lambda (x)(x))f3))
;((f3))
;(((f4)) 3)
(define (f4)
  (lambda (x)
    (lambda(x)(+ x))))
;(((f4))3)

;5
(define (1+ param)
  (+ 1 param))

(define (t f)
  (lambda (x) (f (f (f x)))) )

((t 1+)0)
((t (t 1+))0)




;7 make tester

(define (make-tester y)
  (lambda (x)(if (equal? x y)#t #f)))

((make-tester 'harry)'harry)

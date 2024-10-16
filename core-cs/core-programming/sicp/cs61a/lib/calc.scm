#lang simply-scheme

;; Scheme calculator -- evaluate simple expressions

; The read-eval-print loop:

(define (calc)
  (display "calc: ")
  (print (calc-eval (read)))
  (newline)
  (calc))



; Evaluate an expression:
(define (calc-eval exp)
  (cond ((or(word? exp)(number? exp)) exp)
	((list? exp) (calc-apply (car exp) (map calc-eval (cdr exp))))
	(else (error "Calc: bad expression:" exp))))

; Apply a function to arguments:
(define (new-accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (new-accumulate op initial (cdr sequence)))))

(define (calc-apply fn args)
  (cond ((eq? fn '+) (new-accumulate + 0 args))
	((eq? fn '-) (cond ((null? args) (error "Calc: no args to -"))
			   ((= (length args) 1) (- (car args)))
			   (else (- (car args) (new-accumulate + 0 (cdr args))))))
	((eq? fn '*) (new-accumulate * 1 args))
	((eq? fn '/) (cond ((null? args) (error "Calc: no args to /"))
			   ((= (length args) 1) (/ (car args)))
			   (else (/ (car args) (new-accumulate * 1 (cdr args))))))
        ((eq? fn 'first)(first (first args)))
        ((eq? fn 'last) (last (first args)))
        ((eq? fn 'butfirst)(butfirst (first args)))
        ((eq? fn 'butlast)(butlast (first args)))
	(else (error "Calc: bad operator:" fn))))

(calc-eval '(+ 1 2))

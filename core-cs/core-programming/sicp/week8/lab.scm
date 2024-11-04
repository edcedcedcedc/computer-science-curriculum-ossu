#lang simply-scheme
;ex1,ex2,ex3
;understanding:
;1) add a free variable to the local environment of make-account
;2) add response to balance message 
;3) Modify make-account so that, given the message transactions, it returns a list of all transactions

(define (make-account init-amount)
  (let ((balance init-amount)
        (transactions '()))
    (define (withdraw amount)
      (begin
        (set! balance (- balance amount))
        (set! transactions (append (list(list 'withdraw amount)) transactions))))
    (define (deposit amount)
      (begin
        (set! balance (+ balance amount))
        (set! transactions (append (list(list 'deposit amount)) transactions))))
    (define (balance->balance)
      (begin
        (set! transactions (append '(balance) transactions))
        balance))
    (define (dispatch msg)
      (cond
        ((eq? msg 'withdraw) withdraw)
        ((eq? msg 'balance) (balance->balance))
        ((eq? msg 'transactions) transactions)
        ((eq? msg 'deposit) deposit) ) )
    dispatch) )

(define acc (make-account 100))

;ex4

(define (make-adder n)(lambda (x) (+ x n)))

(define (f x)(make-adder 3))

(define g (make-adder 3))

;(f 5)
;(g 5)


(define (make-funny-adder n)
  (lambda (x)
    (if (equal? x 'new)
        (set! n (+ n 1)) 
        (+ x n))))
(define h (make-funny-adder 3))
(define j (make-funny-adder 7))



(define s 
  (let ((a 3))
    (lambda (msg)
      (cond ((equal? msg 'new)
             (lambda()(set! a (+ a 1))))
            ((equal? msg 'add)
             (lambda(x)(+ x a)))
            (else (error "huh?"))))))


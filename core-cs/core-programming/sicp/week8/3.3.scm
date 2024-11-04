#lang simply-scheme

;ex 3.3
;understanding:
;Modify the make-account procedure so that
;it creates password-protected accounts.at is, make-account
;should take a symbol as an additional argument, as in
;(define acc (make-account 100 'secret-password))
;the resulting account object should process a request only
;if it is accompanied by the password with which the account was created, and should otherwise return a complaint:
;((acc 'secret-password 'withdraw) 40)
;60
;((acc 'some-other-password 'deposit) 50)
;"Incorrect password"


;strategy:
;class var password
;a few ifs inside methods
;
;
;
;
;

(define (make-account password balance)
  (define (withdraw amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "Insufficient funds"))
  (define (deposit amount)
    (set! balance (+ balance amount))
    balance)
  (define (dispatch . m)
    (cond
      ((not(eq? (car m) password))
       (lambda(x)(begin
                   "Incorrect password")))
      ((eq? (cadr m) 'withdraw) withdraw)
      ((eq? (cadr m) 'deposit) deposit)
      (else (error "Unknown request: MAKE-ACCOUNT"
                   m))))
  dispatch)

;(define acc1 (make-account 'x 100))
;((acc1 'y 'withdraw)50)


;3.4
;modify 3.3 so if accesed more then 7 times to invoke procedure call the cops

(define (make-account-c password balance)
  (let ((attempts 0))
    (define (withdraw amount)
      (if (>= balance amount)
          (begin (set! balance (- balance amount))
                 balance)
          "Insufficient funds"))
    (define (deposit amount)
      (set! balance (+ balance amount))
      balance)
    (define (protected . message)
      (if (eq? (car message) password)
          (dispatch (cdr message))
          (lambda(x)
            (begin
              (set! attempts (+ 1 attempts))
              (if (>= attempts 3)
                  "call the cops"
                  (list "Incorrect password" attempts)
                  )))))
    (define (dispatch . message)
      (cond
        ((eq? (caar message) 'withdraw) withdraw)
        ((eq? (caar message) 'deposit) deposit)
        (else (error "Unknown request: MAKE-ACCOUNT"
                     message))))
    protected))


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

(define (make-account-cops password balance)
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
                  "Call the cops"
                  (list "Incorrect password" attempts)
                  )))))
    (define (dispatch . message)
      (cond
        ((eq? (caar message) 'withdraw) withdraw)
        ((eq? (caar message) 'deposit) deposit)
        (else (error "Unknown request: MAKE-ACCOUNT"
                     message))))
    protected))





;3.7
;understanding
;make-joint is to create additional access to the original account
;using new password
;by using new password you can map to the other name

;(makejoint password-protected-acc defined-password new-password)

;example
;(define paul-acc
;(make-joint peter-acc 'open-sesame 'rosebud))
;will allow to use peter acc with paul's acc and password

;strategy
;validate the account
;...rest


(define (make-joint object password extended-password)
  (define (dispatch . m)
    (cond
      ((or (eq? (car m) extended-password)
           (eq? (car m) password))
       (object password (cadr m)))
      (else
       (lambda(x)(begin
                   "Incorrect password")))))
  dispatch)

;(define peter-acc (make-account 'pass123 100))
;(define paul-acc (make-joint peter-acc 'pass123 'pass321))



;3.8
;understanding:
;(+ (f 0)(f 1))

;strategy:
;state 0 and 0 -> -1
;state 0 and 1 -> 1
;state 1 and 0 -> 0
;state 1 and 1 -> 1

(define f
  (let ((state -1))
    (define (dispatch x)
      (begin
        (set! state (+ 1 state))
        (cond
          ((and(= state 0)(= x 0))-1)
          ((and(= state 0)(= x 1)) 1)
          ((and(= state 1)(= x 0)) 0)
          ((and(= state 1)(= x 1)) 1)
          ((> x 1)
           "Domain must be [0,1]")
          (else
           (error "State out of range" state)))))
    dispatch))
    
(define (g)
  (let ((state 0))
    (define (dispatch)
      (begin
        (set! state (+ 1 state))
        state))
    dispatch))

;evaluation
;((g 0)) new environment is created all the time
;(define a (g 0)) you bind the environment to a
;f instead is defined once, so it creates exactly one environment


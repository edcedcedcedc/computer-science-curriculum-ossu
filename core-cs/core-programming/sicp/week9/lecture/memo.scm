#lang sicp

(define (get key)
  (let ((record (assoc key (cdr the-table))))
    (if (not record)
	#f
	(cdr record))))

(define (put key value)
  (let ((record (assoc key (cdr the-table))))
    (if (not record)
	(set-cdr! the-table
		  (cons (cons key value)
			(cdr the-table)))
	(set-cdr! record value)))
  'ok)

(define the-table (list '*table*))

(define (fib n)
  (if (< n 2)
      n
      (+ (fib (- n 1))
         (fib (- n 2)) )))

(define (fast-fib n)
  (if (< n 2)
      n
      (let ((old (get 'fib n)))
        (if (number? old)
            old
            (begin
              (put 'fib n (+ (fast-fib (- n 1))
                             (fast-fib (- n 2))))
              (get 'fib n))))))




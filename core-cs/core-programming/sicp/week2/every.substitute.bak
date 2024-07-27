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
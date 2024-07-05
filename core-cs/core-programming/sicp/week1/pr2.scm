#lang simply-scheme

(define (squares lst)
  (if (empty? lst)
       '()
      (se(squares(butlast lst))(square(last lst)) )))

(define (square x)
  (* x x))


(squares '(1 2 3 4 5))
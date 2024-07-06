#lang simply-scheme
;goal: check if the list of nums is in ascending order
;strategy: n < n + 1; n - 2 < n - 1 < n


(define (ordered? n)
  (cond
    ((and(=(count n) 2)
         (>(last n)(last (butlast n))))#t)
    ((<(last n)(last(butlast n)))#f)
    (else
       (ordered?(butlast n)))))
       
(ordered? '(1 2 3 4 5))
(ordered? '(1 2 6 4 5))
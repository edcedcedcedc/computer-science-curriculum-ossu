#lang simply-scheme
;goal:
;take a sentence return a sentencen with word only ending on e
;strategy:
;



(define (ends-e snt)
  (define (helper wd)
    (if (equal? (last wd)'e)
        wd
        '()))
  (if (empty? snt)
      '()
      (se
       (ends-e(butlast snt))(helper(last snt)))))


(ends-e '(please put the salami above the blue elephant))

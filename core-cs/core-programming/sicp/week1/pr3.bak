#lang simply-scheme
;goal: recursively substitute I, me, you
;strategy:
;I or me -> you
;you -> me
;you and count 0 -> I
;

(define (word? w sent)
  (cond ((and(equal? w 'you)(= (count sent) 1)) 'i)
       ((or (equal? w 'I)(equal? w 'me)) 'you)
       ((equal? w 'you) 'me)
       (else w) ))

(define (switch lst)
  (if (empty? lst)
      '()
      (se
       (switch (butlast lst)))
      (word? (last lst) lst))))

(switch '(you told me that I should wake you up))
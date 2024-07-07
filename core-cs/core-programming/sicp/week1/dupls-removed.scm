#lang simply-scheme
;goal: remove dupls from a list
;strategy: ?
;

(define (dupls-removed lst)
  (if (empty? lst)
      '()
       (if (member?(last lst)(dupls-removed (bl lst)))
                  (se(dupls-removed (bl lst))'())
                  (se(dupls-removed (bl lst))(last lst)))))

(define (dupls-removed1 lst)
  (if (empty? lst)
      '()
       (if(member?(last lst)(bl lst))
                  (se(dupls-removed1 (bl lst))'())
                  (se(dupls-removed1 (bl lst))(last lst)))))

(trace dupls-removed1)
(dupls-removed1 '(a b a))


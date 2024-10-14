#lang simply-scheme


;understanding:
;a btree is a hstructure where each element is either an value a list or a null
;
;     1
;  2    3
;4  5  6
;
;
;
(define binarytree
  (list 1 (list 2 (list 4 5))
          (list 3 (list 6
                        (list 7)))))
(define ls

;strategy:
;domain: btree range: btree
;enumerate nodes
;filter base case 1: null? '(), recursive case1: list? recursive case2: leafnode?
;map: void
;accumulate append '()

;implimentation
(define (invert-btree btree)
  (cond
    ((null? btree) null)
    ((list? (car btree))
     (append(invert-btree (cdr btree))(list(invert-btree (car btree)))))
     (else
      (append(invert-btree (cdr btree))(list (car btree))))))

;evaluation:
(invert-btree binarytree)

     
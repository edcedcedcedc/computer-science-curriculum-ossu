#lang simply-scheme


;understanding:
;square a tree


;strategy:

;direct
;domain -> tree range -> tree
;enumerate leafs
;filter: list? null?
;map: square
;accumulate: cons

;map recursion
;enumerate: leafs
;filter: map list? null?, null?
;map: square
;accumulate: cons(inside map)

;implimentation
(define (square x)
  (* x x))

(define (square-tree tree)
  (cond
    ((null? tree) null)
    ((list? tree)
     (cons(square-tree (car tree))
          (square-tree (cdr tree))))
    (else
     (square tree))))

;(trace square-tree)

(define my-tree
  (list 1 2 3(list 4 5(list 6 7) 8)))


(define (square-tree1 tree)
  (cond
    ((null? tree) null)
    ((list? tree)
     (map square-tree1 tree))
    (else
     (square tree))))




;2.31
(define (tree-map fn tree)
  (cond
    ((null? tree) null)
    ((list? tree)
     (map tree-map tree))
    (else
     (fn tree))))


;2.32
(define (subsets s)
  (if (null? s)
      (list null)
      (let ((rest (subsets (cdr s))))
        (append rest (map (lambda(x)(cons (car s) x))rest)))))
;(trace subsets)
(subsets '(1 2 3))




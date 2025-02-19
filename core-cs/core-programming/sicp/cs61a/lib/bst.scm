#lang simply-scheme

(define (entry tree) (car tree))

(define (left-branch tree) (cadr tree))

(define (right-branch tree) (caddr tree))

(define (make-tree entry left right)
  (list entry left right))

(define (element-of-set? x set)
  (cond ((null? set) #f)
	((= x (entry set)) #t)
	((< x (entry set))
	 (element-of-set? x (left-branch set)))
	((> x (entry set))
	 (element-of-set? x (right-branch set)))))

(define (adjoin-set x set)
  (cond ((null? set) (make-tree x '() '()))
	((= x (entry set)) set)
	((< x (entry set))
	 (make-tree (entry set)
		    (adjoin-set x (left-branch set))
		    (right-branch set)))
	((> x (entry set))
	 (make-tree (entry set)
		    (left-branch set)
		    (adjoin-set x (right-branch set))))))




;understanding:
;construct a binary tree using adjoin-set
;domain list range hierarchical list i.e binary tree

;strategy:
;base case: length 1, since I operate with a tree then (make-tree car seq, null, null)
;recur case: adjoin-set car seq cdr seq


;1 3 5 7 9 11

;(adjoin-set 9 (adjoin-set 3 (adjoin-set 7 (make-tree 5 null null))))


(define (show-tree seq)
  (if (= 1 (length seq))
      (make-tree (car seq) null null)
      (adjoin-set (car seq) (show-tree (cdr seq)))))
  


(show-tree '(11 9 5 1 3 7))
(show-tree '(11 9 5 7 1 3))
(show-tree '(11 7 9 1 3 5)) 




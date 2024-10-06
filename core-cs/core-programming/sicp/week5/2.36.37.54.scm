#lang simply-scheme

;understanding:
;accumulate list of lists in a list

;strategy:
;enumerate - elements of lol
;filter - void, null?
;map - cars, cdrs
;accumulate +, 0

;implimentation
(define (new-accumulate op init seq)
  (if (null? seq)
      init
      (op (car seq)
          (new-accumulate op init (cdr seq)))))

(define (accumulate-n op init seqs)
  (if (null? (car seqs))
      null
      (cons (new-accumulate op init (map(lambda(x)(car x)) seqs))
            (accumulate-n op init (map(lambda(x)(cdr x))seqs)))))




;evaluation 
(define lol
  '((1 2 3)(4 5 6)(7 8 9)(10 11 12)))



;2.37
;understanding:...


;strategy:
;a
;123 2
;123 4 
;123 6

;1 * 2, 2 * 4, 3 * 6
;
;
;
;b

;c
;'((1 2 3 4)
;  (1 2 3 4))
;'((1 1)(2 2)(3 3)(4 4))
;implimentation
(define v1
  (list 1 2 3 4))

(define m1
  '((1 2 3 4)
    (1 2 3 4)
    (1 2 3 4)))

(define m2
  '((1 2 3 4)
    (1 2 3 4)
    (1 2 3 4)
    (1 2 3 4)))

(define (dot-product row vector)
  (apply + (map * row vector)))

(define (matrix-*-vector matrix vector)
  (map (lambda(row)(dot-product vector row))matrix))


(define (transpose mat)
  (accumulate-n cons '() mat))

(define (matrix-*-matrix matrix1 matrix2)
  (map (lambda(row)(matrix-*-vector (transpose matrix1) row)) matrix2))

;evaluation

;2.38
;understanding:
;accumulate - folds right, i.e new accumulate above


;strategy:



;implimentation
(define (fold-left op initial sequence)
  (define (iter result rest)
    (if (null? rest)
        result
        (iter (op result (car rest))
              (cdr rest))))
  (iter initial sequence))

;(fold-left list null (list 1 2 3))
;(new-accumulate list null (list 1 2 3))


;evaluation
;+ * are associative, / list are not



;2.54
;understanding
;to lists are said to be equal if they contain equal elements arranged in the same order


;strategy:
;base case:
; -> #t

;base case1:
;both lists are empty -> #f

;base case2:
;list and notlist
;notlist and list
;list and list and not atoms not equal -> #f

;recursive case:
;if both lists call with and cars cdrs
;
;

;signal flow:
;enumerate: roots and subtrees
;filter: list?
;map: apply recursion on lists i.e equal1? or apply direct eq? on atoms 
;accumulate: and #t

;implimentation
(define (equal1? tree1 tree2)
  (cond
    ((and (null? tree1) (null? tree2))#t)
    ((or(and(list? tree1)(not(list? tree2)))
        (and(not(list? tree1))(list? tree2))
        (and(and(not(list? tree1))
                (not(list? tree2)))
            (not(eq? tree1 tree2))))#f)
    ((and (list? tree1) (list? tree2))
     (and (equal1? (car tree1)(car tree2))
          (equal1? (cdr tree1) (cdr tree2))))
    (else #t)))
     
;evaluation
(trace equal1?)
(equal1? (list 2 (list 2 5)) (list 2 (list 2 3)))

  
  




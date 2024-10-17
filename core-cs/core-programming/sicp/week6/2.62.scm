#lang simply-scheme

;2.62
;understanding:

;a union set of A and B are all elements from set A and set B
;{1,2,3} {4,5,6} 
;union {1,2,3,4,5,6}

;domain two unique ordered list(why? because a set contains uniq values) - 2 lists
;range union set - i.e. 1 list

;if an element from set1 is less then an element from set2
;then the element from set1 isnt contained in set2
;if an element from set2 is less then an element from set1
;then the element from set2 isnt in set1

;strategy:

;thinking in base cases 
;base case: null? set1 then set2; null? set2 then set1
;recursive case: x1 = x2 then pair x1 or x2; x1 < x2 then pair x1 cdr set1; x2 < x1 pair x2 cdr set2

;thinking in signal flow 
;input: domain => set1 set2 i.e lists, range => union set i.e list
;enumerate: list elements 
;filter?: (= x1 x2)(< x1 x2)(< x2 x1)
;map: void 
;accumulate: cons set1 or cons set2



;implimentation:
(define (union-set set1 set2)
  (cond
    ((null? set1) set2)
    ((null? set2) set1)
    (else
     (let ((x1 (car set1)) (x2 (car set2)))
       (cond ((= x1 x2)
              (cons x1 (union-set (cdr set1)
                                  (cdr set2))))
             ((< x1 x2)
              (cons x1 (union-set (cdr set1) set2)))
             ((< x2 x1)
              (cons x2 (union-set set1 (cdr set2)))))))))
              

;from the book 
(define (intersection-set set1 set2)
  (if (or (null? set1) (null? set2))
      '()
      (let ((x1 (car set1)) (x2 (car set2)))
        (cond ((= x1 x2)
               (cons x1 (intersection-set (cdr set1)
                                          (cdr set2))))
              ((< x1 x2)
               (intersection-set (cdr set1) set2))
              ((< x2 x1)
               (intersection-set set1 (cdr set2)))))))

;evaluation:
(union-set '(7 8 9 10 11)'(5 6 7 8 9))
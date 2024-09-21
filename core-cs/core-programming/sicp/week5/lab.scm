#lang simply-scheme



;ex 2.25
;understanding:
;deep list, each element is either an element itself or a list of elements

;strategy
;
;
;

;implimentation
(define dlist-ex '(1(2(7))))



(define (find7 dlist)
  (cond
    ((eq? dlist 7)7)
    ((null? dlist)#f)
    ((list? dlist)
     (let ((accum (find7 (car dlist))))
       (if (not (null? accum))
           accum
           (find7 (cdr dlist)))))
    (else
     null)))

;(trace find7)

;2.53
;(list 'a 'b 'c)
;(list (list 'george))
;(cdr '((x1 x2) (y1 y2)))
;(cadr '((x1 x2) (y1 y2)))
;(pair? (car '(a short list)))
;(memq 'red '((red shoes) (blue socks)))
;(memq 'red '(red shoes blue socks))


;ex 2.55
;it return ', because, ' in context of a list is the part of that list a literal ', so if car returns first
;element, it could be anything even '



;2.27 deep reverse

;understanding, deep reverse a list of lists of any depth using/modyfing reverse func 
;(define x (list 1 2 (list 3 (list 3 4))))
;x
;((1 2) (3 4))
;(reverse x)
;((3 4) (1 2))
;(deep-reverse x)
;((4 3) (2 1))
;
;strategy:
;enumerate: elements
;filter: list?
;map: apply deepreverse to each sublist
;accumulate: append results, in regular recur and tree recur cases

(define (reverse l)
  (cond
    ((null? l)null)
    (else
     (append(reverse (cdr l))(list(car l))))))

(define (deepreverse l)
  (cond
    ((null? l) null)
    ((list? (car l))
    (append(deepreverse(cdr l))(list(deepreverse(car l)))))
    (else
     (append(deepreverse(cdr l))(list(car l))))))

;(trace reverse)
;(define x2 (list 1 2 (list 1 2 (list 1 2))))




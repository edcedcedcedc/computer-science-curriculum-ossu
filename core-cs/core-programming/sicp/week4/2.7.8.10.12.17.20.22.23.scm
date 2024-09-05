#lang simply-scheme
;2.7



;constructor 
(define (make-interval a b) (cons a b))


;understanding: in interval convention [x,y] x is the lower bound y is the upperbound
;strategy:
;selectors
(define (upper-bound interval)
  (cdr interval))

(define (lower-bound interval)
  (car interval))

;code from the book
(define (mul-interval x y)
  (let ((p1 (* (lower-bound x) (lower-bound y)))
        (p2 (* (lower-bound x) (upper-bound y)))
        (p3 (* (upper-bound x) (lower-bound y)))
        (p4 (* (upper-bound x) (upper-bound y))))
    (make-interval (min p1 p2 p3 p4)
                   (max p1 p2 p3 p4))))


(define (div-interval x y)
  (mul-interval
   x
   (make-interval (/ 1.0 (upper-bound y))
                  (/ 1.0 (lower-bound y)))))


(define (add-interval x y)
  (make-interval (+ (lower-bound x) (lower-bound y))
                 (+ (upper-bound x) (upper-bound y))))

;with no respect to data abstraction
;(add-interval (cons 3 4) (cons 3 4))

;with respect to data abstraction
(define interval1 (cons 3 4))
(define interval2 (cons 3 4))
;(add-interval interval1 interval2)


;2.8
;understanding:define a sub interval


;strategy:
;the same as add interval but sub

;implimentation:
(define (sub-interval x y)
  (make-interval (- (lower-bound x) (lower-bound y))
                 (- (upper-bound x) (upper-bound y))))

;evaluation:


;2.10
;understanding:modify div interval to get an error when 0


;strategy:
;condition to check when 0

;implimentation:
(define (div-interval-zero x y)
  (if (not (and(equal? (car y) 0)
               (equal? (cdr y) 0)))
      (mul-interval
       x
       (make-interval (/ 1.0 (upper-bound y))
                      (/ 1.0 (lower-bound y))))
      '(Cannot divide by 0)))

;evaluation:



;2.12
;understanding:
;define a constructor make center percent,
;take a center and a percentage tolerance and produces the desired interval
;define a selector percent 
;strategy:
;

;implimentation:
(define (make-center-width c w)
  (make-interval (- c w) (+ c w)))

(define (percent p) (/ p 100))

(define (make-center-percent c p)
  (let ((w (* c (percent p))))
    (make-interval (- c w) (+ c w))))

(define (center i)
  (/ (+ (lower-bound i) (upper-bound i)) 2.0))

(define (width i)
  (/ (- (upper-bound i) (lower-bound i)) 2.0))

;evaluation:
;(center (cons 3 4))
;(make-center-percent (center (cons 3 4)) 1)

;2.17
;understanding:
;define a list that returns car of the last pair

;strategy:
;

;implimentation:
;recursive
(define (last-pair lst)
  (if (= 1 (length lst))
      (car lst)
      (last-pair (cdr lst))))
;evaluation:



;2.20
;understanding:
;define a procedure that returns nums of the same parity as the first argument
;the procedure should take any nums or arguments with dotted notation

;strategy:
;

;implimentation:
;recursive
(define (same-parity . args)
  (let ((first-element-ref (remainder (car args) 2)))
    (define (recur args)
      (if (null? args)
          null
          (append (if (= (remainder (car args) 2) first-element-ref)
                    (list(car args))
                    '())
                (recur (cdr args)))))
    (recur args))) 
;evaluation:
;<<<(same-parity 2 3 4 5 6 7)
;>>>'(2 4 6)

;2.22
;understanding:
;modify 2.21 and explain why square list iter returns the squared list in reverse order 

;strategy:
;

;implimentation:
;2.21
(define (square-list items)
  (if (null? items)
      null
      (cons (* (car items)(car items))
            (square-list (cdr items)))))

(define (square-list-map items)
  (map (lambda (x)(* x x)) items))

(define (my-map fn lst)
  (if (null? lst)
      null
      (cons (fn (car lst))(my-map fn (cdr lst)))))

;(my-map (lambda (x)(* x x)) (list 1 2 3 4))

;(square-list (list 1 2 3 4))
;(square-list-map (list 1 2 3 4))

;actual exercise

(define (square x)
  (* x x))
(define (square-list-iter items)
  (define (iter things answer)
    (if (null? things)
        answer
        (iter (cdr things)
              (append answer (list (square (car things)))))))
  (iter items null))

;why this happens ?
;this happens because the current-answer is sticked always to the front
;you constantly add a new item in from of a formed list, square 1 => '(1), square 2 = > '(4 1) ...

;evaluation
;(square-list-iter (list 1 2 3 4))



;2.23
;understanding:
;implement for-each 
;domain fn an lst, range mutated list 

;strategy:
;

;implimentation:
(define (my-for-each fn lst)
  (if (null? lst)
      (void)
      (begin (fn(car lst))
             (my-for-each fn (cdr lst)))))
  
;evaluation:
(my-for-each square (list 1 2 3))
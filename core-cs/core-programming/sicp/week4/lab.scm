#lang simply-scheme
;ex 3
(define (make-rational num den)
  (cons num den))
(define (numerator rat)
  (car rat))
(define (denominator rat)
  (cdr rat))
(define (*rat a b)
  (make-rational (* (numerator a) (numerator b))
                 (* (denominator a) (denominator b))))
(define (print-rat rat)
  (word (numerator rat) '/ (denominator rat)))


(print-rat (make-rational 2 3))
(print-rat (*rat (make-rational 2 3) (make-rational 1 4)))


;ex 5
;understanding:
;add two rat nums

;strategy:
;a/b + c/d = ad+cb/bd

;implimentation
(define (+rat a b)
  (make-rational (+ (* (numerator a)(denominator b))
                    (* (numerator b)(denominator a)))
                 (* (denominator a)(denominator b))))

;evaluation:
(print-rat (+rat (make-rational 1 2) (make-rational 3 4)))


;ex7
;understanding:
;sentences are special cases of lists

(define x '(a (b c) d))
(car x)
(cdr x)
(car (cdr x))
(word 'hello)


;2.2
;understanding:
;Consider the problem of representing line
;segments in a plane. Each segment is represented as a pair
;of points: a starting point and an ending point. Define a
;constructor make-segment and selectors start-segment and
;end-segment that define the representation of segments in
;terms of points. Furthermore, a point can be represented
;as a pair of numbers: the x coordinate and the y coordinate. Accordingly, specify a constructor make-point and
;selectors x-point and y-point that define this representation. Finally, using your selectors and constructors, define a
;procedure midpoint-segment that takes a line segment as
;argument and returns its midpoint (the point whose coordinates are the average of the coordinates of the endpoints).
;to try your procedures, you’ll need a way to print points:
;
;
;
;segment is a pair of points
;point a pair of x,y coordinates 

;strategy:
;make-segment
;selectors start-segment end-segment
;make-point
;selectors x-point y-point
;midpoint

;makesegment -> pointx, pointy
;pointx -> (x,y) -> makepoint
;pointy -> (x1,y1) -> makepoint

;implimentation
(define (make-point x y)(cons x y))

(define (make-segment x y)(list x y))

(define (start-segment p)(car p))
(define (end-segment p) (car(cdr p)))

(define (x-point p) (car p))
(define (y-point p) (cdr p))

(define (midpoint s)
  (make-point
   (/(+ (x-point (start-segment s))
        (x-point (end-segment s)))2)
   (/(+ (y-point (start-segment s))
        (y-point (end-segment s)))2)))

(define my-segment (make-segment (make-point 2 2)(make-point 3 4)))

my-segment
(define (print-point p)
  (newline)
  (display "(")
  (display (x-point p))
  (display ",")
  (display (y-point p))
  (display ")"))

;evaluation:
;(print-point (midpoint my-segment))



;2.3
;understanding:
;Exercise 2.3: Implement a representation for rectangles in
;a plane. (Hint: You may want to make use of Exercise 2.2.) In
;terms of your constructors and selectors, create procedures
;that compute the perimeter and the area of a given rectangle.
;Now implement a different representation for rectangles. Can you design your system with suitable abstraction
;barriers, so that the same perimeter and area procedures
;will work using either representation?


;strategy
;I am going to use a simple width and height strategy without linear algebra thing with vectors.
;
;
;
;
;
;top-right
;bottom-left
;x,y
;
;(x,y1);---------(x1,y1)
       ;        ;
       ;        ;
       ;        ;
 ;(x,y);---------(x1,y)

;perimeter
;(x1 - x) - width
;(y1 - y) - height
;p = 2(width + height)
;area
;width*height

;implimentation
;0.1
(define (bottom-left x y)
  (make-point x y))
(define (bottom-right x1 bottom-left)
  (make-point x1 (y-point bottom-left)))
(define (top-left bottom-left y1)
  (make-point (x-point bottom-left) y1))

(define (width bottom-left bottom-right)
  (make-segment bottom-left bottom-right))
(define (height bottom-left top-left)
  (make-segment bottom-left top-left))

(define (width-segment r) (car r))
(define (height-segment r) (car (cdr r)))

(define (rectangle bottom-left bottom-right top-left)
  (list
   (width bottom-left bottom-right)
   (height bottom-left top-left)))

(define (perimeter r)
  (* 2 (+ (abs (- (x-point(start-segment(width-segment r)))
                  (x-point(end-segment(width-segment r)))))
          (abs (- (y-point(start-segment(width-segment r)))
                  (y-point(end-segment(height-segment r))))))))

(define (area r)
  (* (abs (- (x-point(start-segment(width-segment r)))
             (x-point(end-segment(width-segment r)))))
     (abs (- (y-point(start-segment(width-segment r)))
             (y-point(end-segment(height-segment r)))))))

(define (print-rectangle r)
  (display "Rectangle: ")
  (display r)
  (newline)
  (display "Perimeter: ")
  (display (perimeter r))
  (newline)
  (display "Area: ")
  (display (area r)))
  
;evaluation
;0.1
(define origin (bottom-left 0 2))
(define my-rectangle
  (rectangle origin
             (bottom-right 3 origin)
             (top-left origin 4)))

(print-rectangle my-rectangle)


;ex 2.4
;understanding:
;: Here is an alternative procedural representation of pairs. For this representation, verify that (car (cons
;x y)) yields x for any objects x and y.
;What is the corresponding definition of cdr? (Hint: To verify that this works, make use of the substitution model of
;Section 1.1.5.)

(define (cons1 x y)
  (lambda (m) (m x y)))

(define (car1 z)
  (z (lambda (p q) p)))

;strategy:
;
;
;
;implimentation:
(define (cdr1 z)
  (z (lambda (p q) q)))

;evaluation:
(cdr1 (cons1 2 3))



;2.18
;understanding:
;Define a procedure reverse that takes a list
;as argument and returns a list of the same elements in reverse order:
;(reverse (list 1 4 9 16 25))
;(25 16 9 4 1)

;strategy:
;recur
;cons

;implimentation:

(define (reverse l)
  (if (null? l)
      null
      (append(reverse (cdr l))(list(car l)))))

(reverse (list 1 2 3 4))


  






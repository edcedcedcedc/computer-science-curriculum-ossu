#lang simply-scheme

;toy problem example
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;

(define make-kv-pair cons)
(define kv-key car)
(define kv-value cdr)
(define (sort-into-buckets fn)
  fn)

(define (mapreduce mapper reducer base-case data) ; handwavy approximation
  (groupreduce reducer base-case
               (sort-into-buckets (map mapper data))))

(define (groupreduce reducer base-case buckets)
  (map (lambda (subset) (make-kv-pair
                         (kv-key (car subset))
                         (reduce reducer base-case (map kv-value subset))))
       buckets))

;raw data
;
;
;
;
;
;
(define mt1 '((cs61a-xc . 27) (cs61a-ya . 40) (cs61a-xw . 35)
                              (cs61a-xd . 38) (cs61a-yb . 29) (cs61a-xf . 32)))
(define mt2 '((cs61a-yc . 32) (cs61a-xc . 25) (cs61a-xb . 40)
                              (cs61a-xw . 27) (cs61a-yb . 30) (cs61a-ya . 40)))
(define mt3 '((cs61a-xb . 32) (cs61a-xk . 34) (cs61a-yb . 30)
                              (cs61a-ya . 40) (cs61a-xc . 28) (cs61a-xf . 33)))


;sorting
;
;
;
;
;
;
;(sort-into-buckets (append mt1 mt2 mt3))

;result
;
;(((cs61a-xb . 40) (cs61a-xb . 32))
;((cs61a-xc . 27) (cs61a-xc . 25) (cs61a-xc . 28))
;((cs61a-xd . 38))
;((cs61a-xf . 32) (cs61a-xf . 33))
;((cs61a-xk . 34))
;((cs61a-xw . 35) (cs61a-xw . 27))
;((cs61a-ya . 40) (cs61a-ya . 40) (cs61a-ya . 40))
;((cs61a-yb . 29) (cs61a-yb . 30) (cs61a-yb . 30))
;((cs61a-yc . 32)))



;word counting

(map (lambda (wd) (list (make-kv-pair wd 1))) '(cry baby cry))

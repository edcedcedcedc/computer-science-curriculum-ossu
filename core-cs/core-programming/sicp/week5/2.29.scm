#lang simply-scheme


;ex 2.29
;understanding
;a binary list
;mobile - left right branches
;branch - length structure(mobile)
;length - number
;structure - a number or another mobile

;strategy:
;part a

;part b
;predicates
;mobile? -  list of two lists #t
;branch? -  list of list and or number/list #t

;base case -> 0
;recursive case -> +  
;          mobile
;    branch      branch
;number mobile   number number

;enumerate
;filter -> mobile, branch
;map -> void map
;accumulate -> +,0

;implimentation:
    
(define (make-mobile left right)
  (list left right))

(define (make-branch length structure)
  (list length structure))

(define (left-branch mobile)
  (car mobile))
(define (right-branch mobile)
  (cadr mobile))

(define (branch-length branch)
  (car branch))
(define (branch-structure branch)
  (cadr branch))

(define (mobile? mobile)
  (and
   (list? mobile)
   (= (length mobile) 2)
   (list?(left-branch mobile))
   (list?(right-branch mobile))))

(define (branch? branch)
  (and
      (list? branch)
      (= (length branch) 2)
      (number? (left-branch branch))
      (or(number?(right-branch branch))
         (mobile? (right-branch branch)))))

(define dummy-function (lambda (x y)x y))

(define (total-weight mobile)
  (cond
    ((null? mobile) 0)
    ((mobile? mobile)
     (+ (total-weight (left-branch mobile))
        (total-weight (right-branch mobile))))
    ((branch? mobile)
     (+ (total-weight(branch-length mobile))
        (total-weight(branch-structure mobile))))
    (else
     mobile)))

(define my-mobile
  (make-mobile
   (make-branch 3 (make-mobile
                   (make-branch 3 4)
                   (make-branch 1 2)))
   (make-branch 5 9)))

(total-weight my-mobile)
                

#lang simply-scheme


;ex 2.29
;understanding
;a binary list
;mobile - left right branches
;branch - length structure
;length - number
;structure - a number or another mobile

;strategy:
;part a

;part b
;predicates
;mobile? -  list of two lists #t
;branch? -  list of list and or number/list #t

;base case -> 0, mobile
;recursive case -> +

;          mobile
;    branch      branch
;number mobile   number number

;enumerate -> weights 
;filter -> mobile, branch
;map -> void map
;accumulate -> +,0

;part c
;          mobile
;    branch      branch
;number mobile   number number
;torque of a branch = length of the branch * total weight


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
   (pair? mobile)
   ;(= (length mobile) 2)
   (pair?(left-branch mobile))
   (pair?(right-branch mobile))))

(define (branch? branch)
  (and
      (pair? branch)
      ;(= (length branch) 2)
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
     (+ (branch-length mobile)
        (total-weight(branch-structure mobile))))
    (else
     mobile)))

(define mobile1
  (make-mobile
   (make-branch 3 (make-mobile
                   (make-branch 3 4)
                   (make-branch 1 2)))
   (make-branch 5 9)))

(define mobile2 (make-mobile
                   (make-branch 3 4)
                   (make-branch 1 2)))

(define mobile3 (make-mobile
                   (make-branch 3 4)
                   (make-branch 3 4)))

(define (torque branch-length total-weight)
  (* branch-length total-weight))

(define (balanced? mobile)
  (and (mobile? mobile)
       (if (eq? (torque (branch-length(left-branch mobile))
                   (total-weight(branch-structure(left-branch mobile))))
                (torque (branch-length(right-branch mobile))
                   (total-weight(branch-structure(right-branch mobile)))))
      #t
      #f)))

;part d
;understanding:
;cons constructor for pairs, append an atom or list to the beginning of another list 
;strategy:
;so the key point is that if you change the data representation you change the constructors selectors predicates
;but not operations
;
;
(define (make-mobile1 left right) (cons left right))
(define (make-branch1 length structure)
  (cons length structure))

(define mobile4
  (make-mobile1
   (make-branch1 3 (make-mobile1
                   (make-branch1 3 4)
                   (make-branch1 1 2)))
   (make-branch1 5 9)))

(left-branch mobile4)
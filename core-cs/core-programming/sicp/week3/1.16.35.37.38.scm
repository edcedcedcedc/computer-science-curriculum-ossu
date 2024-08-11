#lang simply-scheme

(define (square x)(* x x))

(define (fast-expt b n)
  (cond ((= n 0) 1)
        ((even? n) (square (fast-expt b (/ n 2))))
        (else (* b (fast-expt b (- n 1))))))

(define (regular-expt b n)
  (if (= n 0)
      1
      (* b (regular-expt b (- n 1)))))

(define (iterative-expt b n)
  (define (iter a b n)
    (cond
      ((= n 0) a)
      ((even? n) (iter a (* b b) (/ n 2)))
      (else (iter (* a b) b (- n 1)))))
  (iter 1 b n))

(iterative-expt 2 5)
(trace iterative-expt)
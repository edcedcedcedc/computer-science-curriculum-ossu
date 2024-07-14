#lang simply-scheme

(define (sum-integers a b)
  (if (> a b)
      0
      (+ a (sum-integers (+ a 1) b))))

(trace sum-integers)

(sum-integers 2 3)


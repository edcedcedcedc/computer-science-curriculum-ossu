#lang sicp

(define (front-ptr queue) (car queue))
(define (rear-ptr queue) (cdr queue))
(define (set-front-ptr! queue item)
  (set-car! queue item))
(define (set-rear-ptr! queue item)
  (set-cdr! queue item))

(define (empty-q? queue)
  (null? (front-ptr queue)))

(define (front-q queue)
  (if (empty-q? queue)
      (error "FRONT called with an empty queue" queue)
      (car (front-ptr queue))))

(define (insert-q! queue item)
  (let ((new-pair (cons item '())))
    (cond ((empty-q? queue)
           (set-front-ptr! queue new-pair)
           (set-rear-ptr! queue new-pair)
           (print-q queue))
          (else
           (set-cdr! (rear-ptr queue) new-pair)
           (set-rear-ptr! queue new-pair)
           (print-q queue)))))

(define (delete-q! queue)
  (cond ((empty-q? queue)
         (error "DELETE! called with an empty queue" queue))
        (else (set-front-ptr! queue (cdr (front-ptr queue)))
              (print-q queue))))

(define (print-q queue)
  (car queue))

(define (make-q)(cons '() '()))

#lang simply-scheme

;understanding
;Write a procedure substitute that takes three arguments: a list, an old word, and a
;new word. It should return a copy of the list, but with every occurrence of the old word
;replaced by the new word, even in sublists. For example:
;> (substitute ’((lead guitar) (bass guitar) (rhythm guitar) drums)
;’guitar ’axe)
;((lead axe) (bass axe) (rhythm axe) drums
;
;
;strategy:
;map

;implimentation:

(define (substitute lst old new)
  (map (lambda (x)
         (cond
           ((and (= (length (list x)) 1)(equal? old x))new)
           ((equal? old (car x)) (cons new (cdr x)))
           ((equal? old (car (cdr x)))(append (list(car x))(list new)))
           (else
            x))) lst))
;evaluation
;(substitute '((lead guitar) (bass guitar) (rhythm guitar) 'guitar) 'guitar 'axe)

             

;understanding
;Now write substitute2 that takes a list, a list of old words, and a list of new words; the
;last two lists should be the same length. It should return a copy of the first argument, but
;with each word that occurs in the second argument replaced by the corresponding word of
;the third argument:
; (substitute2 ’((4 calling birds) (3 french hens) (2 turtle doves))
;’(1 2 3 4) ’(one two three four))
;((four calling birds) (three french hens) (two turtle doves))

;
;strategy:
;recur
;map
;compare

;implimentation:

;examples from the book reimplemented 
(define (item-vector items item init)
  (define (iter items a)
    (if (equal? (car items) item)
        a
        (iter (cdr items) (+ a 1))))
  (iter items init))

(define (substitute2 lst old-lst new-lst)
  (if (null? lst)
      null
      (append
       (list (map (lambda (x)
                    (cond
                      ((member? x old-lst)
                       (item (item-vector old-lst x 1) new-lst))
                      (else
                       x)))(car lst)))(substitute2 (cdr lst) old-lst new-lst))))
        
            
;evaluation              
;(item (item-vector (list 'a 'b 'c) 'b 1)(list 'a 'b 'c))
(substitute2 '((4 calling birds) (3 french hens) (2 turtle doves))
             '(1 2 3 4) '(one two three four))


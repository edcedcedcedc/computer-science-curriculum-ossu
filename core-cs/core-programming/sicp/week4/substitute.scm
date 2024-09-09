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
;0.1
;map
;0.2
;first base case
;list?
;second inner base case, map
;recur

;implimentation:
(define (substitute lst old new)
   (cond ((equal? lst old) new)
             ((list? lst)(map(lambda(x)(substitute x old new)) lst))
             (else lst)))

;(substitute '((lead guitar guitar) drums (lead guitar(lead guitar(lead guitar)))) 'guitar 'axe)
;(substitute '((4 calling birds birds) (3 french hens) (2 turtle doves)) 'guitar 'axe)
  
;evaluation
;(substitute '((lead guitar) (bass guitar) (rhythm guitar) drums) 'guitar 'axe)
;0.2
;(list 'lead 'guitar) = (cons 'lead (cons 'guitar null)) = '(lead guitar)
;(substitute '((lead guitar player) (bass guitar player) (rhythm guitar player) (drum player)) 'guitar 'axe)
;'((lead guitar) drums)


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
;0.1
;recur
;map
;compare

;0.2
;recur base case
;map
;recur
;compare
;map base case

;implimentation:

;examples from the book reimplemented 
(define (item-vector items item init)
  (define (iter items a)
    (cond
      ((null? items) -1)
      ((equal? (car items) item)a)
      (else
        (iter (cdr items) (+ a 1)))))
  (iter items init))
;0.1
;this works only for list of lists 
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
;0.2
;this works for any depth list
(define (substitute22 lst old new)
  (cond ((and(word? lst)(member? lst old))
         (item (item-vector old lst 1) new))
        ((list? lst)(map(lambda(x)(substitute22 x old new)) lst))
        (else lst)))       
            
;evaluation
;0.1
;(item (item-vector (list 'a 'b 'c) 'b 1)(list 'a 'b 'c))
;0.2
;(substitute22 '((4 calling birds birds (birds birds (birds))) (3 french hens) (2 turtle doves))
 ;           '(1 2 3 4) '(one two three four))
#lang simply-scheme

;3.38
;Peter: (set! balance (+ balance 10))
;Paul: (set! balance (- balance 20))
;Mary: (set! balance (- balance (/ balance 2)))
;
;a)
;100 +10 -20 /2 = 45
;100 +10 /2 -20 = 35
;100 -20 +10 /2 = 45
;100 -20 /2 +10 = 50
;100 /2 +10 -20 = 40
;100 /2 -20 +10 = 40
;
;
;b)...
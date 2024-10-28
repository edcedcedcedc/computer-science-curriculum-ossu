#lang simply-scheme

;attachtag
;if number?
;contents
;else
;cons typetag contents

;typetag
;if number?
;'scheme-number
;else
;car datum

;contents
;pair?
;cdr
;else
;car -> scheme-number

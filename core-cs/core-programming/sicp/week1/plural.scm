#lang simply-scheme

(define (plural wd)
  (cond ((member?(or(word(bl(last wd))(last wd))
                    (last wd))'(s ss sh ch x z))
         (word wd 'es))
        ((and(member?(last(bl wd))'(a e i o u))
             (equal? 'y (last wd)))
         (word wd 's))
        ((equal? 'y (last wd))
         (word(bl wd)'ies))
        (else
         (word wd 's))))

(trace plural)

(plural 'car)
(plural 'boy)
(plural 'baby)

;sure this program might be extended
;but in terms of current requirements its enough


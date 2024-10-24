#lang simply-scheme

;understanding:
;division - a set of records in a single file
;record - info about employees, keyed on employees names
;record. - more info keyed on address and salary

;in the original example
;type/op
;square/area
;square/perimeter
;circle/area
;circle/perimeter 

;type/op
;division-A, employee-A/get-record,get-salary
;division-B, employee-C/get-record,get-salary

;(define (area shape)
;  (operate 'area shape))

;(define (perimeter shape)
;  (operate 'perimeter shape))

;(put 'square 'area (lambda (s) (* s s)))
;(put 'circle 'area (lambda (r) (* pi r r)))


;strategy:
;define a data directed programming table with type/operation
;define ddp database
;define a get, find-division, find-employee procedures
;define get-salary, get-record

;implimentation:

(define type-tag car)
(define contents cadr)

(define ddp-database                                    
  (list
   (list 'Division-A 'Samuel-Fastgpu 'get-record
         (lambda(x)
           (list'(name Samuel)
                '(surname Fastgpu)
                '(address (Dubai, Burj Khalifa Tower, floor 99, ap 1666))
                '(salary 30000-usd))))
   (list 'Division-A 'Samuel-Slowgpu 'get-salary (lambda()'(salary 30000-usd)))
   (list 'Division-B 'John-Hackerton 'get-record 
         (lambda(x)(list'(name John)
                        '(surname Hackerton)
                        '(address (Dummy, Dummy dummy, dummy 9, ap 1666))
                        '(salary 50000-usd))))
   (list 'Division-B 'Steve-Macbook 'get-salary (lambda(x)'(salary 50000-usd)))
   (list 'Division-B 'Steve-Macbook 'get-record (lambda(x)(list'(name Steve)
                                                              '(surname Macbook)
                                                              '(address (Dummy, Dummy dummy, dummy 9, ap 1666))
                                                              '(salary 50000-usd))))))

;;this database to me seems like a message passing instead of ddp
;;it has intelligent data types that dispatch on operation name
(define message-passing-database
  (list
   (list 'Division-A                                      
         (list 'Samuel-Fastgpu 'get-record 'get-salary
               (lambda(x)
                 (cond
                   ((eq? x 'get-salary)'(salary 30000-usd))
                   ((eq? x 'get-record)(list'(name Samuel)
                                            '(surname Fastgpu)
                                            '(address (Dubai, Burj Khalifa Tower, floor 99, ap 1666))
                                            '(salary 30000-usd)))
                   (else
                    (error "Unknown operator for type")))))
         (list 'John-Hackerton 'get-record 'get-salary
               (lambda(x)
                 (cond
                   ((eq? x 'get-salary)'(salary 50000-usd))
                   ((eq? x 'get-record)(list'(name John)
                                            '(surname Hackerton)
                                            '(address (Dummy, Dummy dummy, dummy 9, ap 1666))
                                            '(salary 50000-usd)))
                   (else
                    (error "Unknown operator for type"))))))
   (list 'Division-B
         (list 'Max-Systemdown 'get-record  
               (lambda(x)
                 (cond
                   ((eq? x 'get-salary)'(salary 60000-usd))
                   ((eq? x 'get-record)(list'(name Max)
                                            '(surname Systemdown)
                                            '(address (floor 99, ap 1666))
                                            '(salary 60000-usd)))
                   (else
                    (error "Unknown operator for type")))))
         (list 'Ian-Agilehood  
               (lambda(x)
                 (cond
                   ((eq? x 'get-salary)'(salary 30000-usd))
                   ((eq? x 'get-record)(list'(name Ian)
                                            '(surname Agilehood)
                                            '(address (Dummy data 2, ap 666))
                                            '(salary 30000-usd)))
                   (else
                    (error "Unknown operator for type"))))))))

(define (find-division division database)
  (cond
    ((null? database)
     (error "No such division in the database"))
    ((eq? division (caar database))(cdar database))
    (else
     (find-division division (cdr database)))))



;c
;message passing
(define (find-employee-message-passing employee division)
  (cond
    ((null? division)
     (error "Employee not found"))
    ((eq? employee (caar division))(car division))
    (else
     (find-employee-message-passing employee (cdr division)))))

;data directed
(define (find-employee-ddp employee op database)
  (cond
    ((null? database)#f)
    ((and
      (eq? employee (cadr(car database)))
      (eq? op (caddr(car database)))) database)
    (else
     (find-employee-ddp employee op (cdr database)))))


;my get should return the function that is already applied to operation
;and in operate I only shall invoke it with contents
;message passing get
(define (get obj op)
  (let ((division (find-division (car obj) message-passing-database)))
    (let ((employee (find-employee-message-passing (cadr obj) division)))   
     (cadddr employee))))

;ddp get
(define (get-ddp obj op)
  (let ((employee (find-employee-ddp obj op ddp-database)))
    (if employee
     (car(cdddar employee))
     #f)))


;message passing operate
;the object is invoked with the operation name, that knows about itself 
(define (operate op obj)
  (let ((proc (get obj op)))
    (proc op)))

;data directed operate
(define (operate-ddp op obj)
  (let ((proc (get-ddp (type-tag obj) op)))
    (if proc
        (proc (contents obj))
        (error "Unknown operator for type"))))
                   
;a
(define (get-record obj)
  (operate 'get-record obj))

;b
(define (get-salary obj)
  (operate 'get-salary obj))

;d
;If a new company takes over out team would need to implement
;a put function to append a new employee and division to the central system

;evaluation
;I firstly implimented message passing database without realising it and after I read again message passing topic from the book
;I realised that this seems like it so I made another ddp database above the message-passing database



;data directed programming
(define steve-macbook
  (list 'Steve-Macbook '()))
;(operate-ddp 'get-salary steve-macbook)
;(operate-ddp 'get-zalary steve-macbook)

;mesage passing
(define example-obj
  '(Division-A Samuel-Fastgpu))
;(get-record example-obj)

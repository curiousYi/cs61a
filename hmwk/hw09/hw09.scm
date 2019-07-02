(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign x)
  (cond
    ((> x 0) 1)
    ((= x 0) 0)
    ((< x 0) -1)
  )
)

(define (square x) (* x x))

(define (pow b n)
  (cond
    ((= n 1) (b))
    ((= n 2) (square b))
    ((even? n) (* (square (pow b (/ n 2)))))
    ((odd? n) (* (pow b (- n 1)) b))
  )
)

(define (ordered? s)
  (cond
    (
      (> (length s) 1) 
      (if
        (
          <
          (
            -
            (car s)
            (car (cdr s))
          )
          1
        )
        (ordered? (cdr s))
        #f
      )
    )
    (
      else
      #t
    )
  )
)

(
  define (nullOrPair s)
  (cond
    ((pair? s) #t)
    ((null? s) #t)
    (else #f)
  )
)

(define (nodots s)
  (cond
    ( (pair? s)
      ( cond
        ( (pair? (car s))
          ( cons (nodots (car s)) (nodots (cdr s)))
        )
        ( else
          (cons (car s) (nodots (cdr s)))
        )
      )
    )
    ( (not (nullOrPair s))
      (cons s nil)
    )
    (
      else
      s
    )
  )
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          ((= (car s) v) #t)
          ((> (car s) v) #f)
          (else  (contains? (cdr s) v)
          )
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((contains? s v) s)
          ((null? s) (cons v nil))
          (
            (if (< (length s) 2)
              (if (< (car s) v)
                (cons (car s) (cons v nil))
                (cons v s)
              )
              (if (< (car s) v)
                (if (> (car (cdr s)) v)
                  (cons (car s) (cons v (cdr s)))
                  (cons (car s) (add (cdr s) v))
                )
                (cons v s)
              )
            )
          )
    )
)
(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          (
            (cond
              ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
              ((> (car s) (car t)) (intersect s (cdr t)))
              (else (intersect (cdr s) t))
            )
          )
          (else nil) ; replace this line
    )
)

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          (
            (cond
              ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
              ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
              (else (cons (car s) (union (cdr s) t)))
            )
          )
          (else nil) ; replace this line
          ))

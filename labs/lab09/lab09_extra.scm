;; Extra Scheme Questions ;;


; Q5
(define lst
  'YOUR-CODE-HERE
)

; Q6
(define (composed f g)
  (lambda (x) 
    (f
      (g x)
      )
  )
)

; Q7
(define (remove item lst)
  (if (equal? lst nil)
    ()
    (if (equal? (car lst) item)
        (remove item (cdr lst))
        (cons (car lst) (remove item (cdr lst)))
    )
  )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (if (equal? (min a b) 0)
    (max a b)
    (if (equal? (modulo (max a b) (min a b)) 0)
      (min a b)
      (gcd (min a b) (modulo (max a b) (min a b)))
    )
  )
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
  (if (min (length s) 2)
    s
    (if 
      (equal? 
        (car s)
        (car (cdr s))
      )
      (cons (car s) (cdr (cdr s)))
      s
    )
  )
)

; Q10
(define (substitute s old new)
  'YOUR-CODE-HERE
)

; Q11
(define (sub-all s olds news)
  'YOUR-CODE-HERE
)

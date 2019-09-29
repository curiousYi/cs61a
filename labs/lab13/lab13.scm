;; Scheme ;;
//TO-DO figure out how to delay execution and just return the function
(define (compose-all funcs)
  (if nil? (cdr funcs)
    ((car funcs) 
    ((car funcs ( (compose-all( funcs))))
  )
  nil
)

(define (deep-map fn s)
  (cons 
    (if list? (car s)
      (deep-map fn (car s))
      (fn (car s))
    )
    (if nil? (cdr s)
      nil
      (deep-map fn (cdr s))
    )
  )
)

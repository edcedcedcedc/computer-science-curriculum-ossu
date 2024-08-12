#lang simply-scheme

;goal/understanding:
;
;2 players: customer / dealer
;
;To be dealt a set of cards that comes as close
;to 21 as possible without going over "busting"
;
;A card is represented as a word -
;10s - ten of spades
;a, j, q, k - ace, jack, queen, king
;
;picture cards are worth 10 points
;ace is worth 1 or 11 at the player's option
;
;each players is dealt two cards
;with one of the dealer's cards face up
;
;dealer always takes another cards if he has 16 or less
;and always stops with 17 or more
;
;customer can play however he chooses
;but must play before the dealer
;
;if custumer exceeds 21, he loses
;and the dealer doesnt bother to take any cards
;
;if tie neither player wins

(define (twenty-one strategy)
  (define (play-dealer customer-hand dealer-hand-so-far rest-of-deck)
    (cond ((> (best-total dealer-hand-so-far) 21) 1)
	  ((< (best-total dealer-hand-so-far) 17)
	   (play-dealer customer-hand
			(se dealer-hand-so-far (first rest-of-deck))
			(bf rest-of-deck)))
	  ((< (best-total customer-hand) (best-total dealer-hand-so-far)) -1)
	  ((= (best-total customer-hand) (best-total dealer-hand-so-far)) 0)
	  (else 1)))

  (define (play-customer customer-hand-so-far dealer-up-card rest-of-deck)
    (cond ((> (best-total customer-hand-so-far) 21) -1)
	  ((strategy customer-hand-so-far dealer-up-card)
	   (play-customer (se customer-hand-so-far (first rest-of-deck))
			  dealer-up-card
			  (bf rest-of-deck)))
	  (else
	   (play-dealer customer-hand-so-far
			(se dealer-up-card (first rest-of-deck))
			(bf rest-of-deck)))))

  (let ((deck (make-deck)))
    (play-customer (se (first deck) (first (bf deck)))
		   (first (bf (bf deck)))
		   (bf (bf (bf deck))))) )

(define (make-ordered-deck)
  (define (make-suit s)
    (every (lambda (rank) (word rank s)) '(A 2 3 4 5 6 7 8 9 10 J Q K)) )
  (se (make-suit 'H) (make-suit 'S) (make-suit 'D) (make-suit 'C)))

(define (make-deck)
  (define (shuffle deck size)
    (define (move-card in out which)
      (if (= which 0)
	  (se (first in) (shuffle (se (bf in) out) (- size 1)))
	  (move-card (bf in) (se (first in) out) (- which 1)) ))
    (if (= size 0)
	deck
    	(move-card deck '() (random size)) ))
  (shuffle (make-ordered-deck) 52) )



;problem 1 
(define (best-total hand)
  (define picture-cards '(A J Q K))
  (define (card-value card)
    (if (member? (first card) picture-cards)
         11
         (first card)))
  (define (limit value)
    (if (<= value 21)
        value
        (limit (abs (- value 10)))))
  (if (empty? hand)
      0
      (limit(+(best-total (bf hand))(card-value (first hand))))))

;problem 2
(define (stop-at-17 customer-hand dealer-card)
  (if (<(+(best-total customer-hand)
          (best-total (se dealer-card))) 17)
      #t
      #f))

;problem 3 
(twenty-one stop-at-17)

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
  (se (make-suit 'H) (make-suit 'S) (make-suit 'D) (make-suit 'C) 'JOKER-BLACK 'JOKER-RED))

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
  (define jokers '(JOKER-RED JOKER-BLACK))
  (define (card-value card)
    (if (or(member? (first card)picture-cards)
           (member? (first card)jokers)) 
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
  (if (<(best-total (se customer-hand dealer-card))17)
      #t
      #f))

;problem 3
(define (play-n strategy n)
  (define (iter strategy n a)
    (if (= n 0)
        a
        (iter strategy (- n 1)(+ a (twenty-one strategy)))))
  (iter strategy n 0))
      
;problem 4
;understanding:
;takes a card only if the dealer has ace, 7, 8, 9, 10 or picture card showing
;and the customer has less then 17
;or
;the dealer has 2 3 4 5 or 6 showing and customer has less than 12 
;
;strategy:
;A
;3F
;
(define (dealer-sensitive customer-hand dealer-card)
  (if (or (and (member?(first dealer-card)'(A 7 8 9 10))
               (< (best-total customer-hand) 17))
          (and (member? dealer-card '(2 3 4 5 6))
               (< (best-total customer-hand) 12)))
      #t
      #f))

;problem 5
;understanding: generalize problem 2
;strategy:
;domain numbers, range function
;
;(define (stop-at-17 customer-hand dealer-card)
;  (if (<(best-total (se customer-hand dealer-card))17)
;      #t
;      #f))

(define (stop-at n)
  (lambda (customer-hand dealer-card)
    (if (< (best-total (se customer-hand dealer-card)) n) #t #f)))

;problem 6
; On Valentine’s Day, your local casino has a special deal: If you win a round of 21 with
;a heart in your hand, they pay double. You decide that if you have a heart in your hand,
;you should play more aggressively than usual. Write a valentine strategy that stops at
;17 unless you have a heart in your hand, in which case it stops at 19.

(define (valentine customer-hand)
  (if (member? 'H customer-hand)
      (stop-at 19)
      (stop-at 17)))

;problem 7
;Generalize part 6 above by defining a function
;suit-strategy that takes three arguments: a suit (h, s, d, or c),
;a strategy to be used if your hand doesn’t include that suit,
;and a strategy to be used if your hand does include that suit. It should return a strategy
;that behaves accordingly. Show how you could use this function and the stop-at function
;from part 5 to redefine the valentine strategy of part 6.

(define (suit-strategy suit strategy1 strategy2)
  (lambda (customer-hand)
    (if (member? suit customer-hand)
        strategy1
        strategy2)))

(define new-valentine
  (suit-strategy 'H (stop-at 19)(stop-at 17)))


;problem 8
;understanding:
;Define a function majority that takes three strategies as arguments and produces a
;strategy as a result, such that the result strategy always decides whether or not to “hit”
;by consulting the three argument strategies, and going with the majority. That is, the
;result strategy should return #t if and only if at least two of the three argument strategies
;do. Using the three strategies from parts 2, 4, and 6 as argument strategies, play a few
;games using the “majority strategy” formed from these three.
;strategy:
;permutations
;combintations with +
; ;str1 str2 str3
  ;str1 str2 +
  ;srt1 str3 +
  ;str2 str1
  ;str2 str3 +
  ;str3 str1
  ;str3 strt2

(define (majority strategy1 strategy2 strategy3)
  (lambda (customer-hand dealer-card)
    (if (or
         (and (strategy2 customer-hand dealer-card)
              (strategy1 customer-hand dealer-card))
         (and (strategy1 customer-hand dealer-card)
              (strategy3 customer-hand dealer-card))
         (and (strategy2 customer-hand dealer-card)
              (strategy3 customer-hand dealer-card))) #t #f)))

(define majority-strategy
  (majority stop-at-17 dealer-sensitive (valentine '(1A 2C))))

(twenty-one majority-strategy)

;9
;Understanding:
;domain procedure range procedure
;return new strategy that should take one more card then the original strategy

;strategy:
;0.2new strategy should hit if the old stand and stand if the old hit


;implimentation
(define (reckless strategy)
 (lambda (customer-hand dealer-card)
   (if (strategy (butlast customer-hand) dealer-card)
       #f
       #t)))        
;evaluation
;0.1 I consfused the hit with stand,
;and thought that if old strategy hits then new strategy hits as well, but this is wrong
;(define (reckless strategy)
; (lambda (customer-hand dealer-card)
;   (if (strategy (butlast customer-hand) dealer-card)
;       #t
;       #f)))


;problem 10
;Copy your Scheme file to a new file, named joker.scm, before you begin
;this problem. We are going to change the rules by adding two jokers to the deck. A joker
;can be worth any number of points from 1 to 11. Modify whatever has to be modified to
;make this work. (The main point of this exercise is precisely for you to figure out which
;procedures must be modified.) You will submit both this new file and the original,
;nonjoker version for grading. You don’t have to worry about making strategies optimal; just
;be sure nothing blows up and the hands are totalled correctly.



      
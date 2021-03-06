Feature: The dealer for the game of 21

"""
Como repartidor de cartas, cuando la ronda inicie el repartidor debe tener dos cartas.
"""

Scenario: Deal initial cards
  Given a dealer
  When the round starts
  Then the dealer gives itself two cards

"""
Como repartidor dada una mano debo poder sumar las cartas de la mano.
"""

Scenario Outline: Get hand total
  Given a <hand>
  When the dealer sums the cards
  Then the <total> is correct

  Examples: Hands
  | hand          | total |
  | 5,7           | 12    |
  | 5,Q           | 15    |
  | Q,Q,A         | 21    |
  | J,Q,K         | 30    |
  | K,Q,A         | 21    |
  | Q,A           | 21    |
  | A,A,A         | 13    |

"""
como repartidor dado el total de una mano 
debo determinar la jugada que debe realizar según las reglas del juego
"""

Scenario Outline: Dealer plays by the rules
  Given a hand <total>
   when the dealer determines a play
   then the <play> is correct

  Examples: Hands
  | total  | play   |
  | 10     | hit    |
  | 15     | hit    |
  | 16     | hit    |
  | 17     | stand  |
  | 18     | stand  |
  | 19     | stand  |
  | 20     | stand  |
  | 21     | stand  |
  | 22     | stand  |

"""
como repartidor en una ronda debo poder jugar
"""

Scenario: A Dealer can always play
  Given a dealer
  When the round starts
  Then the dealer chooses a play

"""
como jugador dado una mano 
debo determinar cuando separar la mano.
"""

Scenario Outline: Split a players hand
  Given the value of player <hand>
  When the player determines the split
  Then the action of <split> is valid

  Examples: Hands
  | hand          | split |
  | Q,A           | no    |
  | J,Q           | no    |
  | A,A           | yes    |
  | 10,10         | yes    |
  | 8,8           | yes    |


Scenario Outline: Game determines who wins
  Given the values of player and dealer <totalPair>
  When the round is over
  Then the <winner> is who gets 21 

  Examples: Hands
  | totalPair          | winner |
  | 25,18           | dealer    |
  | 20,23           | player    |
  | 19,21           | dealer    |
  | 20,19           | player    |
  | 17,17           | dealer    |
  
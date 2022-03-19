import random

_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def _next_card():
    return random.choice(_cards)

def _hand_total(hand):
    values = [None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    value_map = {k: v for k, v in zip(_cards, values)}

    total = sum([value_map[card] for card in hand if card != 'A'])
    ace_count = hand.count('A')

    for i in range(ace_count, -1, -1):
        if i == 0:
            total = total + ace_count
        elif total + (i * 11) + (ace_count - i) <= 21:
            total = total + (i * 11) + ace_count - i
            break

    return total

def _even_hand(hand):
    verified = any(i==j for i,j in zip(hand, hand[1:]))
    if verified:
        return 'yes'
    else:
        return 'no'

class Player():
    def __init__(self):
        self.hand = []
    def get_even_hand(self):
        return _even_hand(self.hand) 
     
    def determine_split(self, hand):
        return any(i==j for i,j in zip(hand, hand[1:]))


class Dealer():
    def __init__(self):
        self.hand = []
        self.totalPair = []

    def new_round(self):
        self.hand = [_next_card(), _next_card()]

    def get_hand_total(self):
        return _hand_total(self.hand)

    def determine_play(self, total):
        if total < 17:
            return 'hit'
        else:
            return 'stand'
        
    def make_play(self):
        return self.determine_play(self.get_hand_total())
    
    def determine_winner(self, totalPlayer, totalDealer):
        if (totalDealer > totalPlayer) and totalDealer <= 21:
            return 'dealer'
        elif (totalDealer == totalPlayer) and (totalDealer <= 21 and totalPlayer <= 21):
            return 'dealer'
        else:
            return 'player'

    def make_winner(self):
        return self.determine_winner(self.totalPair[0], self.totalPair[1])

    def round_over(self):
        totalPlayer = self.totalPair[0]
        totalDealer = self.totalPair[1]
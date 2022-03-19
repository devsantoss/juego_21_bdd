from twentyone import *
dealer = Dealer()
player = Player()

# Prueba la funcion para generar nueva mano
# Resultado: 2 (True)
def test_new_round():
    dealer.new_round()
    assert len(dealer.hand) == 2

# Prueba para verificar el valor total de una mano
# Resultado: 21 (True)
def test_get_hand_total():
    dealer.hand = ['A','J']
    assert dealer.get_hand_total() == 21

# Prueba para verificar el valor total de una mano
# Resultado: 18 (True)
def test_get_hand_total_noases():
    dealer.hand = ['3','Q','5']
    assert dealer.get_hand_total() == 18

# Prueba para verificar el valor total de una mano
# Resultado: 12 (True)
def test_get_hand_total_2ases():
    dealer.hand = ['A','J','A']
    assert dealer.get_hand_total() == 12

# Prueba para verificar la funcion de jugar
# Resultado: hit (True)
def test_determine_play():
    assert dealer.determine_play(15) == 'hit'

# Prueba para verificar la funcion de hacer jugada
# Resultado: stand (True)
def test_make_play():
    dealer.hand = ['3','Q','5']
    assert dealer.make_play() == 'stand'

def test_determine_split():
    player.hand = ['8','8']
    assert player.determine_split(player.hand) == True

def test_get_even_hand():
    player.hand = ['8','8']
    assert player.get_even_hand() == 'yes'    

def test_determine_winner():
    dealer.totalPair = []
    dealer.totalPair.append(19)
    dealer.totalPair.append(20)
    assert dealer.determine_winner(dealer.totalPair[0], dealer.totalPair[1]) == 'dealer'

def test_make_winner():
    dealer.totalPair = []
    dealer.totalPair.append(19)
    dealer.totalPair.append(24)
    assert dealer.make_winner() == 'player'



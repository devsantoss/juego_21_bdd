from behave import *
from twentyone import *

@given('a dealer')
def step_impl(context):
    context.dealer = Dealer()

@given('a hand {total:d}')
def step_impl(context, total):
    context.dealer = Dealer()
    context.total = total

@given('a {hand}')
def step_impl(context, hand):
    context.dealer = Dealer()
    context.dealer.hand = hand.split(',')

@when('the round starts')
def step_impl(context):
    context.dealer.new_round()

@when('the dealer sums the cards')
def step_impl(context):
    context.dealer_total = context.dealer.get_hand_total()

@when('the dealer determines a play')
def step_impl(context):
    context.dealer_play = context.dealer.determine_play(context.total)

@then('the dealer gives itself two cards')
def step_impl(context):
    assert (len(context.dealer.hand) == 2)

@then('the dealer chooses a play')
def step_impl(context):
    assert (context.dealer.make_play() in ['stand', 'hit'])

@then('the {total:d} is correct')
def step_impl(context, total):
    assert (context.dealer_total == total)

@then('the {play} is correct')
def step_impl(context, play):
    assert (context.dealer_play == play)

# Cuando hacer split de una mano

@given('the value of player {hand}')
def step_impl(context, hand):
    context.player = Player()
    context.player.hand = hand.split(',')

@when('the player determines the split')
def step_impl(context):
    context.player_split = context.player.determine_split(context.player.hand)

@then('the action of split is valid')
def step_impl(context):
    assert (context.player.get_even_hand() in ['yes', 'no'])

# Cuando determinar un ganador
@given('the values of player and dealer {totalPair}')
def step_impl(context, totalPair):
    context.dealer = Dealer()
    context.dealer.totalPair = totalPair.split(',')

@when('the round is over')
def step_impl(context):
    context.dealer.round_over()

@then('the winner is who gets 21')
def step_impl(context):
    assert (context.dealer.make_winner() in ['player', 'dealer'])

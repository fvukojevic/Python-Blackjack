from card import Card
from deck import Deck
from hand import Hand
from chips import Chips


def init_deck(deck):
    signs = ['♠', '♥', '♦', '♣']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cards = [Card(x, y) for x in signs for y in values]
    deck.cards = cards


def init_game():
    while True:
        ans = input('Ready to start the game? Press Yes or No: ')
        if ans.lower() != 'yes' and ans.lower() != 'no':
            print('Invalid input')
        else:
            return True if ans.lower() == 'yes' else False


def ask_hit():
    while True:
        ans = input('Hit again? Press Yes or No: ')
        if ans.lower() != 'yes' and ans.lower() != 'no':
            print('Invalid input')
        else:
            return True if ans.lower() == 'yes' else False


def take_bet(chips):
    while True:
        try:
            bet = int(input('How much money do you want to bet? '))
            if bet > chips.total:
                print(f'Not enough funds, you have {chips.total}')
            else:
                chips.bet = bet
                break
        except ValueError:
            print('Please provide an integer')


def init_hand():
    global deck, playerHand, dealerHand
    playerHand.add_card(deck.hit())
    playerHand.add_card(deck.hit())
    dealerHand.add_card(deck.hit())
    print_hands(playerHand, dealerHand)


def print_hands(playerHand, dealerHand):
    print('PlayerHand: ')
    print(playerHand)
    print('\n')

    print('DealerHand: ')
    print(dealerHand)
    print('\n')


def player_bust(playerHand, dealerHand, chips):
    print('\nPlayer BUST!\n')
    dealer_wins(playerHand, dealerHand, chips)


def dealer_bust(playerHand, dealerHand, chips):
    print('\nDealer BUST!\n')
    player_wins(playerHand, dealerHand, chips)


def player_wins(playerHand, dealerHand, chips):
    print('\nPlayer Wins!\n')
    chips.win_bet()
    print_hands(playerHand, dealerHand)


def dealer_wins(playerHand, dealerHand, chips):
    print('\nDealer Wins!\n')
    chips.lose_bet()
    print_hands(playerHand, dealerHand)


def tie(playerHand, dealerHand):
    print('\nTie!\n')
    print_hands(playerHand, dealerHand)


def continue_playing():
    while True:
        ans = input('Continue playing? Yes or no: ')
        if ans.lower() != 'yes' and ans.lower() != 'no':
            print('Invalid input')
        else:
            return True if ans.lower() == 'yes' else False


if __name__ == '__main__':
    '''
    Initializing the chips
    '''
    chips = Chips()  # pass value if you want to start with a different totals. Default is 100

    '''
    Game Phase
    '''
    playing = True
    while playing:
        '''
        Initializing the deck
        '''
        deck = Deck()
        init_deck(deck)
        deck.shuffle()

        '''
        Taking a bet from a player
        '''
        take_bet(chips)

        '''
        Initializing the hand. Note that the dealer only starts with one card
        '''
        playerHand = Hand()
        dealerHand = Hand()
        init_hand()

        '''
        Player turn
        '''
        while True:
            hit = ask_hit()
            if hit:
                playerHand.add_card(deck.hit())
                print(playerHand)
                if playerHand.value > 21:
                    player_bust(playerHand, dealerHand, chips)
                    break
            else:
                break

        '''
        Dealer Turn. Beat player value or bust
        '''
        while True:
            '''
            Check if player busted. If so, no need for Dealer to play
            '''
            if playerHand.value > 21:
                break
            if dealerHand.value > playerHand.value:
                dealer_wins(playerHand, dealerHand, chips)
                break
            elif dealerHand.value == 21 and playerHand.value == 21:
                tie(playerHand, dealerHand)
                break
            else:
                dealerHand.add_card(deck.hit())
                if dealerHand.value > 21:
                    dealer_bust(playerHand, dealerHand, chips)
                    break

        print(chips)
        playing = continue_playing()

class Hand:
    specialCards = ['K', 'Q', 'J']
    ace = 'A'

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        if card.sign == self.ace:
            self.aces += 1
        self.calculate_value()

    def calculate_value(self):
        self.value = 0
        for card in self.cards:
            try:
                value = int(card.sign)
                self.value += value
            except:
                if card.sign in self.specialCards:
                    self.value += 10
                else:
                    self.value += 11
            while self.value > 21 and self.aces > 0:
                self.value -= 10
                self.aces -= 1
        if self.value == 21:
            print('Blackjack!')

    def __str__(self):
        str = ''
        for card in self.cards:
            str += f'{card.sign}{card.suite} '
        return f'{str}\nValue:{self.value}'

class Card:

    def __init__(self, suite, sign):
        self.suite = suite
        self.sign = sign

    def __str__(self):
        return f'{self.suite}{self.sign}'

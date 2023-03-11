class Card:
    def __init__(self,card_value,suit):
        self.card_value = card_value
        self.card_value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][card_value-1]
        self.suit = '♥♦♣♠'[suit]
        

    def price(self):
        if self.card_value >= 10:
            return 10
        elif self.card_value == 1:
            return 11
        return self
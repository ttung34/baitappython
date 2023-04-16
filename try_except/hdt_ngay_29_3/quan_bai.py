class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def print_card(self):
        print(f'{self.suit}--{self.value}')

class Deck_of_card:
    def __init__(self):
        self.cards = []
        suits = [3,4,5,6,7,8,9,10,'J','Q','K','A',2]
        values =['Ro','Co','Bich','Tep']
        for suit in suits:
            for value in values:
                card = Card(suit,value)
                self.cards.append(card)
    
    def shuffle_card(self):
        shuffle (self.cards)

    def print_deck_of_card(self):
        for card in self.cards:
            card.print_card()

    def __str__(self):
        for card in self.cards:
            card.print_card()
        return card.print_card()
    
    def divide_card(self):
        post = self.cards.pop(-1)
        return post
    
class Player:
    def __init__(self, name):
        self.name =name
        self.own =[]

    def take_cards(self, card):
        self.own.append(card)

    def print_cards(self):
        for card in self.own:
            # It prints the card.
            card.print_card() 


deck_card =Deck_of_card()
deck_card.shuffle_card()
p1 = Player("Tung")
p2 = Player("Trang")
p3 = Player("Nguyen")
p4 = Player("Nguyet")
play = [p1,p2,p3,p4]
for i in range(3):
    for player in play:
        player.take_cards(deck_card)
for player in play:
    player.print_cards()



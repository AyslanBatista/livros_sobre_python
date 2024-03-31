"""
Como exercício, escreva um método __lt__ para objetos Time. Você pode usar
uma comparação de tuplas, mas também pode usar a comparação de números
inteiros.
"""


class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [
        None,
        'Ace',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'Jack',
        'Queen',
        'King',
    ]

    def __str__(self):
        return '%s of %s' % (
            Card.rank_names[self.rank],
            Card.suit_names[self.suit],
        )

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


card1 = Card(2, 2)
card2 = Card(3, 3)

print(card1 > card2)

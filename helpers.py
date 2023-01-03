import random


CARD_COLOR = ("carreau", "coeur", "pique", "trefle")
CARD_RANK = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "valet",
    "dame",
    "roi",
    "as",
)


class Deck(list):
    def __init__(self):
        # crée le deck
        for color in CARD_COLOR:
            for rank in CARD_RANK:
                card = Card(color, rank)
                self.append(card)
        self.shuffle()

    def shuffle(self):
        # mélange le deck
        random.shuffle(self)

    def draw_card(self):
        # tire une carte du deck
        try:
            return self.pop()
        except IndexError:
            return None


class Card:
    def __init__(self, color, rank):
        self.color = color
        self.rank = rank
        self.visible = False
        self.score_rank = CARD_RANK.index(self.rank)
        self.score_color = CARD_COLOR.index(self.color)

    def __str__(self):
        # sorte de tostring
        return f"{self.rank} de {self.color}"

    def __repr__(self):
        # sorte de toobject
        return str(self)

    def __lt__(self, other):
        if self.score_rank != other.score_rank:
            return self.score_rank < other.score_rank

        return self.score_color < other.score_color


class Player:
    def __init__(self, name):
        self.name = name
        self.card = Hand()


class Hand(list):
    def append(self, object):
        if not isinstance(object, Card):
            return ValueError("object must be card")
        return super().append(object)

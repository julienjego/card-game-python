from models import CARD_COLOR, CARD_RANK, Player


class CheckerRankAndSuitIndex:
    def check(self, players):
        last_player = self.players[0]
        best_candidate = self.players[0]

        for player in self.players[1:]:
            player_card = player.hand[0]
            last_player_card = last_player.hand[0]

            score = (
                CARD_RANK.index(player_card.rank),
                CARD_COLOR.index(player_card.color),
            )
            last_score = (
                CARD_RANK.index(last_player_card.rank),
                CARD_COLOR.index(last_player_card.color),
            )

            if score[0] == last_score[0]:
                if score[1] > last_score[1]:
                    best_candidate = player
            elif score[0] > last_score[0]:
                best_candidate = player

            last_player = player

        return best_candidate.name


class Controller:
    def __init__(self, deck, view, checker_strategy):
        # Modèles
        self.deck = deck
        self.players = []

        # Vue
        self.view = view
        self.checker_strategy = checker_strategy

    def get_players(self):
        while len(self.players) < 2:
            name = self.view.prompt_for_players()
            if not name:
                return
            player = Player(name)
            self.players.append(player)

    def start_game(self):
        self.deck.shuffle()
        for player in self.players:
            card = self.deck.draw_card()
            if card:
                player.hand.append(card)

    def evaluate_game(self):
        self.checker_strategy.check(self.players)

    def rebuild_deck(self):
        for player in self.players:
            while player.hand:
                card = player.hand.pop()
                card.is_visible = False
                self.deck.append(card)
        self.deck.shuffle()

    def run(self):
        self.get_players()

        running = True
        while running:
            self.start_game()
            for player in self.players:
                self.view.show_player_hand(player.name, player.hand)
            self.view.prompt_for_flip_cards()
            for player in self.players:
                for card in player.hand:
                    card.is_visible = True
                self.view.show_player_hand(player.name, player.hand)

            self.view.show_winner(self.evaluate_game())

            running = self.view.prompt_for_new_game()
            self.rebuild_deck()

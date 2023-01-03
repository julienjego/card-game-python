class View:
    def prompt_for_players(self):
        name = input("nom du joueur: ")
        if not name:
            return None
        return name

    def prompt_for_flip_cards(self):
        print()
        input("on retourne les cartes")
        return True

    def show_player_hand(self, name, hand):
        print(f"[Joueur {name}]")
        for card in hand:
            if card.is_visible:
                print(card)
            else:
                print("Carte face cachée")

    def show_winner(self, name):
        print(f"Bravo {name} !")

    def prompt_for_new_game(self):
        print("nouvelle partie ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True

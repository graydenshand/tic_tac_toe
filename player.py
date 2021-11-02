class Player:
    def init_game(self, game, player_number):
        self.game = game
        self.number = player_number
        if player_number == 1:
            self.mark = 1
        elif player_number == 2:
            self.mark = -1
        else:
            raise ValueError("Illegal player_number")

    def choose_position(self):
        raise NotImplementedError

    def __str__(self):
        return f"Player{self.number}"

    def __repr__(self) -> str:
        return str(self)

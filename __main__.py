from .game import Game
from .human_player import Human
from .computer_player import Computer
import numpy as np

game_mode = input(
    f"What game mode would you like to play?\n1: Human vs Human\n2: Human vs Computer\n"
)

if game_mode == "1":
    game = Game(Human(), Human())
elif game_mode == "2":
    players = [Human(), Computer()]
    np.random.shuffle(players)
    game = Game(players[0], players[1])
else:
    raise NotImplementedError

game.run()

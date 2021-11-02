from .game import Game
from .computer_player import Computer
import json


player1, player2 = Computer(training=True), Computer(training=True)

with open(f"tic_tac_toe/player1_states.json", "r") as f:
    player1.state_scores = json.loads(f.read())
with open(f"tic_tac_toe/player2_states.json", "r") as f:
    player2.state_scores = json.loads(f.read())


def get_loser(winner):
    if winner == 0:
        return 0
    return player1 if player2 == winner else player2


scoreboard = {player1: 0, player2: 0, "Draw": 0}

NUM_GAMES = 10000
for i in range(1, NUM_GAMES + 1):
    game = Game(player1, player2)
    winner = game.run()
    if winner != 0:
        winner.feed_reward(1)
        loser = get_loser(winner)
        loser.feed_reward(0)
        scoreboard[winner] += 1
    else:
        player1.feed_reward(0.5)
        player2.feed_reward(0.5)
        scoreboard["Draw"] += 1

print("Summary")
print("Games played: %i" % NUM_GAMES)
print(scoreboard)


# Save states
with open("tic_tac_toe/player1_states.json", "w") as f:
    sorted_states = {
        k: v
        for k, v in sorted(
            player1.state_scores.items(), key=lambda x: x[1], reverse=True
        )
    }
    f.write(json.dumps(sorted_states))

with open("tic_tac_toe/player2_states.json", "w") as f:
    sorted_states = {
        k: v
        for k, v in sorted(
            player2.state_scores.items(), key=lambda x: x[1], reverse=True
        )
    }
    f.write(json.dumps(sorted_states))

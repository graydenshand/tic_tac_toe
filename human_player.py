from .player import Player

class Human(Player):
  def choose_position(self):
    user_input = input("Enter position to claim: ")
    stripped_input = user_input.strip(" ()")
    if len(stripped_input) != 3 or stripped_input[1] != ",":
      raise ValueError(f"Illegal input: {user_input}")
    i, j = stripped_input.split(",")
    position = (int(i),int(j))
    self.game.board[position] = self.mark
    return (position)

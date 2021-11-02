import numpy as np
from .human_player import Human
from .board import Board
from .player import Player

class Game:
  """
  A Tic Tac Toe Game
  """
  def __init__(self, p1, p2):
    self.board = Board()
    self.p1 = p1
    self.p1.init_game(self, 1)
    self.p2 = p2
    self.p2.init_game(self, 2)
    self.game_over = False
    self.current_player = self.p1
    self.has_human_player = (isinstance(p1, Human) or isinstance(p2, Human))

  def switch_players(self):
    self.current_player = self.p2 if self.current_player == self.p1 else self.p1

  @property
  def available_positions(self):
    positions = []
    for i in range(3):
      for j in range(3):
        if self.board[i,j] == 0:
          positions.append((i,j))
    return positions

  @property
  def winner(self):
    # Check rows
    for i in range(3):
      row_sum = sum(self.board[i, :])
      if row_sum == 3:
        return self.p1
      elif row_sum == -3:
        return self.p2

    # Check columns
    for j in range(3):
      col_sum = sum(self.board[:,j])
      if col_sum == 3:
        return self.p1
      elif col_sum == -3:
        return self.p2

    # Check diagonals
    diag_sum_1 = sum([self.board[i,i] for i in range(3)])
    diag_sum_2 = sum([self.board[i, 2-i] for i in range(3)])
    diag_sum = max(abs(diag_sum_1), abs(diag_sum_2))
    if diag_sum == 3:
      if diag_sum_1 == 3 or diag_sum_2 == 3:
        return self.p1
      else:
        return self.p2

    # Draw
    if len(self.available_positions) == 0:
      return 0

    # Game still ongoing
    return None

  def give_reward(self):
    result = self.winner()
    if result == 1:
      self.p1.feed_reward(1)
      self.p2.feed_reward(0)
    elif result == -1:
      self.p1.feedReward(0)
      self.p2.feedReward(1)
    elif result == 0:
      self.p1.feedReward(0.1)
      self.p2.feedReward(0.5)

  def run(self):
    while self.winner is None:
      if self.has_human_player:
        print(self.board)
        print(f"{self.current_player} move: ")
        position = None
        while position is None:
          try:
            position = self.current_player.choose_position()
          except ValueError as e:
            position = None
            print(e)
      else:  
        self.current_player.choose_position()
      self.switch_players()

    if self.has_human_player:
      print(self.board)
      if self.winner == 0:
        print("Game over, draw!")
      else:
        print(f"Game over, {self.winner} wins!")

    return self.winner
    
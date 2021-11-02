from .player import Player
import numpy as np
import copy
import json

class Computer(Player):
  exp_rate = 0.1
  lr = 0.3
  decay_gamma = 0.9
  
  def __init__(self, training=False):
    super().__init__()
    self.states = []
    self.state_scores = {}
    self.training = training

  def choose_position(self):
    positions = self.game.available_positions
    if self.training and np.random.uniform(0,1) <= self.exp_rate:  
      index = np.random.choice(range(len(positions)))   
      position = positions[index]
    else:
      max_score = -1
      for p in positions:
        next_board = copy.deepcopy(self.game.board)
        next_board[p] = self.mark
        next_board_state = next_board.state
    
        score = 0. if next_board_state not in self.state_scores else self.state_scores[next_board_state]

        if not self.training:
          print(self, p, score)
        if score > max_score:
          position = p
          max_score = score
          next_state = next_board_state

      if not self.training:
        print(self, "Best move", position, max_score)
    # Update the board
    self.game.board[position] = self.mark
    # Add the selected move to 'states' object
    self.states.append(self.game.board.state)

    
    
    if self.game.board.state not in self.state_scores.keys():
      print(f"{self} Trying something new", self.game.board.state)
      self.state_scores[self.game.board.state] = 0

    return position

  def init_game(self, game, player_number):
    super().init_game(game, player_number)
    self.states = []
    if not self.training:
      # Load pre-trained scores
      with open(f"tic_tac_toe/player{player_number}_states.json", "r") as f:
        self.state_scores = json.loads(f.read())

  def feed_reward(self, reward):
    for st in reversed(self.states):
      if self.state_scores.get(st) is None:
        self.state_scores[st] = 0
      new_score = self._calculate_score_change(self.state_scores[st], reward)
      self.state_scores[st] = new_score
      reward = new_score


  def _calculate_score_change(self, original, reward):
    new_score = original + (self.lr * (self.decay_gamma * reward - original))
    return new_score

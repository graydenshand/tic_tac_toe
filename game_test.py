from .game import Game
from .board import Board
from .player import Player
import pytest

@pytest.fixture
def game():
  return Game(Player(), Player())

def test_switch_players(game):
  assert game.current_player == game.p1
  game.switch_players()
  assert game.current_player == game.p2
  game.switch_players()
  assert game.current_player == game.p1

def test_winner(game):
  # Not finished
  assert game.winner is None

  # Columns
  game.board = Board([0,0,1,0,0,1,0,0,1])
  assert game.winner == game.p1
  game.board = Board([0,-1,0,0,-1,0,0,-1,0])
  assert game.winner == game.p2

  # Rows
  game.board = Board([-1,-1,-1,0,0,0,0,0,0])
  assert game.winner == game.p2
  game.board = Board([0,0,0,1,1,1,0,0,0])
  assert game.winner == game.p1

  # Draw
  game.board = Board([-1,1,1,1,1,-1,-1,-1,1])
  assert game.winner == 0
  

def test_available_positions(game):
  game.board = Board([0,1,0,1,1,-1,-1,-1,1])
  assert game.available_positions == [(0,0), (0,2)]
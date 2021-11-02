from .board import Board
import pytest

@pytest.fixture
def board():
  return Board()

def test_board_get(board):
  assert board[0,0] == 0

def test_board_set(board):
  board[0,1] = 1
  assert board[0,1] == 1

def test_state(board):
  board[2,1] = 1
  assert board.state == "[0. 0. 0. 0. 0. 0. 0. 1. 0.]"

def test_str(board):
  board[2,1] = 1
  assert str(board) == " _ | _ | _ \n _ | _ | _ \n _ | X | _ "
  print(board)
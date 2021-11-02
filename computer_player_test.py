from .computer_player import Computer
from .game import Game
import pytest


@pytest.fixture
def computer():
    return Computer()


def test_init_game(computer):
    mock_game = "test"
    computer.init_game(mock_game, 2)
    assert computer.game == mock_game
    assert computer.number == 2
    assert computer.mark == -1


def test_choose_position_chooses_optimal_score(computer):
    game = Game(computer, Computer())
    computer.state_scores = {
        "[0. 0. 0. 0. 1. 0. 0. 0. 0.]": 0.9,
        "[1. 0. 0. 0. 0. 0. 0. 0. 0.]": 0.1,
    }
    assert computer.state_scores.get("[1. 0. 0. 0. 0. 0. 0. 0. 0.]") is not None
    computer.choose_position()
    print(game.board)
    assert game.board[1, 1] == 1


def test_feed_reward(computer):
    computer.state_scores = {}
    computer.states = [
        "[0. 0. 0. 0. 1. 0. 0. 0. 0.]",
        "[-1. 0. 0. 0. 1. 0. 0. 1. 0.]",
        "[-1. 1. 0. -1. 1. 0. 0. 1. 0.]",
    ]
    computer.feed_reward(1)
    assert len(computer.state_scores) == 3
    score1 = computer._calculate_score_change(0, 1)
    score2 = computer._calculate_score_change(0, score1)
    score3 = computer._calculate_score_change(0, score2)
    assert computer.state_scores["[0. 0. 0. 0. 1. 0. 0. 0. 0.]"] == score3
    assert computer.state_scores["[-1. 0. 0. 0. 1. 0. 0. 1. 0.]"] == score2
    assert computer.state_scores["[-1. 1. 0. -1. 1. 0. 0. 1. 0.]"] == score1

    computer2 = Computer()
    computer2.state_scores = {}
    computer2.states = [
        "[-1. 0. 0. 0. 1. 0. 0. 0. 0.]",
        "[-1. 0. 0. -1. 1. 0. 0. 1. 0.]",
    ]
    computer2.feed_reward(0)
    assert len(computer2.state_scores) == 2
    assert computer2.state_scores["[-1. 0. 0. 0. 1. 0. 0. 0. 0.]"] == 0
    assert computer2.state_scores["[-1. 0. 0. -1. 1. 0. 0. 1. 0.]"] == 0

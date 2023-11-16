from logic import Board, Game, Human, Bot
import pytest
def test_empty_board():
    board = Board()
    for x in range(3):
        for y in range(3):
            assert board.get(x, y) is None, "Board should be initialized with all None"

def test_set_and_get():
    board = Board()
    board.set(0, 0, 'X')
    assert board.get(0, 0) == 'X', "Set and Get methods should correctly update and return board state"

def test_board_full():
    board = Board()
    for x in range(3):
        for y in range(3):
            board.set(x, y, 'X')
    assert board.is_full(), "Board should be full when all cells are occupied"

def test_winner():
    board = Board()
    # Set up a winning condition
    board.set(0, 0, 'X')
    board.set(1, 1, 'X')
    board.set(2, 2, 'X')
    assert board.get_winner(), "Should detect a winner"

def test_no_winner():
    board = Board()
    assert not board.get_winner(), "Should not detect a winner on an empty board"
import random
class Board:
  def __init__(self):
    self._rows = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

  def __str__(self):
    s = '-------\n'
    for row in self._rows:
      for cell in row:
        s = s + '|'
        if cell == None:
          s=s+' '
        else:
          s=s+cell
      s = s + '|\n-------\n'
    return s

  def get(self, x, y):
    return self._rows[y][x]

  def set(self, x, y, value):
    self._rows[y][x] = value

  def is_full(self):
        return all(cell is not None for row in self._rows for cell in row)


  def get_winner(self):
        for i in range(3):
            if self._rows[i][0] == self._rows[i][1] == self._rows[i][2] is not None or \
               self._rows[0][i] == self._rows[1][i] == self._rows[2][i] is not None:
                return True
        if self._rows[0][0] == self._rows[1][1] == self._rows[2][2] is not None or \
           self._rows[0][2] == self._rows[1][1] == self._rows[2][0] is not None:
            return True
        return False

class Game:
    def __init__(self, playerX, playerO):
        self._board = Board()
        self._playerX = playerX
        self._playerO = playerO
        self._current_player = self._playerX

    def run(self):
        while not self._board.is_full() and not self._board.get_winner():
            print(self._board)
            move = self._current_player.get_move(self._board)
            x, y = move
            if self._board.get(x, y) is None:
                self._board.set(x, y, 'X' if self._current_player == self._playerX else 'O')
                self._current_player = self._playerO if self._current_player == self._playerX else self._playerX
            else:
                print("Invalid move. Try again.")

        print(self._board)
        if self._board.get_winner():
            print("We have a winner!")
        else:
            print("It's a draw!")

class Human:
    def get_move(self, board):
        move = input("Enter your move (x y): ").split()
        return int(move[0]), int(move[1])

class Bot:
    def get_move(self, board):
        available_moves = [(x, y) for x in range(3) for y in range(3) if board.get(x, y) is None]
        return random.choice(available_moves) if available_moves else (None, None)
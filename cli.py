from logic import Board, Game, Human, Bot

player_choice = input("Choose 1 for single player or 2 for two players: ")
if player_choice == "1":
    game = Game(Human(), Bot())
else:
    game = Game(Human(), Human())
game.run()
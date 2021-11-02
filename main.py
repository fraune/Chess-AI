from agent.ChessGame import ChessGame


def start():
    game = ChessGame()
    game.play_until(3)


start()

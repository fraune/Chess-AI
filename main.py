from agent.ChessGame import ChessGame
from utility.logger import Logger


def start():
    logger = Logger(print_to_file=True)

    game = ChessGame()
    game.play_until(1)

    logger.close()


start()

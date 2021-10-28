import chess

from agent.Scorer import Scorer


def start():
    board = chess.Board()
    scorer = Scorer()
    scorer.evaluate(board)


start()

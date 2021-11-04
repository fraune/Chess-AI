import random

import chess

from agent.BoardStateTreeNode import BoardStateTreeNode
from agent.Scorer import Scorer
from utility.Logger import Logger


class Player:
    logger: Logger

    def __init__(self):
        self.logger = Logger()


class SearchPlayer(Player):
    tree_depth: int
    tree_width: int

    def __init__(self, depth: int, width: int):
        self.tree_depth = depth
        self.tree_width = width

    def get_next_move(self, board: chess.Board):
        bstn = BoardStateTreeNode(board, max_children=self.tree_width)
        bstn.populate_tree(self.tree_depth)
        moves = bstn.evaluate_moves(Scorer())

        if len(moves) == 0:
            self.logger.log('No scored moves')
            return

        moves.sort(key=lambda tup: tup[0], reverse=True)

        # index 0 picks tuple with highest score for white, index 1 picks move out of that tuple
        return moves[0][1]


class RandomPlayer(Player):

    def get_next_move(self, board: chess.Board):
        bstn = BoardStateTreeNode(board)
        moves = bstn.enumerate_moves()

        if len(moves) <= 0:
            self.logger.log('No scored moves')
            return

        move_index = random.randint(0, len(moves) - 1)
        return moves[move_index]

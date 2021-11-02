import random

import chess

from agent.BoardStateTreeNode import BoardStateTreeNode
from agent.Scorer import Scorer


class Player:
    pass


class SearchPlayer(Player):
    tree_depth: int
    tree_width: int

    def __init__(self, depth: int, width: int):
        self.tree_depth = depth
        self.tree_width = width

    def play_move(self, board: chess.Board):
        bstn = BoardStateTreeNode(board, max_children=self.tree_width)
        bstn.populate_tree(self.tree_depth)
        moves = bstn.evaluate_moves(Scorer())

        if len(moves) == 0:
            print('No scored moves')
            return

        moves.sort(key=lambda tup: tup[0], reverse=True)
        move = moves[0][1]
        board.push(move)


class RandomPlayer(Player):

    def play_move(self, board: chess.Board):
        bstn = BoardStateTreeNode(board)
        moves = bstn.enumerate_moves()

        if len(moves) <= 0:
            print('No scored moves')
            return

        move_index = random.randint(0, len(moves))
        board.push(moves[move_index])

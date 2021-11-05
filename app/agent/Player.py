import random

import chess

from app.agent.BoardStateTreeNode import BoardStateTreeNode
from app.agent.PlayerType import PlayerType
from app.agent.Scorer import Scorer
from app.config import MAXIMUM_TREE_DEPTH, MAXIMUM_TREE_WIDTH
from app.utility.Logger import Logger


def create_player_from_enum(player_type: PlayerType):
    if player_type is PlayerType.RANDOM:
        return RandomPlayer()
    elif player_type is PlayerType.SEARCH:
        return SearchPlayer(MAXIMUM_TREE_DEPTH, MAXIMUM_TREE_WIDTH)
    else:
        raise ValueError(f'Unknown PlayerType: {player_type}')


class Player:
    logger: Logger

    def __init__(self):
        self.logger = Logger()


class RandomPlayer(Player):
    player_type = PlayerType.RANDOM

    def get_next_move(self, board: chess.Board):
        root = BoardStateTreeNode(board)
        moves = root.enumerate_moves()

        if len(moves) <= 0:
            self.logger.log('No scored moves')
            return

        move_index = random.randint(0, len(moves) - 1)
        return moves[move_index]


class SearchPlayer(Player):
    player_type = PlayerType.SEARCH
    _tree_depth: int
    _tree_width: int

    def __init__(self, depth: int, width: int):
        super().__init__()
        self._tree_depth = depth
        self._tree_width = width

    def get_next_move(self, board: chess.Board):
        root = BoardStateTreeNode(board, max_children=self._tree_width)
        root.populate_tree(self._tree_depth)
        moves = root.evaluate_moves(Scorer())

        if len(moves) == 0:
            self.logger.log('No scored moves')
            return

        moves.sort(key=lambda tup: tup[0], reverse=True) # TODO: test for black vs white

        # index 0 picks tuple with highest score for white, index 1 picks move out of that tuple
        return moves[0][1]

import random

import chess

from agent.BoardStateTreeNode import BoardStateTreeNode


class Player:
    _moves: list[chess.Move]

    def play_move(self, board: chess.Board):
        self._enumerate_game_states(board)
        self._score_moves()
        move = self._choose_move()
        board.push(move)


class RandomPlayer(Player):
    def _enumerate_game_states(self, board: chess.Board):
        bstn = BoardStateTreeNode(board)
        self.moves = bstn.enumerate_moves()

    def _score_moves(self):
        pass

    def _choose_move(self):
        move_index = random.randint(0, len(self._moves))
        return self._moves[move_index]


class SearchPlayer(Player):
    def _enumerate_game_states(self, board: chess.Board):
        bstn = BoardStateTreeNode(board)
        self.moves = bstn.enumerate_moves()

    def _score_moves(self):
        # TODO: write
        # is this needed for random player?
        print('xyz')

    def _choose_move(self):
        move_index = random.randint(0, len(self._moves))
        return self._moves[move_index]

    def play_move(self, board: chess.Board):
        # TODO: write
        self._enumerate_game_states(board)
        # self._score_moves()
        move = self._choose_move()
        board.push(move)

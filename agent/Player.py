import chess


class Player:
    _moves: list[chess.Move]

    def _enumerate_game_states(self, board: chess.Board):
        # TODO: write
        print('xyz')


class RandomPlayer(Player):
    def _score_moves(self):
        # TODO: write
        print('xyz')

    def _choose_move(self):
        # TODO: write
        print('xyz')

    def play_move(self, board: chess.Board):
        # TODO: write
        self._enumerate_game_states(board)
        self._score_moves()
        move = self._choose_move()
        board.push(move)
        print('xyz')

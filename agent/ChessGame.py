import chess


class ChessGame:
    _board: chess.Board
    # _played_turns: int
    _black_player
    _white_player

    def play_turn(self) -> bool:
        # TODO: play

        return self._board.is_game_over()

    def reset(self):
        self._board.reset()
        # More to do here?

    def print_game_stats(self):
        print(f'Game Status: {self._game_status()}')
        print(f'  Whose turn  = {self._whose_turn_color()}')
        print(f'  Turns taken = {self._board.fullmove_number}')  # Increments only after black moves
        print(f'  Is check    = {self._board.is_check()}')  # Increments only after black moves

        if self._board.is_game_over():
            print(f'  Checkmate?   = {self._board.is_checkmate()}')  # Increments only after black moves
            print(f'  Stalemate?   = {self._board.is_stalemate()}')  # Increments only after black moves
            print(f'  Winner color = {self._board.outcome().winner}')  # Increments only after black moves

    def play_until(self, n_turns: int) -> bool:
        for index in range(1, n_turns + 1):
            game_over = self.play_turn()
            if game_over:
                print('Game over')
                return True

    def _game_status(self) -> str:
        return 'game over' if self._board.is_game_over() else 'in progress'

    def _whose_turn_color(self) -> str:
        return 'white' if self._board.turn else 'black'

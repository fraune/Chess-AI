import chess

from agent import Player
from agent.Player import RandomPlayer, SearchPlayer


class ChessGame:
    _board: chess.Board = chess.Board()
    # _played_turns: int  # redundant with Board.fullmove_number
    _black_player: Player = RandomPlayer()
    _white_player: Player = SearchPlayer(3, 15)

    def reset(self):
        self._board.reset()

    def play_until(self, n_turns: int) -> bool:
        for index in range(1, n_turns + 1):
            game_over = self.play_turn()
            if game_over:
                print('Game over')
                return True

    def play_turn(self) -> bool:
        move = self._white_player.get_next_move(self._board) \
            if self._board.turn else self._black_player.get_next_move(self._board)

        if move:
            print(move)
            self._board.push(move)
        return self._board.is_game_over()

    def print_game_stats(self):
        print(f'Game Status: {self._game_status()}')
        print(f'  Whose turn  = {self._whose_turn_color()}')
        print(f'  Turns taken = {self._board.fullmove_number}')  # Increments only after black moves
        print(f'  Is check    = {self._board.is_check()}')

        if self._board.is_game_over():
            print(f'  Checkmate?   = {self._board.is_checkmate()}')
            print(f'  Stalemate?   = {self._board.is_stalemate()}')
            print(f'  Winner color = {self._board.outcome().winner}')
            print(f'  Outcome      = {self._board.outcome()}')

    def _game_status(self) -> str:
        return 'game over' if self._board.is_game_over() else 'in progress'

    def _whose_turn_color(self) -> str:
        return 'white' if self._board.turn else 'black'

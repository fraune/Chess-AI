import chess

from agent import Player
from agent.Player import RandomPlayer, SearchPlayer
from utility.logger import Logger


class ChessGame:
    logger: Logger
    _board: chess.Board = chess.Board()
    # _played_turns: int  # redundant with Board.fullmove_number?
    _black_player: Player = RandomPlayer()
    _white_player: Player = RandomPlayer()  # SearchPlayer(3, 15)

    def __init__(self):
        self.logger = Logger()
        self.logger.log('Chess game initialized')

    def reset(self):
        self.logger.log('Chess game reset')
        self._board.reset()

    def play_until(self, half_moves: int) -> bool:
        for index in range(1, half_moves + 1):
            self.print_game_stats()
            game_over = self.play_turn()
            if game_over:
                return True
        self.logger.log({'fen': self._board.fen()})

    def play_turn(self) -> bool:
        move = self._white_player.get_next_move(self._board) \
            if self._board.turn else self._black_player.get_next_move(self._board)

        if move:
            self.logger.log(f'{self._whose_turn_color()} pushing {move}')
            self._board.push(move)
        else:
            self.logger.log(f'{self._whose_turn_color()} has no moves')

        return self._board.is_game_over()

    def print_game_stats(self):
        details = {
            'game status': self._game_status(),
            'next turn': self._whose_turn_color(),
            'turn number': self._board.fullmove_number,  # starts at 1, increments only after black moves
            'is check': self._board.is_check()
        }

        if self._board.is_game_over():
            details['is checkmate'] = self._board.is_checkmate()
            details['is stalemate'] = self._board.is_stalemate()
            details['winning color'] = self._board.outcome().winner
            details['outcome'] = self._board.outcome()

        self.logger.log(details)

    def _game_status(self) -> str:
        return 'game over' if self._board.is_game_over() else 'in progress'

    def _whose_turn_color(self) -> str:
        return 'white' if self._board.turn else 'black'

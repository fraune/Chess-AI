from datetime import datetime
from typing import Optional

import chess

from app.agent import Player
from app.agent.PlayerType import PlayerType
from app.utility.Logger import Logger


class ChessGame:
    logger: Logger
    _board: chess.Board
    _plies_made: int = 0
    _white_player: Player
    _black_player: Player
    _start_time: datetime
    _end_time: datetime

    def __init__(self, white_player: Player, black_player: Player):
        self._start_time = datetime.now()
        self.logger = Logger()
        self._board = chess.Board()
        self._white_player = white_player
        self._black_player = black_player
        self.logger.log('Chess game initialized')

    def reset(self):
        self.logger.log('Chess game reset')
        self._board.reset()

    def play_until(self, half_moves: int) -> bool:
        for index in range(1, half_moves + 1):
            self.print_game_stats()
            game_over = self.play_turn()
            if game_over:
                break
        self.print_game_stats()
        self.logger.log({'fen': self._board.fen()})

        self._end_time = datetime.now()
        return self._board.is_game_over()

    def play_turn(self) -> bool:
        move = self._white_player.get_next_move(self._board) \
            if self._board.turn else self._black_player.get_next_move(self._board)

        if move:
            self.logger.log(f'{self._whose_turn_color()} pushing {move}')
            self._board.push(move)
            self._plies_made += 1
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
            details['winning color'] = self._winner()
            details['outcome'] = self._board.outcome().termination.name

        self.logger.log(details)

    def _game_status(self) -> str:
        return 'game over' if self._board.is_game_over() else 'in progress'

    def _whose_turn_color(self) -> str:
        return 'white' if self._board.turn else 'black'

    def _winner(self) -> Optional[str]:
        if not self._board.is_game_over():
            return None

        winner = self._board.outcome().winner
        if winner is True:
            return 'white'
        elif winner is False:
            return 'black'
        elif winner is None:
            return 'draw'
        else:
            return '???'

    def _count_pieces(self) -> tuple[int, int]:
        fen = self._board.fen()
        num_white = fen.count('P') + fen.count('N') + fen.count('B') + fen.count('R') + fen.count('Q') + fen.count('K')
        num_black = fen.count('p') + fen.count('n') + fen.count('b') + fen.count('r') + fen.count('q') + fen.count('k')
        return num_white, num_black

    def summary(self) -> dict:
        white_count, black_count = self._count_pieces()
        
        summary_json = {
            'white_player_type': self._white_player.player_type.name,
            'black_player_type': self._black_player.player_type.name,
            'game_state': self._game_status(),
            'outcome': self._board.outcome().termination.name if self._board.is_game_over() else None,
            'winner': self._winner(),
            'turn_number': self._board.fullmove_number,
            'plies_made': self._plies_made,
            'game_start_time': str(self._start_time),
            'game_end_time': str(self._end_time),
            'game_time_seconds': (self._end_time - self._start_time).total_seconds(),
            'fen': self._board.fen(),
            'white_remaining': white_count,
            'black_remaining': black_count,
        }

        if self._white_player.player_type is PlayerType.SEARCH:
            summary_json['white_search_depth'] = self._white_player.tree_depth
            summary_json['white_search_width'] = self._white_player.tree_width
        if self._black_player.player_type is PlayerType.SEARCH:
            summary_json['black_search_depth'] = self._black_player.tree_depth
            summary_json['black_search_width'] = self._black_player.tree_width

        return summary_json

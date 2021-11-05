from typing import Optional

from app.agent.PlayerType import PlayerType


class Configuration:
    def __init__(self, matches: int, white_player_type: PlayerType, black_player_type: PlayerType,
                 search_depth: Optional[int] = None, search_width: Optional[int] = None):
        self.matches = matches
        self.white_player_type = white_player_type
        self.black_player_type = black_player_type
        self.search_tree_depth = search_depth
        self.search_tree_width = search_width

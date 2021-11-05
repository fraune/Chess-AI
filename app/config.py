from typing import Optional

from app.agent.PlayerType import PlayerType
from app.utility.LogLevel import LogLevel
from app.utility.Simulation import Simulation
from app.utility.experiment import experiment

# utility.Logger.Logger
PRINT_TO_CONSOLE: bool = True
PRINT_TO_FILE: bool = False
LOG_FILE_NAME: Optional[str] = None  # Overrides Logger's automatic file name generation. Used if PRINT_TO_FILE is set.
LOG_LEVEL_FILTER: LogLevel = LogLevel.INFO

# utility.simulator
#   Affects v1 simulations only
v1_GAMES_TO_SIMULATE: int = 10  # Random vs Random ~1000 games per minute?
v1_MAXIMUM_PLIES_PER_GAME: int = 1000  # Most "Random VS Random" games are completed in less than 300 total plies
#   Affects v2 simulations only
v2_SIMULATION_CONFIGURATIONS: list[Simulation] = experiment

# agent.ChessGame.ChessGame
#   Affects v1 simulations only
WHITE_PLAYER_TYPE: PlayerType = PlayerType.RANDOM
BLACK_PLAYER_TYPE: PlayerType = PlayerType.RANDOM  # Haven't validated Search with Black

# agent.Player.SearchPlayer
#   Affects v1 simulations only
MAXIMUM_TREE_DEPTH: int = 2  # Factor to limit the number of plies to look ahead
MAXIMUM_TREE_WIDTH: int = 5  # Factor to limit the number of possible moves per ply

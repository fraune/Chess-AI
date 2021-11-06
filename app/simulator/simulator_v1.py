from datetime import datetime

from app.agent.ChessGame import ChessGame
from app.agent.Player import create_player_from_enum
from app.config import V1_GAMES_TO_SIMULATE, WHITE_PLAYER_TYPE, BLACK_PLAYER_TYPE, MAXIMUM_PLIES_PER_GAME
from app.simulator.simulator_v2 import logger
from app.utility.Logger import Logger
from app.utility.SummaryWriter import SummaryWriter

logger = Logger()


def run_simulation_set_v1():
    start_datetime = datetime.now()
    now = start_datetime.strftime('%Y%m%d%H%M%S')
    file_name = f'{now}-{V1_GAMES_TO_SIMULATE}x-chess-summary.json'
    sw = SummaryWriter(file_name)

    for simulation in range(1, V1_GAMES_TO_SIMULATE + 1):
        print(f'Starting game {simulation}/{V1_GAMES_TO_SIMULATE}')
        summary = run_one_simulation_v1(simulation)
        dict_to_write = {'simulation': simulation, **summary}
        sw.write_summary(dict_to_write)

    end_datetime = datetime.now()
    time_delta = end_datetime - start_datetime
    avg_time = time_delta.total_seconds() / V1_GAMES_TO_SIMULATE
    print(f'Ran {V1_GAMES_TO_SIMULATE} games in {str(time_delta)} for an average of {avg_time:.6f} seconds per game.')

    logger.flush()
    logger.close()
    sw.flush()
    sw.close()


def run_one_simulation_v1(simulation_number) -> dict:
    logger.log(f'Simulation #{simulation_number} beginning')
    white_player = create_player_from_enum(WHITE_PLAYER_TYPE)
    black_player = create_player_from_enum(BLACK_PLAYER_TYPE)
    game = ChessGame(white_player, black_player)
    game.play_until(MAXIMUM_PLIES_PER_GAME)
    logger.log(f'Simulation #{simulation_number} complete')
    return game.summary()

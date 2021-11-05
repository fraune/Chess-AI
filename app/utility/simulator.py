from datetime import datetime

from app.agent.ChessGame import ChessGame
from app.config import GAMES_TO_SIMULATE, MAXIMUM_PLIES_PER_GAME
from app.utility.Logger import Logger
from app.utility.SummaryWriter import SummaryWriter

logger = Logger()


def run_simulation_set():
    sw = SummaryWriter()
    start_datetime = datetime.now()

    for simulation in range(1, GAMES_TO_SIMULATE + 1):
        print(f'Starting game {simulation}/{GAMES_TO_SIMULATE}')
        summary = run_one_simulation(simulation)
        dict_to_write = {'simulation': simulation, **summary}
        sw.write_summary(dict_to_write)

    end_datetime = datetime.now()
    time_delta = end_datetime - start_datetime
    avg_time = time_delta.total_seconds() / GAMES_TO_SIMULATE
    print(f'Ran {GAMES_TO_SIMULATE} simulations in {str(time_delta)},'
          f'for an average of {avg_time:.6f} seconds per game.')

    logger.flush()
    logger.close()
    sw.flush()
    sw.close()


def run_one_simulation(simulation_number):
    logger.log(f'Simulation #{simulation_number} beginning')
    game = ChessGame()
    game.play_until(MAXIMUM_PLIES_PER_GAME)
    logger.log(f'Simulation #{simulation_number} complete')
    return game.summary()

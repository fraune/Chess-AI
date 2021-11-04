from agent.ChessGame import ChessGame
from config import GAMES_TO_SIMULATE, MAXIMUM_PLIES_PER_GAME
from utility.Logger import Logger
from utility.SummaryWriter import SummaryWriter

logger = Logger()


def run_simulation_set():
    sw = SummaryWriter()

    for simulation in range(1, GAMES_TO_SIMULATE + 1):
        summary = run_one_simulation(simulation)
        dict_to_write = {'simulation': simulation, **summary}
        sw.write_summary(dict_to_write)

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

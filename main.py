from agent.ChessGame import ChessGame
from utility.Logger import Logger
from utility.SummaryWriter import SummaryWriter

# In testing, most games completed in less than 300 random plies
PLIES_TO_SIMULATE = 1000


def run_simulation(simulation_number: int = 1):
    logger = Logger(print_to_file=False)
    logger.log(f'Simulation {simulation_number} beginning')

    game = ChessGame()
    game.play_until(PLIES_TO_SIMULATE)

    logger.log(f'Simulation {simulation_number} complete')
    logger.close()

    return game.summary()


def run_simulation_set(sets_to_run: int):
    sw = SummaryWriter()
    for simulation in range(1, sets_to_run + 1):
        summary = run_simulation(simulation)
        dict_to_write = {'simulation': simulation, **summary}
        sw.write_summary(dict_to_write)
    sw.flush()
    sw.close()


run_simulation_set(1000)

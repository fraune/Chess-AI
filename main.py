from agent.ChessGame import ChessGame
from utility.Logger import Logger
from utility.SummaryWriter import SummaryWriter


def run_simulation(sim_number: int = 1):
    logger = Logger(print_to_file=False)
    logger.log(f'Simulation {sim_number} beginning')

    game = ChessGame()
    game.play_until(999)

    logger.log(f'Simulation {sim_number} complete')
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

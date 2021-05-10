import os
import numpy as np

import covidTTI.utils as utils

if __name__ == "__main__":
    # change working directory to the project root directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir('../')

    # load config file
    config_file = os.path.join("configs","config.yaml")
    config = utils.load_config(config_file)

    # get number of cases
    n_cases = config['pop_params']['prevalence']

    # seed
    seed = 1

        


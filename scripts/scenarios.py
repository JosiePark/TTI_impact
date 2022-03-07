import os
import numpy as np

import covidTTI.utils as utils
import covidTTI.sim as sim

if __name__ == "__main__":
    # change working directory to the project root directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir('../')

    # load config file
    config_file = os.path.join("configs","config.yaml")
    config = utils.load_config(config_file)

    output = sim.run(config)

    print(output)




        


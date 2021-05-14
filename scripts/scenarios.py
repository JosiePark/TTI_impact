import os
import numpy as np

import covidTTI.utils as utils
from covidTTI.model import TTIModel
import covidTTI.analysis as analysis

if __name__ == "__main__":
    # change working directory to the project root directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir('../')

    # load config file
    config_file = os.path.join("configs","config.yaml")
    config = utils.load_config(config_file)

    # seed
    seed = 1

    # create model
    model = TTIModel(config)

    # calculate the R_0 number
    R_0 = analysis.calculate_R_0(model)
    R_eff = analysis.calculate_R_eff(model)
    print('R_0 =', R_0)
    print('R_eff = ', R_eff)




        


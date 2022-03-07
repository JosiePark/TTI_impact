import os
import numpy as np

import covidTTI.utils as utils

CONFIG_FILE = os.path.join("tests","test_config.yaml")
SEED = 1
RNG = np.random.default_rng(seed = SEED)

def test_load_config():
    config = utils.load_config(CONFIG_FILE)
    assert config["pop_params"]["prevalence"] == 1000

def test_bernoulli():
    assert utils.bernoulli(1,RNG)

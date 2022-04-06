import os
import numpy as np

import covidTTI.utils as utils

CONFIG_FILE = os.path.join("tests","test_config.yaml")
SEED = 1
RNG = np.random.default_rng(seed = SEED)
PDF = [0,0,0,1]

def test_init_seed():
    test_rng = utils.init_seed(random_seed=SEED)
    assert type(test_rng) == np.random._generator.Generator

def test_load_config():
    config = utils.load_config(CONFIG_FILE)
    assert config["pop_params"]["prevalence"] == 1000

def test_bernoulli():
    assert utils.bernoulli(1,RNG)

def test_draw_from_pdf():
    result = utils.draw_from_pdf(RNG, PDF)
    assert result == 3
    result = utils.draw_from_pdf(RNG, PDF, size = 2)
    assert result[0] == 3
    assert result[1] == 3





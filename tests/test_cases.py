from covidTTI.utils import load_config
import os

from covidTTI.cases import indexCase
from covidTTI.utils import load_config, calc_incubation_period

CONFIG_FILE = os.path.join("tests", "test_config.yaml")
CONFIG = load_config(CONFIG_FILE)
INCUBATION_PERIOD = calc_incubation_period(10)

def test_indexCase():
    testCase = indexCase(CONFIG, INCUBATION_PERIOD)
    assert testCase.parameters['pop_params']['prevalence'] == 1000
    assert testCase.symptomatic
    
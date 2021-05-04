'''
Script that simulates a single case of covid.

It assigns a probability that they isolate, dependent on the probability of various
testing conditions
'''

import numpy as np

from utils import bernoulli

class indexCase():

    def __init__(
        self, 
        parameters, 
        random_seed
        ):
        self.parameters = parameters
        self.rng = np.random.RandomState(seed=random_seed)

    def simulate_case(self):

        # probability symptomatic vs asymptomatic
        self.symptomatic = bernoulli(self.parameters['epi_params']['p_symptomatic'], self.rng)

        # probability tested, and whether PCR or LFD
        if self.symptomatic:
            self.tested = bernoulli(self.parameters['testing_params']['p_symp_test'], self.rng)
            self.PCR_tested = self.tested*bernoulli(self.parameters['testing_params']['p_PCR_symp'], self.rng)
        else:
            self.tested = bernoulli(self.parameters['testing_params']['p_asymp_test'], self.rng)
            self.PCR_tested = self.tested*bernoulli(self.parameters['testing_params']['p_PCR_asymp'], self.rng)

        # time from infection case is tested
        if self.symptomatic:
            # if case is symptomatic then testing is done day after symptom onset
            self.day_tested = 
        else:


        # time from infection test result is communicated

        # probability positive

        # probability isolate

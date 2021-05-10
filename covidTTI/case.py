'''
Script that simulates a single case of covid.

It assigns a probability that they isolate, dependent on the probability of various
testing conditions
'''

import numpy as np
import uuid

from covidTTI.utils import bernoulli
from covidTTI.parameters import draw_from_incubation_period
from covidTTI.contacts import Contact

class indexCase():

    def __init__(
        self, 
        parameters, 
        random_seed = 1
        ):
        self.parameters = parameters
        self.rng = np.random.default_rng(random_seed)
        self.simulate_case()
        self.init_contacts()

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
            self.day_tested = draw_from_incubation_period(self.rng) + 1
        else:
            # if case is asymptomatic, then assume a uniform probability of being tested
            # during generation time
            self.day_tested = self.rng.random_integers(low = 0, high = self.parameters['epi_params']['max_infectiousness_day'], size = 1)

        # time from infection test result is communicated
        self.day_result = self.day_tested + self.parameters['testing_params']['result_delay']

        # probability positive
        self.positive_result = self.PCR_tested*bernoulli(.5, self.rng)

        # probability isolates

        return

    def init_contacts(self):

        self.contacts = {}

    def populate_contacts(self):
        '''
        Function that populates the contacts of a given index case. Contacts are drawn
        from a poisson distribution

        Categories of contacts are divided into home, work school and community contacts.
        '''
        contact_keys = self.parameters['contact_params'].keys()
        
        for layer in contact_keys:
            n_contacts = np.random.poisson(self.parameters['contact_params'][layer]['n_contacts'], 1)
            for n in n_contacts:
                contact_id = uuid.uuid4().hex
                self.contacts[contact_id] = Contact(self.parameters, contact_layer=layer)

        return 

    


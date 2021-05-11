import numpy as np

import covidTTI.utils as utils

class Contact():

    def __init__(
        self, 
        case,
        is_household = True
        ):

        self.index_case = case
        self.is_household = is_household
        self.parameters = case.parameters
        self.rng = case.rng

        # draw uniformly from the infectious length
        # to get the day that the individual came into
        # contact with the index case
        self.day_exposed = self.rng.random.randint(
            low = 0, 
            high = self.parameters['epi_params']['max_infectious_day']
        )

        self.infect()
        self.trace()
        self.test()
        self.isolate()

    def infect(self):
        '''
        Calculates whether or not the contact has covid
        '''

        if self.index_case.symptomatic:
            infection_scale = 1
        else:
            infection_scale = self.parameters['epi_params']['asymp_factor']

        # if a member of the household
        if self.is_household:
            self.has_covid = utils.bernoulli(
                infection_scale * self.parameters['contact_params']['sar']['household'],
                self.rng
                )
            if self.has_covid:
                # day infected is sample from the infection profile
                self.day_infected = utils.draw_from_viral_load(self.rng)
            else:
                self.day_infected = np.nan
        # if not a member of the household, then
        # the probability the contact has covid is a function of 
        # the day they came into contact, and of the infectiosness
        # distribution
        else:
            # TODO: find value of viral load at day exposed
            viral_load = 0.2
            self.has_covid = utils.bernoulli(
                viral_load * infection_scale * self.parameters['contact_params']['sar']['other'] * self.parameters['epi_params']['max_infectious_day'],
                self.rng
                )
            
            if self.has_covid:
                self.day_infected = self.day_exposed
            else:
                self.day_infected = np.nan        

    def trace(self):
        '''
        Calculate whether the contact was traced or not
        by drawing from a distribution
        '''

    def test(self):
        '''
        Calculate whether (and when) the contact was tested
        '''

    def isolate(self):
        '''
        Calculate whether (and when) the contact isolated
        '''

        


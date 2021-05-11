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
            viral_load = utils.calculate_viral_load(self.day_exposed)
            self.has_covid = utils.bernoulli(
                viral_load * infection_scale * self.parameters['contact_params']['sar']['other'] * self.parameters['epi_params']['max_infectious_day'],
                self.rng
                )
            
            if self.has_covid:
                self.day_infected = self.day_exposed
            else:
                self.day_infected = np.nan  

        # establish whether case is symptomatic or not
        if self.has_covid:
            self.symptomatic = utils.bernoulli(
                self.parameters['epi_params']['p_symp'],
                self.rng
            )
        else:
            self.symptomatic = False      

    def trace(self):
        '''
        Calculate whether the contact was traced or not
        '''

        # if the index case enters contacts, then
        if self.index_case.enters_contacts:
            # if contact is a household member
            # assume tracing is successful
            # and contact is traced on same day as contacts entered
            if self.is_household:
                self.traced = True
                self.day_traced = self.index_case.day_contacts_entered
            else:
                self.traced = utils.bernoulli(
                    self.parameters['trace_params']['p_traced'],
                    self.rng
                )
                # assume tracing occurs a maximum of 3 days after contacts
                # were entered by the index case
                self.day_traced = self.index_case.day_contacts_entered + \
                    self.rng.randint(0, 3)
                
        else:
            self.traced = False
            self.day_traced = np.nan

    def test(self):
        '''
        Calculate whether (and when) the contact was tested
        '''



    def isolate(self):
        '''
        Calculate whether (and when) the contact isolated
        '''

        


import covidTTI.utils as utils

class Contact():

    def __init__(
        self, 
        is_household,
        parameters,
        rng,
        prob_infected = None,
        day_exposed = 1
        ):

        self.is_household = is_household
        self.parameters = parameters
        self.day_exposed = day_exposed
        self.rng = rng

        self.infect(prob_infected)
        self.trace()
        self.test()
        self.isolate()

    def infect(self, prob_infected):
        '''
        Calculates whether or not the contact has covid
        '''

        # if a member of the household, assume infected and day infected is distribution according
        # to the viral load
        if self.is_household:
            self.has_covid = True
        # if not a member of the household, then
        # the probability the contact has covid is a function of 
        # the day they came into contact, and of the infectiosness
        # distribution
        else:
            self.has_covid = utils.bernoulli(prob_infected, self.rng)
            
        if self.has_covid:
            self.day_infectious = utils.draw_from_exposed_to_infectious(self.rng)
            self.day_infected = self.day_infectious + utils.draw_from_viral_load(self.rng)
            

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

        


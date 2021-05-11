import covidTTI.utils as utils

class indexCase():

    def __init__(
        self,
        parameters,
        random_seed = 1
        ):

        self.parameters = parameters
        self.rng = utils.init_seed(random_seed = random_seed)
        self.init_case()
        self.sample_contacts()

    def init_case(self):

        # is symptomatic?
        self.symptomatic = utils.bernoulli(
            self.parameters['epi_params']['p_symp'], 
            self.rng
            )
        # how long in days infectious
        self.infectious_length = self.parameters['epi_params']['max_infectious_day']

    def sample_contacts(self):

        # number of household contacts
        # it is assumed that these contacts are come
        # into contact every day
        self.n_household = self.rng.choice(
            a = self.parameters['contact_params']['household_dict'].keys(), 
            p = self.parameters['contact_params']['household_dict'].values(), 
            size = 1
        )

        # number of non-household contacts
        # it is multiplied by the length of the infectious
        # period
        n_household = 0
        for day in range(self.infectious_length):
            n_household += np.round(
                self.rng.poisson(lam = self.parameters['contact_params']['n_contacts'])
            )

        self.n_other = n_household
        



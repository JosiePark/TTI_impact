import uuid
import numpy as np

from covidTTI.contacts import Contact
import covidTTi.utils as utils

def populate_cases(
    parameters,
    max_days_infectious = 14,
    random_seed = 1
    ):
    '''
    Args:
        n_cases (int) : is the number of index cases of Covid19
        household_dict (dict) : is a dictionary where the key is the number of members
            of a household and the value is the proportion of households with that number
        mean_outside_contacts (int) : is the mean number of non-household contacts an individual has daily
    '''

    # initialise seed
    rng = np.random.default_rng(seed = random_seed)

    # iterate through cases and populate daily contacts for the given case
    cases = {}
    for n in range(parameters['pop_params']['n_cases']):
        cases[n] = {}
        # draw household contacts
        household_contacts = {}
        n_household = rng.choice(
            a = parameters['contact_params']['household_dict'].keys(), 
            p = parameters['contact_params']['household_dict'].values(), 
            size = 1
            )
        # create a dictionary of contacts for given case
        for i in range(n_household):
            household_contacts[i] = Contact(
                is_household = True,
                parameters = parameters,
                rng = rng
                )
        # draw non-household contacts
        # TODO: investigate this distribution
        # draw a new set of contacts for each day
        for day in range(max_days_infectious):
            n_random = np.round(rng.poisson(lam = parameters['contact_params']['mean_daily_contacts']))
            prob_infected = utils.calc_infection_prob_per_day(parameters, n_random)
            random_contacts = {}
            for i in range(n_random):
                random_contacts[i] = Contact(
                    is_household = False,
                    parameters = parameters,
                    rng = rng,
                    prob_infected=prob_infected,
                    day_exposed = day
                    )
        # add contacts to dictionary
        cases[n]['household'] = household_contacts
        cases[n]['random'] = random_contacts

    return cases



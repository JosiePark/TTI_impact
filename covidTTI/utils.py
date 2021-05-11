import yaml
from scipy.stats import gamma
import numpy as np

def init_seed(random_seed = 1):
    '''
    Function that create random generator
    '''
    return np.random.default_rng(seed = random_seed)


def load_config(fpath):
    '''
    Function that loads the config file
    '''

    with open(fpath, 'r') as f:
        config = yaml.safe_load(f)

    return config

def bernoulli(p, rng):
    '''
    Function that draws from a bernoulli distribution with probability p

    Args:
        p (float) : probability the trial was successful
    Return:
        (bool) : whether the trial was successful or not
    '''
    return rng.uniform() < p

def draw_from_incubation_period(rng, size = 1):
    '''
    Draw from the incubation period - defined as the time
    from infection to symptom onset
    '''
    return rng.gamma(shape = 4.23, scale = 1/0.81, size = size)

def draw_from_generation_interval(rng, size = 1):
    '''
    Draw from the generation interval - defined as the time
    between two consecutive infections
    '''
    return 

def draw_from_exposed_to_infectious(rng, size = 1):
    '''
    
    '''

    return rng.lognormal(mean = 4.5, sigma = 1.5, size = 1)

def draw_from_viral_load(rng, size = 1):
    '''

    '''
    return rng.negative_binomial(mean = 1, shape = 0.45, size = size)


def calc_infection_prob_per_day(parameters, n_contacts):
    '''
    beta is a constant called the transmission rate and is the 
    average number of people each infectious person spreads the disease to each day

    Args:
        n_contacts(int): is number of contacts per day
    '''
    # probability of being infected is beta/n_contacts

    return parameters['epi_params']['beta']/n_contacts



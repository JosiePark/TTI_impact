import yaml
from scipy.stats import gamma

def load_config(fpath):

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

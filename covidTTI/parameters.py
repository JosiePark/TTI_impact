from covidTTI.utils import dgamma

def draw_from_incubation_period(rng, option = 'Zhang'):

    if option == 'Zhang':
        return rng.gamma(shape = 4.23, scale = 1/0.81, size = 1)

def calculate_R_0(model):
    '''
    Calculates what the R number would be without any
    interventions or isolating.

    This is the equivalent of the base Reproduction Number, or R0
    '''

    n_cases = len(model.cases)

    # count number of infected secondary cases
    infected_contacts = [c for c in model.contacts if c.has_covid]
    n_infected = len(infected_contacts)

    # R number is the average number of people that an
    # index case infects
    R_0 = n_infected/n_cases

    return R_0

def calculate_R_eff(model):
    '''
    Calculates the R number after interventions and isolating.

    This is equiavelent to the effective Reproduction number
    '''

    # TODO

    return

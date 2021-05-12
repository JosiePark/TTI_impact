import covidTTI.utils as utils

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

def calculate_infections_stopped(model):
    '''
    Calculate what proportion of onward infection was prevented
    by isolation
    '''

    prevented_transmission = 0
    for c in model.contacts:
        if c.isolated:
            # calculate the amount of onward transmission
            # from the day the contact isolate
            onward_transmission = utils.calculate_viral_load(
                c.day_isolated
            )
            prevented_transmission += onward_transmission

    prevented_transmission_per_contact = prevented_transmission/len(model.contacts)
    
    return prevented_transmission_per_contact

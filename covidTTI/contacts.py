class Contact():

    def __init__(self, parameters, household):
        self.parameters = parameters
        self.household = household

    def simulate_contacts(self):

        # probability infected
        if self.household:
            # assume if a household contact, individual is infected
            self.has_covid = True
        else:

        
        # probability contacted

        # probability 

def populate_contacts(Case, parameters):
    '''
    Function that populates the contacts of a given index case
    '''

    # household contacts

    # non-household contacts


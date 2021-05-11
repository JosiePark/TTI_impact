import uuid
import numpy as np

from covidTTI.contacts import Contact
from covidTTI.cases import indexCase

class TTIModel():

    def __init__(
        self, 
        parameters
        ):

        self.parameters = parameters
        self.n_cases = self.parameters['pop_params']['prevalence']
        self.init_cases()
        self.init_contacts()

    def init_cases(self):

        cases = []
        for n in self.n_cases:
            cases.append(indexCase(self.parameters))

        self.cases = cases

    def init_contacts(self):

        secondary_contacts = []
        for case in self.cases:
            for n in range(case.n_household):
                secondary_contacts.append(
                    Contact(case,
                    is_household = True
                    )
                )
            for n in range(case.n_other):
                secondary_contacts.append(
                    Contact(case,
                    is_household = False
                    )
                )
        



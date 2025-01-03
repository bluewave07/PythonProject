import dataclasses

@dataclasses.dataclass
class Player:
    def __init__(self, firstName, lastName, jersey, guardians):
        self.firstName = firstName
        self.lastName = lastName
        self.jersey = jersey
        self.guardians = guardians

    def add_guardian(self, guardian):
        self.guardians.append(guardian)



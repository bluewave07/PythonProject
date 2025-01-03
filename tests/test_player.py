from project.guardian import Guardian
from project.player import Player


def test_construction():
    p = Player('Felicity', 'Smith', 16, [])
    assert p.firstName == 'Felicity'
    assert p.lastName == 'Smith'
    assert p.jersey == 16
    assert [] == p.guardians


def test_add_guardians():
    g = Guardian('Felicity', 'Smith')
    p = Player('Felicity', 'Smith', 16, [])
    p.add_guardian(g)
    assert p.guardians == [g]





